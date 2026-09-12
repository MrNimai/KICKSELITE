/* PROGRESS TRAPS, STRIPE-LOOK REALTIME CREDIT CARD */
document.addEventListener('DOMContentLoaded', () => {
    initCheckoutFlow();
});

function initCheckoutFlow() {
    const cart = window.Storage.getCart();
    if (cart.items.length === 0) {
        window.location.href = "cart.html";
        return;
    }

    // Dynamic invoice summary listing panel
    renderOrderSummaryPanel();

    // Visual graphics input listeners
    const cardInput = document.getElementById('cardNum');
    const nameInput = document.getElementById('cardName');
    const expInput = document.getElementById('cardExp');
    const cvvInput = document.getElementById('cardCvv');
    const ccCard = document.querySelector('.credit-card-inner');
    
    if (cardInput) {
        cardInput.addEventListener('input', (e) => {
            let value = e.target.value.replace(/\s+/g, '').replace(/[^0-9]/gi, '');
            let matches = value.match(/\d{4,16}/g);
            let match = matches && matches[0] || '';
            let parts = [];
            
            for (let i = 0, len = match.length; i < len; i += 4) {
                parts.push(match.substring(i, i + 4));
            }
            if (parts.length > 0) {
                e.target.value = parts.join(' ');
            } else {
                e.target.value = value;
            }
            
            document.getElementById('previewCardNum').textContent = e.target.value || "•••• •••• •••• ••••";
        });
    }

    if (nameInput) {
        nameInput.addEventListener('input', (e) => {
            document.getElementById('previewCardName').textContent = e.target.value.toUpperCase() || "CARDHOLDER NAME";
        });
    }

    if (expInput) {
        expInput.addEventListener('input', (e) => {
            let val = e.target.value.replace(/[^0-9]/gi, '');
            if (val.length >= 2) {
                e.target.value = val.substring(0,2) + '/' + val.substring(2,4);
            } else {
                e.target.value = val;
            }
            document.getElementById('previewCardExp').textContent = e.target.value || "MM/YY";
        });
    }

    if (cvvInput && ccCard) {
        cvvInput.addEventListener('focus', () => ccCard.classList.add('flipped'));
        cvvInput.addEventListener('blur', () => ccCard.classList.remove('flipped'));
        cvvInput.addEventListener('input', (e) => {
            document.getElementById('previewCardCvv').textContent = e.target.value || "•••";
        });
    }

    // Multi-Step Layout controllers
    const steps = ['shippingStep', 'paymentStep', 'reviewStep'];
    let currentStepIdx = 0;

    window.nextStep = function(targetIdx) {
        if (targetIdx === 1) {
            // Validate Shipping Form
            if (!validateShippingForm()) {
                window.showToast("Please fill out all required shipping details!", "error");
                return;
            }
        } else if (targetIdx === 2) {
            // Validate Payment Form
            if (!validatePaymentForm()) {
                window.showToast("Please input valid credit card details!", "error");
                return;
            }
            // Populate Step 3 invoice overview details
            populateConfirmationDetails();
        }

        document.getElementById(steps[currentStepIdx]).style.display = "none";
        document.getElementById(steps[targetIdx]).style.display = "block";
        
        // Update Indicator step circles
        document.querySelectorAll('.step-node').forEach((node, idx) => {
            node.classList.remove('active', 'completed');
            if (idx < targetIdx) {
                node.classList.add('completed');
            } else if (idx === targetIdx) {
                node.classList.add('active');
            }
        });

        currentStepIdx = targetIdx;
    };

    window.prevStep = function(targetIdx) {
        document.getElementById(steps[currentStepIdx]).style.display = "none";
        document.getElementById(steps[targetIdx]).style.display = "block";
        
        document.querySelectorAll('.step-node').forEach((node, idx) => {
            node.classList.remove('active', 'completed');
            if (idx < targetIdx) {
                node.classList.add('completed');
            } else if (idx === targetIdx) {
                node.classList.add('active');
            }
        });
        
        currentStepIdx = targetIdx;
    };

    function validateShippingForm() {
        const fields = ['shpFname', 'shpLname', 'shpAddr', 'shpCity', 'shpZip', 'shpEmail', 'shpPhone'];
        let valid = true;
        fields.forEach(f => {
            const input = document.getElementById(f);
            if (input && input.value.trim() === '') {
                input.style.borderColor = "var(--color-error)";
                valid = false;
            } else if (input) {
                input.style.borderColor = "var(--color-border)";
            }
        });
        return valid;
    }

    function validatePaymentForm() {
        const fields = ['cardNum', 'cardName', 'cardExp', 'cardCvv'];
        let valid = true;
        fields.forEach(f => {
            const input = document.getElementById(f);
            if (input && input.value.trim() === '') {
                input.style.borderColor = "var(--color-error)";
                valid = false;
            } else if (input) {
                input.style.borderColor = "var(--color-border)";
            }
        });
        return valid;
    }

    function populateConfirmationDetails() {
        const fname = document.getElementById('shpFname').value;
        const lname = document.getElementById('shpLname').value;
        const addr = document.getElementById('shpAddr').value;
        const city = document.getElementById('shpCity').value;
        const zip = document.getElementById('shpZip').value;
        const country = document.getElementById('shpCountry').value;
        const speed = document.querySelector('input[name="shippingSpeed"]:checked').value;
        
        document.getElementById('revAddressSummary').innerHTML = `
            <strong>${fname} ${lname}</strong><br>
            ${addr}<br>
            ${city}, ${zip}<br>
            ${country}<br>
            <span style="font-size:0.85rem; color:var(--color-muted);">Delivery Speed Option: ${speed === 'standard' ? 'Standard (3-5 days)' : 'Express (1-2 days)'}</span>
        `;
    }

    // Submit order through the protected Supabase database function.
    window.placeOrderSubmit = async function() {
        const overlay = document.getElementById('checkoutLoaderOverlay');
        const statusMsg = document.getElementById('loaderStatusMessage');
        
        if (overlay) overlay.classList.add('active');
        try {
            const user = await window.Auth.getSession();
            if (!user) {
                window.location.href = 'login.html';
                return;
            }
            await new Promise(resolve => setTimeout(resolve, 700));
            if (statusMsg) statusMsg.textContent = "Securing your order...";
            await new Promise(resolve => setTimeout(resolve, 500));
            if (statusMsg) statusMsg.textContent = "Reserving your premium shipment...";
            const shippingAddress = {
                name: `${document.getElementById('shpFname').value.trim()} ${document.getElementById('shpLname').value.trim()}`,
                line1: document.getElementById('shpAddr').value.trim(),
                city: document.getElementById('shpCity').value.trim(),
                state: '',
                zip: document.getElementById('shpZip').value.trim(),
                country: document.getElementById('shpCountry').value,
                phone: document.getElementById('shpPhone').value.trim(),
                email: document.getElementById('shpEmail').value.trim()
            };
            const shippingMethod = document.querySelector('input[name="shippingSpeed"]:checked').value;
            const order = await window.Auth.placeOrder(cart.items, shippingAddress, shippingMethod);
            window.Storage.saveCart({ items: [], coupon: null });
            window.location.href = `success.html?orderId=${order.order_number}`;
        } catch (error) {
            if (overlay) overlay.classList.remove('active');
            window.showToast(error.message || 'We could not place your order.', 'error');
        }
    };

    function renderOrderSummaryPanel() {
        const container = document.getElementById('checkoutSummaryItems');
        if (!container) return;
        
        // Populate elements
        container.innerHTML = cart.items.map(item => {
            const product = window.db.products.find(p => p.id === item.productId);
            if (!product) return '';
            return `
                <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--color-border); padding-bottom: 0.8rem; margin-bottom: 0.8rem;">
                    <div>
                        <strong style="font-size:0.95rem;">${product.name}</strong><br>
                        <span style="font-size:0.8rem; color:var(--color-muted);">Color: ${item.variant.color} | Size: ${item.variant.size} (x${item.quantity})</span>
                    </div>
                    <strong>$${(product.price * item.quantity).toFixed(2)}</strong>
                </div>
            `;
        }).join('');

        let subtotal = 0;
        cart.items.forEach(item => {
            const product = window.db.products.find(p => p.id === item.productId);
            if (product) subtotal += product.price * item.quantity;
        });

        let discount = 0;
        if (cart.coupon) {
            if (cart.coupon.discountType === 'percentage') {
                discount = subtotal * (cart.coupon.value / 100);
            } else if (cart.coupon.discountType === 'fixed') {
                discount = cart.coupon.value;
            }
        }

        let shipping = subtotal > 150 || (cart.coupon && cart.coupon.discountType === 'free_shipping') ? 0 : 15.00;
        const tax = (subtotal - discount) * 0.08;
        const finalTotal = subtotal - discount + shipping + tax;

        document.getElementById('summarySubtotal').textContent = `$${subtotal.toFixed(2)}`;
        document.getElementById('summaryShipping').textContent = shipping === 0 ? "FREE" : `$${shipping.toFixed(2)}`;
        document.getElementById('summaryTax').textContent = `$${tax.toFixed(2)}`;
        document.getElementById('summaryTotal').textContent = `$${finalTotal.toFixed(2)}`;
    }
}
