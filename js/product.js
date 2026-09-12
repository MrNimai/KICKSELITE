/* ZOOM EFFECT, VARIANTS SWAP, DYNAMIC REVIEW BOARD */
document.addEventListener('DOMContentLoaded', () => {
    initProductDetail();
});

function initProductDetail() {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id') || "SKU-001";
    
    const product = window.db.products.find(p => p.id === id) || window.db.products[0];
    
    // Render static properties
    document.title = `${product.name} | KicksElite`;
    
    const brand = document.getElementById('prodBrand');
    const title = document.getElementById('prodTitle');
    const price = document.getElementById('prodPrice');
    const desc = document.getElementById('prodDesc');
    const mainImg = document.getElementById('mainImg');
    const thumbContainer = document.getElementById('thumbnailsList');
    
    if (brand) brand.textContent = product.brand;
    if (title) title.textContent = product.name;
    if (desc) desc.textContent = product.description;
    if (price) {
        price.innerHTML = `$${product.price.toFixed(2)} ${product.originalPrice ? `<span class="card-price-old" style="margin-left:1rem; font-size:1.3rem;">$${product.originalPrice.toFixed(2)}</span>` : ''}`;
    }
    
    // Breadcrumb updates
    const breadcrumb = document.getElementById('breadcrumbCategory');
    if (breadcrumb) {
        breadcrumb.textContent = product.category;
        breadcrumb.href = `shop.html?category=${product.category}`;
    }
    const breadcrumbName = document.getElementById('breadcrumbName');
    if (breadcrumbName) breadcrumbName.textContent = product.name;

    // Load Image Gallery thumbnails
    if (mainImg) mainImg.src = product.images[0];
    if (thumbContainer) {
        thumbContainer.innerHTML = product.images.map((img, idx) => `
            <div class="thumbnail-pane ${idx === 0 ? 'active' : ''}" onclick="swapMainImage(this, '${img}')">
                <img src="${img}" alt="${product.name} shadow">
            </div>
        `).join('');
    }

    // Dynamic zoom execution
    const zoomContainer = document.querySelector('.main-view-container');
    if (zoomContainer && mainImg) {
        zoomContainer.addEventListener('mousemove', (e) => {
            const x = e.clientX - zoomContainer.offsetLeft;
            const y = e.clientY - zoomContainer.offsetTop;
            
            const originX = (x / zoomContainer.offsetWidth) * 100;
            const originY = (y / zoomContainer.offsetHeight) * 100;
            
            mainImg.style.transformOrigin = `${originX}% ${originY}%`;
            mainImg.style.transform = "scale(1.8)";
        });
        
        zoomContainer.addEventListener('mouseleave', () => {
            mainImg.style.transform = "scale(1)";
        });
    }

    // Render option variables
    const colorsWrapper = document.getElementById('colorsWrapper');
    const sizesWrapper = document.getElementById('sizesWrapper');
    
    if (colorsWrapper) {
        colorsWrapper.innerHTML = product.colors.map((c, idx) => `
            <button class="btn btn-secondary color-swatch-option ${idx === 0 ? 'active' : ''}" onclick="selectColorSwatch(this, '${c}')" style="padding: 0.5rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--color-border);">${c}</button>
        `).join('');
    }
    
    if (sizesWrapper) {
        sizesWrapper.innerHTML = product.sizes.map((s, idx) => `
            <button class="size-btn ${idx === 0 ? 'active' : ''}" onclick="selectSizeButton(this, ${s})">${s}</button>
        `).join('');
    }

    // Specs table load
    const specsBody = document.getElementById('specsBody');
    if (specsBody) {
        specsBody.innerHTML = Object.entries(product.specs).map(([key, value]) => `
            <tr>
                <td>${key}</td>
                <td>${value}</td>
            </tr>
        `).join('');
    }

    // Initialize interactive actions
    let activeColor = product.colors[0];
    let activeSize = product.sizes[0];
    let activeQty = 1;

    window.swapMainImage = function(pane, src) {
        document.querySelectorAll('.thumbnail-pane').forEach(p => p.classList.remove('active'));
        pane.classList.add('active');
        if (mainImg) mainImg.src = src;
    };

    window.selectColorSwatch = function(btn, color) {
        document.querySelectorAll('.color-swatch-option').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeColor = color;
        checkOptionStock();
    };

    window.selectSizeButton = function(btn, size) {
        document.querySelectorAll('.size-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeSize = size;
        checkOptionStock();
    };

    // Quantity selectors
    const qtyInput = document.getElementById('qtyValue');
    const qtyMinus = document.getElementById('qtyMinus');
    const qtyPlus = document.getElementById('qtyPlus');

    if (qtyMinus && qtyPlus && qtyInput) {
        qtyMinus.addEventListener('click', () => {
            if (activeQty > 1) {
                activeQty--;
                qtyInput.value = activeQty;
            }
        });
        qtyPlus.addEventListener('click', () => {
            const stockKey = `${activeColor}-${activeSize}`;
            const max = product.stock[stockKey] !== undefined ? product.stock[stockKey] : 10;
            if (activeQty < max) {
                activeQty++;
                qtyInput.value = activeQty;
            } else {
                window.showToast("Cannot exceed maximum available stock!", "error");
            }
        });
    }

    function checkOptionStock() {
        const stockKey = `${activeColor}-${activeSize}`;
        const stockLeft = product.stock[stockKey];
        const statusLabel = document.getElementById('stockStatusLabel');
        const addToCartBtn = document.getElementById('addToCartBtn');
        
        if (statusLabel) {
            if (stockLeft === 0) {
                statusLabel.textContent = "Out Of Stock";
                statusLabel.style.color = "var(--color-error)";
                if (addToCartBtn) addToCartBtn.disabled = true;
            } else if (stockLeft <= 5) {
                statusLabel.textContent = `Low Stock - Only ${stockLeft} pairs left!`;
                statusLabel.style.color = "var(--color-secondary)";
                if (addToCartBtn) addToCartBtn.disabled = false;
            } else {
                statusLabel.textContent = "In Stock";
                statusLabel.style.color = "var(--color-success)";
                if (addToCartBtn) addToCartBtn.disabled = false;
            }
        }
    }
    checkOptionStock();

    // Add To Cart Submit Action
    const addToCartBtn = document.getElementById('addToCartBtn');
    if (addToCartBtn) {
        addToCartBtn.addEventListener('click', () => {
            window.Storage.addToCart(product.id, { color: activeColor, size: activeSize }, activeQty);
            window.showToast(`Success! ${activeQty} pair(s) added to Cart.`, "success");
        });
    }

    // Toggle Wishlist Action
    const addToWishlistBtn = document.getElementById('addToWishlistBtn');
    if (addToWishlistBtn) {
        addToWishlistBtn.addEventListener('click', () => {
            const added = window.Storage.toggleWishlist(product.id);
            window.showToast(added ? "Saved to Wishlist!" : "Removed from Wishlist!", "success");
        });
    }

    // Render Related Products
    const relatedGrid = document.getElementById('relatedGrid');
    if (relatedGrid) {
        const related = window.db.products.filter(p => p.category === product.category && p.id !== product.id).slice(0, 4);
        relatedGrid.innerHTML = related.map(p => `
            <article class="product-card">
                <div class="card-img-wrapper">
                    <img src="${p.images[0]}" alt="${p.name}">
                    <div class="card-actions">
                        <a href="product.html?id=${p.id}" class="card-btn" aria-label="View Details"><svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></a>
                    </div>
                </div>
                <div class="card-info">
                    <span class="card-brand">${p.brand}</span>
                    <h3 class="card-title"><a href="product.html?id=${p.id}">${p.name}</a></h3>
                    <div class="card-price-row">
                        <span class="card-price">$${p.price.toFixed(2)}</span>
                    </div>
                </div>
            </article>
        `).join('');
    }

    // Load Tab Pane Switches
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));
            
            btn.classList.add('active');
            const target = document.getElementById(btn.dataset.tab);
            if (target) target.classList.add('active');
        });
    });

    // Render Review list
    initReviewSystem(product);
}

function initReviewSystem(product) {
    const totalReviewsText = document.getElementById('totalReviewsText');
    const averageRatingText = document.getElementById('averageRatingText');
    const reviewsList = document.getElementById('reviewsList');
    const reviewForm = document.getElementById('reviewForm');
    
    // Pull any custom review saved in localStorage overrides
    const key = `shoestore_reviews_${product.id}`;
    let customReviews = JSON.parse(localStorage.getItem(key)) || [];
    let allReviews = [...product.reviews, ...customReviews];
    
    function renderReviews() {
        if (totalReviewsText) totalReviewsText.textContent = `${allReviews.length} Customer Reviews`;
        
        const avg = allReviews.reduce((sum, r) => sum + r.rating, 0) / allReviews.length;
        if (averageRatingText) averageRatingText.textContent = avg.toFixed(1);
        
        // Stars distribution summary calculation
        const distribution = { 5:0, 4:0, 3:0, 2:0, 1:0 };
        allReviews.forEach(r => { distribution[r.rating]++; });
        
        for (let star = 5; star >= 1; star--) {
            const bar = document.getElementById(`distBar${star}`);
            if (bar) {
                const percent = allReviews.length > 0 ? (distribution[star] / allReviews.length) * 100 : 0;
                bar.style.width = `${percent}%`;
            }
        }
        
        if (reviewsList) {
            reviewsList.innerHTML = allReviews.map(r => `
                <div style="border-bottom: 1px solid var(--color-border); padding-bottom: 1.5rem; margin-bottom: 1.5rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom: 0.5rem;">
                        <strong>${r.user}</strong>
                        <span style="font-size:0.85rem; color:var(--color-muted);">${r.date}</span>
                    </div>
                    <div style="color:var(--color-gold); margin-bottom:0.5rem;">${'★'.repeat(r.rating) + '☆'.repeat(5-r.rating)}</div>
                    <p style="color:var(--color-muted);">${r.comment}</p>
                </div>
            `).join('');
        }
    }
    renderReviews();

    if (reviewForm) {
        reviewForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('revName').value.trim();
            const comment = document.getElementById('revComment').value.trim();
            const rating = parseInt(document.getElementById('revRating').value);
            
            if (name === '' || comment === '') {
                window.showToast("All fields are required!", "error");
                return;
            }
            
            const newRev = {
                user: name,
                rating: rating,
                date: new Date().toISOString().split('T')[0],
                comment: comment
            };
            
            customReviews.unshift(newRev);
            localStorage.setItem(key, JSON.stringify(customReviews));
            allReviews.unshift(newRev);
            
            // Success responses
            window.showToast("Thank you! Review added successfully.", "success");
            reviewForm.reset();
            renderReviews();
        });
    }
}