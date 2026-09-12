/* CALCULATE DISCOUNTS, UPDATE QUANTITIES, CART CRUD */
document.addEventListener('DOMContentLoaded', () => {
    initCartPage();
});

function initCartPage() {
    const tableBody = document.getElementById('cartTableBody');
    if (!tableBody) return;
    
    // Coupon form logic
    const couponForm = document.getElementById('couponForm');
    const couponInput = document.getElementById('couponCode');
    
    if (couponForm) {
        couponForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const code = couponInput.value.trim().toUpperCase();
            const promo = window.db.coupons.find(c => c.code === code);
            
            if (promo) {
                let cart = window.Storage.getCart();
                cart.coupon = promo;
                window.Storage.saveCart(cart);
                window.showToast(`Promo Applied! Coupon discount enabled.`, "success");
                renderCart();
            } else {
                window.showToast("Invalid Coupon Code!", "error");
            }
        });
    }

    window.removeCouponBtn = function() {
        let cart = window.Storage.getCart();
        cart.coupon = null;
        window.Storage.saveCart(cart);
        window.showToast("Coupon removed.", "info");
        renderCart();
    };

    window.updateQty = function(index, amount) {
        let cart = window.Storage.getCart();
        const item = cart.items[index];
        const product = window.db.products.find(p => p.id === item.productId);
        const stockKey = `${item.variant.color}-${item.variant.size}`;
        const stockLeft = product.stock[stockKey] !== undefined ? product.stock[stockKey] : 10;
        
        let target = item.quantity + amount;
        if (target > stockLeft) {
            window.showToast("Cannot exceed available stock!", "error");
            return;
        }
        window.Storage.updateCartQty(index, target);
        renderCart();
    };

    window.removeItem = function(index) {
        const row = document.getElementById(`cartRow_${index}`);
        if (row) {
            row.style.transform = "translateX(100px)";
            row.style.opacity = "0";
            setTimeout(() => {
                window.Storage.removeFromCart(index);
                renderCart();
            }, 300);
        }
    };

    function renderCart() {
        const cart = window.Storage.getCart();
        
        if (cart.items.length === 0) {
            const cartWrap = document.getElementById('cartPageLayout');
            if (cartWrap) {
                cartWrap.innerHTML = `
                    <div class="empty-state" style="grid-column: span 2;">
                        <svg viewBox="0 0 24 24" width="80" height="80" stroke="currentColor" stroke-width="1" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                        <h2 style="margin-bottom: 1rem;">Your Cart is Empty</h2>
                        <p style="color:var(--color-muted); margin-bottom: 2rem;">Looks like you haven't added anything to your cart yet.</p>
                        <a href="shop.html" class="btn btn-primary">Start Shopping</a>
                    </div>
                `;
            }
            return;
        }

        tableBody.innerHTML = cart.items.map((item, index) => {
            const product = window.db.products.find(p => p.id === item.productId);
            if (!product) return '';
            const subtotal = product.price * item.quantity;
            return `
                <tr class="cart-item-row" id="cartRow_${index}" style="transition: var(--transition);">
                    <td class="cart-product-cell">
                        <img src="${product.images[0]}" alt="${product.name}" class="cart-prod-img">
                        <div>
                            <span class="cart-prod-name"><a href="product.html?id=${product.id}">${product.name}</a></span>
                            <div class="cart-prod-meta">Variant: ${item.variant.color} | Size: ${item.variant.size}</div>
                        </div>
                    </td>
                    <td>$${product.price.toFixed(2)}</td>
                    <td>
                        <div class="qty-widget" style="margin: 0;">
                            <button class="qty-btn" onclick="updateQty(${index}, -1)">-</button>
                            <input class="qty-input" type="text" value="${item.quantity}" readonly>
                            <button class="qty-btn" onclick="updateQty(${index}, 1)">+</button>
                        </div>
                    </td>
                    <td>$${subtotal.toFixed(2)}</td>
                    <td style="text-align: right;">
                        <button onclick="removeItem(${index})" aria-label="Remove item" style="color:var(--color-error); font-size:1.2rem;">&times;</button>
                    </td>
                </tr>
            `;
        }).join('');

        // Recalculate Subtotal / Promo / Totals
        let subtotal = 0;
        cart.items.forEach(item => {
            const product = window.db.products.find(p => p.id === item.productId);
            if (product) subtotal += product.price * item.quantity;
        });

        let discount = 0;
        let discountRowHTML = '';
        if (cart.coupon) {
            if (cart.coupon.discountType === 'percentage') {
                discount = subtotal * (cart.coupon.value / 100);
            } else if (cart.coupon.discountType === 'fixed') {
                discount = cart.coupon.value;
            }
            discountRowHTML = `
                <div class="summary-row" style="color:var(--color-success); font-weight:600;">
                    <span>Discount (${cart.coupon.code})</span>
                    <span>-$${discount.toFixed(2)} <button onclick="removeCouponBtn();" style="color:var(--color-error); margin-left:5px;">&times;</button></span>
                </div>
            `;
        }

        // Flat Rate Shipping Calculation
        let shipping = subtotal > 150 || (cart.coupon && cart.coupon.discountType === 'free_shipping') ? 0 : 15.00;
        const tax = (subtotal - discount) * 0.08;
        const finalTotal = subtotal - discount + shipping + tax;

        document.getElementById('summarySubtotal').textContent = `$${subtotal.toFixed(2)}`;
        document.getElementById('summaryShipping').textContent = shipping === 0 ? "FREE" : `$${shipping.toFixed(2)}`;
        document.getElementById('summaryTax').textContent = `$${tax.toFixed(2)}`;
        document.getElementById('summaryTotal').textContent = `$${finalTotal.toFixed(2)}`;
        
        const discContainer = document.getElementById('summaryDiscountRow');
        if (discContainer) discContainer.innerHTML = discountRowHTML;
    }
    renderCart();
}