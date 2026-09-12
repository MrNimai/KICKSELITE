-- KicksElite production data model. Run once in Supabase: SQL Editor -> New query -> Run.
create extension if not exists pgcrypto;

create table if not exists public.profiles (
    id uuid primary key references auth.users(id) on delete cascade,
    full_name text not null default '',
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists public.products (
    id text primary key,
    name text not null,
    brand text not null,
    category text not null,
    price numeric(10,2) not null check (price >= 0),
    original_price numeric(10,2),
    image_url text not null,
    images jsonb not null default '[]'::jsonb,
    colors jsonb not null default '[]'::jsonb,
    sizes jsonb not null default '[]'::jsonb,
    stock jsonb not null default '{}'::jsonb,
    description text,
    is_active boolean not null default true,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create table if not exists public.addresses (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references auth.users(id) on delete cascade,
    name text not null,
    line1 text not null,
    city text not null,
    state text not null,
    zip text not null,
    country text not null default 'United States',
    phone text,
    is_default boolean not null default false,
    created_at timestamptz not null default now()
);

create table if not exists public.orders (
    id uuid primary key default gen_random_uuid(),
    order_number text unique not null default ('ORD-' || upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 8))),
    user_id uuid not null references auth.users(id) on delete restrict,
    status text not null default 'Processing' check (status in ('Processing', 'Paid', 'Shipped', 'Delivered', 'Cancelled')),
    shipping_address jsonb not null,
    shipping_method text not null default 'standard',
    subtotal numeric(10,2) not null,
    shipping_total numeric(10,2) not null,
    tax_total numeric(10,2) not null,
    total numeric(10,2) not null,
    created_at timestamptz not null default now()
);

create table if not exists public.order_items (
    id uuid primary key default gen_random_uuid(),
    order_id uuid not null references public.orders(id) on delete cascade,
    product_id text not null references public.products(id),
    product_name text not null,
    color text not null,
    size text not null,
    quantity integer not null check (quantity > 0),
    unit_price numeric(10,2) not null
);

create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
    insert into public.profiles (id, full_name)
    values (new.id, coalesce(new.raw_user_meta_data ->> 'full_name', ''))
    on conflict (id) do nothing;
    return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users
for each row execute procedure public.handle_new_user();

alter table public.profiles enable row level security;
alter table public.products enable row level security;
alter table public.addresses enable row level security;
alter table public.orders enable row level security;
alter table public.order_items enable row level security;

drop policy if exists "Public reads active products" on public.products;
create policy "Public reads active products" on public.products for select using (is_active = true);
drop policy if exists "Users read own profile" on public.profiles;
create policy "Users read own profile" on public.profiles for select to authenticated using (id = auth.uid());
drop policy if exists "Users update own profile" on public.profiles;
create policy "Users update own profile" on public.profiles for update to authenticated using (id = auth.uid()) with check (id = auth.uid());
drop policy if exists "Users read own addresses" on public.addresses;
create policy "Users read own addresses" on public.addresses for select to authenticated using (user_id = auth.uid());
drop policy if exists "Users add own addresses" on public.addresses;
create policy "Users add own addresses" on public.addresses for insert to authenticated with check (user_id = auth.uid());
drop policy if exists "Users update own addresses" on public.addresses;
create policy "Users update own addresses" on public.addresses for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists "Users delete own addresses" on public.addresses;
create policy "Users delete own addresses" on public.addresses for delete to authenticated using (user_id = auth.uid());
drop policy if exists "Users read own orders" on public.orders;
create policy "Users read own orders" on public.orders for select to authenticated using (user_id = auth.uid());
drop policy if exists "Users read own order items" on public.order_items;
create policy "Users read own order items" on public.order_items for select to authenticated using (exists (select 1 from public.orders where orders.id = order_items.order_id and orders.user_id = auth.uid()));

-- This function calculates prices on the database, locks inventory rows, reduces stock,
-- and creates the order. Customers cannot submit a different price from their browser.
create or replace function public.create_order(p_items jsonb, p_shipping_address jsonb, p_shipping_method text default 'standard')
returns table(order_id uuid, order_number text)
language plpgsql security definer set search_path = public as $$
declare
    item jsonb;
    product_row public.products%rowtype;
    v_quantity integer;
    v_key text;
    v_stock integer;
    v_subtotal numeric(10,2) := 0;
    v_shipping numeric(10,2);
    v_tax numeric(10,2);
    v_total numeric(10,2);
    v_order_id uuid;
    v_order_number text;
begin
    if auth.uid() is null then raise exception 'You must sign in before placing an order'; end if;
    if jsonb_typeof(p_items) <> 'array' or jsonb_array_length(p_items) = 0 then raise exception 'Your cart is empty'; end if;
    for item in select value from jsonb_array_elements(p_items) loop
        v_quantity := (item ->> 'quantity')::integer;
        v_key := (item ->> 'color') || '-' || (item ->> 'size');
        select * into product_row from public.products where id = item ->> 'product_id' and is_active = true for update;
        if not found then raise exception 'A product in your cart is unavailable'; end if;
        v_stock := coalesce((product_row.stock ->> v_key)::integer, 0);
        if v_quantity < 1 or v_stock < v_quantity then raise exception 'Not enough stock for %', product_row.name; end if;
        v_subtotal := v_subtotal + (product_row.price * v_quantity);
    end loop;
    v_shipping := case when p_shipping_method = 'express' then 25 when v_subtotal >= 150 then 0 else 15 end;
    v_tax := round(v_subtotal * 0.08, 2);
    v_total := v_subtotal + v_shipping + v_tax;
    insert into public.orders (user_id, shipping_address, shipping_method, subtotal, shipping_total, tax_total, total)
    values (auth.uid(), p_shipping_address, p_shipping_method, v_subtotal, v_shipping, v_tax, v_total)
    returning id, orders.order_number into v_order_id, v_order_number;
    for item in select value from jsonb_array_elements(p_items) loop
        v_quantity := (item ->> 'quantity')::integer;
        v_key := (item ->> 'color') || '-' || (item ->> 'size');
        select * into product_row from public.products where id = item ->> 'product_id' for update;
        v_stock := (product_row.stock ->> v_key)::integer;
        update public.products set stock = jsonb_set(stock, array[v_key], to_jsonb(v_stock - v_quantity), true), updated_at = now() where id = product_row.id;
        insert into public.order_items (order_id, product_id, product_name, color, size, quantity, unit_price)
        values (v_order_id, product_row.id, product_row.name, item ->> 'color', item ->> 'size', v_quantity, product_row.price);
    end loop;
    return query select v_order_id, v_order_number;
end;
$$;
grant execute on function public.create_order(jsonb, jsonb, text) to authenticated;

insert into public.products (id, name, brand, category, price, original_price, image_url, images, colors, sizes, stock, description) values
('SKU-001','Air Max Apex 90','Nike','Athletic',159.99,199.99,'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80','["https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80"]','["Varsity Red","Noir Black","Platinum White"]','[7,8,9,10,11,12]','{"Varsity Red-8":12,"Varsity Red-9":15,"Varsity Red-10":0,"Noir Black-8":4,"Noir Black-9":8,"Noir Black-10":14,"Platinum White-8":9,"Platinum White-9":11,"Platinum White-10":6}','Premium Air cushioning and leather overlays.'),
('SKU-002','Ultraboost Pure 22','Adidas','Running',180.00,null,'https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=800&q=80','["https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=800&q=80"]','["Triple White","Core Black"]','[8,9,10,11]','{"Triple White-8":5,"Triple White-9":3,"Triple White-10":0,"Core Black-8":7,"Core Black-9":10,"Core Black-10":12}','Responsive running shoe.'),
('SKU-003','Cali Suede Classic','Puma','Lifestyle',79.99,89.99,'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?auto=format&fit=crop&w=800&q=80','["https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?auto=format&fit=crop&w=800&q=80"]','["Forest Green","Mustard Yellow"]','[7,8,9,10,11]','{"Forest Green-8":15,"Forest Green-9":18,"Forest Green-10":20,"Mustard Yellow-8":8,"Mustard Yellow-9":5,"Mustard Yellow-10":3}','Heritage streetwear classic.'),
('SKU-004','990v5 Heritage Trainer','New Balance','Lifestyle',199.99,null,'https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=800&q=80','["https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=800&q=80"]','["Castlerock Grey","Tan Suede"]','[8,9,10,11,12]','{"Castlerock Grey-8":4,"Castlerock Grey-9":5,"Castlerock Grey-10":6,"Tan Suede-8":3,"Tan Suede-9":5,"Tan Suede-10":8}','Premium heritage trainer.'),
('SKU-005','Jordan Retro High OG','Nike','Basketball',180.00,null,'https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=800&q=80','["https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=800&q=80"]','["Bred Red","Royal Blue"]','[8,9,10,11,12,13]','{"Bred Red-8":2,"Bred Red-9":5,"Bred Red-10":3,"Bred Red-11":0,"Royal Blue-8":4,"Royal Blue-9":1,"Royal Blue-10":6,"Royal Blue-11":2}','Classic high-top basketball shoe.')
on conflict (id) do nothing;
