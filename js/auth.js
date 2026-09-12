/* Supabase Auth client for static hosting and Live Server. */
window.Auth = (() => {
    const config = window.SUPABASE_CONFIG;
    const client = config && window.supabase && window.supabase.createClient(
        config.url,
        config.publishableKey,
        { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true } }
    );

    const publicUser = user => user ? {
        id: user.id,
        name: user.user_metadata?.full_name || user.email?.split('@')[0] || 'Member',
        email: user.email
    } : null;

    const requireClient = () => {
        if (!client) throw new Error('Authentication is not configured. Refresh the page and try again.');
        return client;
    };

    const auth = {
        user: null,
        async getSession() {
            const supabase = requireClient();
            const { data: { session } } = await supabase.auth.getSession();
            if (!session) return null;
            const { data, error } = await supabase.auth.getUser();
            if (error) throw error;
            this.user = publicUser(data.user);
            window.dispatchEvent(new Event('authUpdated'));
            return this.user;
        },
        async signup(name, email, password) {
            const supabase = requireClient();
            const { data, error } = await supabase.auth.signUp({
                email,
                password,
                options: {
                    data: { full_name: name },
                    emailRedirectTo: `${window.location.origin}/login.html`
                }
            });
            if (error) throw error;
            this.user = publicUser(data.user);
            window.dispatchEvent(new Event('authUpdated'));
            return { user: this.user, needsEmailConfirmation: !data.session };
        },
        async login(email, password) {
            const supabase = requireClient();
            const { data, error } = await supabase.auth.signInWithPassword({ email, password });
            if (error) throw error;
            this.user = publicUser(data.user);
            window.dispatchEvent(new Event('authUpdated'));
            return this.user;
        },
        async updateProfile(name, email) {
            const supabase = requireClient();
            const attributes = { data: { full_name: name } };
            if (email !== this.user?.email) attributes.email = email;
            const { data, error } = await supabase.auth.updateUser(attributes);
            if (error) throw error;
            this.user = publicUser(data.user);
            window.dispatchEvent(new Event('authUpdated'));
            return this.user;
        },
        async updatePassword(currentPassword, newPassword) {
            const supabase = requireClient();
            if (!this.user?.email) throw new Error('Please sign in again.');
            const { error: signInError } = await supabase.auth.signInWithPassword({ email: this.user.email, password: currentPassword });
            if (signInError) throw new Error('Current password is incorrect.');
            const { error } = await supabase.auth.updateUser({ password: newPassword });
            if (error) throw error;
        },
        async getOrders() {
            const { data, error } = await requireClient().from('orders')
                .select('order_number, status, subtotal, shipping_total, tax_total, total, shipping_address, created_at, order_items(product_name, color, size, quantity, unit_price)')
                .order('created_at', { ascending: false });
            if (error) throw error;
            return data.map(order => ({
                orderId: order.order_number,
                date: new Date(order.created_at).toLocaleDateString(),
                customerName: order.shipping_address.name,
                subtotal: `$${Number(order.subtotal).toFixed(2)}`,
                shipping: Number(order.shipping_total) === 0 ? 'FREE' : `$${Number(order.shipping_total).toFixed(2)}`,
                tax: `$${Number(order.tax_total).toFixed(2)}`,
                total: `$${Number(order.total).toFixed(2)}`,
                status: order.status,
                items: order.order_items.map(item => ({ name: item.product_name, color: item.color, size: item.size, quantity: item.quantity, price: `$${Number(item.unit_price).toFixed(2)}` }))
            }));
        },
        async placeOrder(items, shippingAddress, shippingMethod) {
            const { data, error } = await requireClient().rpc('create_order', {
                p_items: items.map(item => ({ product_id: item.productId, color: item.variant.color, size: String(item.variant.size), quantity: item.quantity })),
                p_shipping_address: shippingAddress,
                p_shipping_method: shippingMethod
            });
            if (error) throw error;
            return data[0];
        },
        async getAddresses() {
            const { data, error } = await requireClient().from('addresses').select('*').order('is_default', { ascending: false }).order('created_at', { ascending: false });
            if (error) throw error;
            return data.map(address => ({
                id: address.id,
                name: address.name,
                line1: address.line1,
                city: address.city,
                state: address.state,
                zip: address.zip,
                country: address.country,
                phone: address.phone,
                isDefault: address.is_default
            }));
        },
        async addAddress(address) {
            const supabase = requireClient();
            if (address.isDefault) {
                const { error: updateError } = await supabase.from('addresses').update({ is_default: false }).eq('user_id', this.user.id);
                if (updateError) throw updateError;
            }
            const { error } = await supabase.from('addresses').insert({ user_id: this.user.id, name: address.name, line1: address.line1, city: address.city, state: address.state, zip: address.zip, country: address.country, phone: address.phone, is_default: address.isDefault });
            if (error) throw error;
        },
        async deleteAddress(id) {
            const { error } = await requireClient().from('addresses').delete().eq('id', id);
            if (error) throw error;
        },
        async logout() {
            const { error } = await requireClient().auth.signOut();
            if (error) throw error;
            this.user = null;
            window.dispatchEvent(new Event('authUpdated'));
        }
    };
    return auth;
})();
