/* LOCAL STORAGE ACCESS SYSTEM UTILITIES */
window.Storage = {
    getCart() {
        let cart = localStorage.getItem('shoestore_cart');
        return cart ? JSON.parse(cart) : { items: [], coupon: null };
    },
    saveCart(cart) {
        localStorage.setItem('shoestore_cart', JSON.stringify(cart));
        window.dispatchEvent(new Event('cartUpdated'));
    },
    addToCart(productId, variant, qty) {
        let cart = this.getCart();
        let existingIndex = cart.items.findIndex(i => i.productId === productId && 
            i.variant.color === variant.color && i.variant.size === variant.size);
        if (existingIndex > -1) {
            cart.items[existingIndex].quantity += qty;
        } else {
            cart.items.push({ productId, variant, quantity: qty });
        }
        this.saveCart(cart);
    },
    removeFromCart(index) {
        let cart = this.getCart();
        cart.items.splice(index, 1);
        this.saveCart(cart);
    },
    updateCartQty(index, qty) {
        let cart = this.getCart();
        if (qty <= 0) {
            cart.items.splice(index, 1);
        } else {
            cart.items[index].quantity = qty;
        }
        this.saveCart(cart);
    },
    getWishlist() {
        let wishlist = localStorage.getItem('shoestore_wishlist');
        return wishlist ? JSON.parse(wishlist) : [];
    },
    saveWishlist(wishlist) {
        localStorage.setItem('shoestore_wishlist', JSON.stringify(wishlist));
        window.dispatchEvent(new Event('wishlistUpdated'));
    },
    toggleWishlist(productId) {
        let wishlist = this.getWishlist();
        let idx = wishlist.indexOf(productId);
        let added = false;
        if (idx > -1) {
            wishlist.splice(idx, 1);
        } else {
            wishlist.push(productId);
            added = true;
        }
        this.saveWishlist(wishlist);
        return added;
    },
    getCompare() {
        let compare = localStorage.getItem('shoestore_compare');
        return compare ? JSON.parse(compare) : [];
    },
    saveCompare(compare) {
        localStorage.setItem('shoestore_compare', JSON.stringify(compare));
    },
    toggleCompare(productId) {
        let compare = this.getCompare();
        let idx = compare.indexOf(productId);
        let added = false;
        if (idx > -1) {
            compare.splice(idx, 1);
        } else {
            if (compare.length >= 3) {
                return "limit";
            }
            compare.push(productId);
            added = true;
        }
        this.saveCompare(compare);
        return added;
    },
    getOrders() {
        let orders = localStorage.getItem('shoestore_orders');
        return orders ? JSON.parse(orders) : [];
    },
    saveOrder(order) {
        let orders = this.getOrders();
        orders.unshift(order);
        localStorage.setItem('shoestore_orders', JSON.stringify(orders));
    },
    getAddresses() {
        let addr = localStorage.getItem('shoestore_addresses');
        return addr ? JSON.parse(addr) : [];
    },
    saveAddresses(addresses) {
        localStorage.setItem('shoestore_addresses', JSON.stringify(addresses));
    },
    addAddress(address) {
        let addresses = this.getAddresses();
        if (address.isDefault) {
            addresses.forEach(a => a.isDefault = false);
        }
        addresses.push(address);
        this.saveAddresses(addresses);
    },
    deleteAddress(id) {
        let addresses = this.getAddresses();
        addresses = addresses.filter(a => a.id !== id);
        if (addresses.length > 0 && !addresses.some(a => a.isDefault)) {
            addresses[0].isDefault = true;
        }
        this.saveAddresses(addresses);
    }
};
