/* MANAGE PAST ORDERS INVOICES, DYNAMIC SAVED ADDRESS CARDS */
document.addEventListener('DOMContentLoaded', () => {
    initCabinetDashboard();
});

async function initCabinetDashboard() {
    const listContainer = document.getElementById('pastOrdersList');
    const addressContainer = document.getElementById('addressGrid');
    
    let currentUser;
    try {
        currentUser = await window.Auth.getSession();
    } catch (error) {
        window.location.replace('login.html');
        return;
    }
    if (!currentUser) {
        window.location.replace('login.html');
        return;
    }
    
    const userGreets = document.querySelectorAll('.user-greeting-name');
    userGreets.forEach(g => g.textContent = currentUser.name);

    // Profile updates submission
    const profileForm = document.getElementById('profileForm');
    if (profileForm) {
        const pName = document.getElementById('profName');
        const pEmail = document.getElementById('profEmail');
        
        if (pName && pEmail) {
            pName.value = currentUser.name;
            pEmail.value = currentUser.email;
        }

        profileForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            try {
                currentUser = await window.Auth.updateProfile(pName.value.trim(), pEmail.value.trim());
                userGreets.forEach(g => g.textContent = currentUser.name);
                window.showToast("Profile details updated successfully!", "success");
            } catch (error) {
                window.showToast(error.message, "error");
            }
        });
    }

    const passwordForm = document.getElementById('passwordForm');
    if (passwordForm) {
        passwordForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const currentPassword = document.getElementById('currentPassword').value;
            const newPassword = document.getElementById('newPassword').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            if (newPassword !== confirmPassword) return window.showToast('New passwords do not match.', 'error');
            try {
                await window.Auth.updatePassword(currentPassword, newPassword);
                passwordForm.reset();
                window.showToast('Password updated successfully.', 'success');
            } catch (error) {
                window.showToast(error.message, 'error');
            }
        });
    }

    // Toggle Cabinet Views Tab Panes
    window.switchCabinetTab = function(btn, tabId) {
        document.querySelectorAll('.cabinet-nav-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
        
        btn.classList.add('active');
        const pane = document.getElementById(tabId);
        if (pane) pane.classList.add('active');
    };

    // Load list of orders
    let accountOrders = [];
    async function renderOrders() {
        if (!listContainer) return;
        try {
            accountOrders = await window.Auth.getOrders();
        } catch (error) {
            listContainer.innerHTML = `<p style="color:var(--color-error);">${error.message}</p>`;
            return;
        }
        const orders = accountOrders;
        
        if (orders.length === 0) {
            listContainer.innerHTML = `
                <div class="empty-state" style="padding: 2rem 0;">
                    <p style="color:var(--color-muted);">You have not placed any orders yet.</p>
                    <a href="shop.html" class="btn btn-primary" style="margin-top:1rem;">Shop Collection</a>
                </div>
            `;
            return;
        }

        listContainer.innerHTML = orders.map(ord => `
            <div style="border:1px solid var(--color-border); border-radius:var(--radius-md); padding:1.5rem; margin-bottom:1.5rem; background-color:var(--color-card-bg);">
                <div style="display:flex; justify-content:space-between; border-bottom:1px solid var(--color-border); padding-bottom:0.8rem; margin-bottom:1rem; flex-wrap:wrap; gap:1rem;">
                    <div>
                        <strong>ID: #${ord.orderId}</strong><br>
                        <span style="font-size:0.85rem; color:var(--color-muted);">Placed on: ${ord.date}</span>
                    </div>
                    <div style="text-align:right;">
                        <strong>Total Bill: ${ord.total}</strong><br>
                        <span style="font-size:0.85rem; color:var(--color-success); font-weight:700;">Status: ${ord.status}</span>
                    </div>
                </div>
                <div>
                    <span style="font-size:0.9rem; font-weight:700; margin-bottom:0.5rem; display:block;">SHIPMENT CONTENT</span>
                    ${ord.items.map(i => `
                        <div style="font-size:0.9rem; color:var(--color-muted); display:flex; justify-content:space-between; margin-bottom:0.4rem;">
                            <span>${i.name} (${i.color} / Size: ${i.size}) x${i.quantity}</span>
                            <span>${i.price}</span>
                        </div>
                    `).join('')}
                </div>
                <div style="margin-top: 1rem; text-align:right;">
                    <button onclick="triggerInvoicePrint('${ord.orderId}')" class="btn btn-secondary" style="padding: 0.4rem 1rem; font-size:0.8rem;">Print Invoice</button>
                    <a href="tracking.html?orderId=${ord.orderId}" class="btn btn-primary" style="padding: 0.4rem 1rem; font-size:0.8rem; margin-left:0.5rem;">Track Status</a>
                </div>
            </div>
        `).join('');
    }
    renderOrders();

    // Trigger Print formatted printable modal Invoice
    window.triggerInvoicePrint = function(orderId) {
        const order = accountOrders.find(o => o.orderId === orderId);
        if (!order) return;
        
        const printWindow = window.open('', '_blank');
        printWindow.document.write(`
            <html>
                <head>
                    <title>Invoice #${order.orderId}</title>
                    <style>
                        body { font-family: sans-serif; padding: 40px; color: #333; }
                        .header { display: flex; justify-content: space-between; border-bottom: 2px solid #000; padding-bottom: 20px; }
                        .details { margin: 30px 0; line-height: 1.6; }
                        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
                        th { background-color: #f5f5f5; }
                        .totals { text-align: right; margin-top: 30px; font-size: 1.1rem; line-height: 1.8; }
                    </style>
                </head>
                <body onload="window.print()">
                    <div class="header">
                        <h2>KICKSELITE INC.</h2>
                        <div><strong>INVOICE</strong><br>ID: #${order.orderId}</div>
                    </div>
                    <div class="details">
                        <strong>Date:</strong> ${order.date}<br>
                        <strong>Customer Name:</strong> ${order.customerName}<br>
                        <strong>Address:</strong> Verified Address on File
                    </div>
                    <table>
                        <thead>
                            <tr>
                                <th>Item details</th>
                                <th>Unit Cost</th>
                                <th>Quantity</th>
                                <th>Line Subtotal</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${order.items.map(i => `
                                <tr>
                                    <td>${i.name} (${i.color} / Size: ${i.size})</td>
                                    <td>${i.price}</td>
                                    <td>${i.quantity}</td>
                                    <td>$${(parseFloat(i.price.replace('$', '')) * i.quantity).toFixed(2)}</td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                    <div class="totals">
                        Subtotal: ${order.subtotal}<br>
                        Shipping & Handling: ${order.shipping}<br>
                        Estimated State Taxes: ${order.tax}<br>
                        <strong>Grand Total Bill: ${order.total}</strong>
                    </div>
                </body>
            </html>
        `);
        printWindow.document.close();
    };

    // Saved address cards CRUD
    async function renderAddresses() {
        if (!addressContainer) return;
        let list;
        try {
            list = await window.Auth.getAddresses();
        } catch (error) {
            addressContainer.innerHTML = `<p style="color:var(--color-error);">${error.message}</p>`;
            return;
        }
        
        addressContainer.innerHTML = list.map(addr => `
            <div style="border:1px solid var(--color-border); border-radius:var(--radius-md); padding:1.5rem; position:relative; background-color:var(--color-card-bg);">
                ${addr.isDefault ? `<span style="position:absolute; top:1rem; right:1rem; background-color:var(--color-success); color:white; font-size:0.7rem; padding:0.2rem 0.6rem; border-radius:var(--radius-sm); font-weight:700;">DEFAULT</span>` : ''}
                <strong style="display:block; margin-bottom:0.5rem; font-size:1.1rem;">${addr.name}</strong>
                <p style="color:var(--color-muted); font-size:0.9rem; line-height:1.5;">
                    ${addr.line1}<br>
                    ${addr.city}, ${addr.state} ${addr.zip}<br>
                    ${addr.country}<br>
                    Phone: ${addr.phone}
                </p>
                <div style="margin-top:1rem; display:flex; gap:0.5rem;">
                    <button onclick="deleteAddressBtn('${addr.id}')" style="color:var(--color-error); font-size:0.8rem; font-weight:600;">Delete Address</button>
                </div>
            </div>
        `).join('');
    }
    renderAddresses();

    // Toggle Modal form for adding Address
    const modal = document.getElementById('addressModal');
    const form = document.getElementById('addressForm');

    window.toggleAddressModal = function() {
        if (modal) modal.classList.toggle('active');
    };

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('adrName').value.trim();
            const line1 = document.getElementById('adrLine1').value.trim();
            const city = document.getElementById('adrCity').value.trim();
            const state = document.getElementById('adrState').value.trim();
            const zip = document.getElementById('adrZip').value.trim();
            const phone = document.getElementById('adrPhone').value.trim();
            const def = document.getElementById('adrDefault').checked;
            
            if (!name || !line1 || !city || !state || !zip) {
                window.showToast("All mandatory fields are required!", "error");
                return;
            }
            
            const newAddr = {
                name, line1, city, state, zip, phone,
                country: "United States",
                isDefault: def
            };
            try {
                await window.Auth.addAddress(newAddr);
                window.showToast("New address added successfully!", "success");
                form.reset();
                toggleAddressModal();
                renderAddresses();
            } catch (error) {
                window.showToast(error.message, 'error');
            }
        });
    }

    window.deleteAddressBtn = async function(id) {
        try {
            await window.Auth.deleteAddress(id);
            window.showToast("Address deleted.", "info");
            renderAddresses();
        } catch (error) {
            window.showToast(error.message, 'error');
        }
    };

    window.logoutSession = async function() {
        try { await window.Auth.logout(); } catch (error) { window.showToast(error.message, 'error'); return; }
        window.location.href = "index.html";
    };
}
