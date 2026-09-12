/* GLOBAL DOM MANIPULATIONS AND REGISTRATIONS */
document.addEventListener('DOMContentLoaded', () => {
    initStickyHeader();
    initMobileMenu();
    initSearchOverlay();
    initDarkMode();
    updateBadges();
    initBackToTop();
    initNewsletterForm();
    
    window.addEventListener('cartUpdated', updateBadges);
    window.addEventListener('wishlistUpdated', updateBadges);
});

function initStickyHeader() {
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                header.classList.add('sticky');
            } else {
                header.classList.remove('sticky');
            }
        });
    }
}

function initMobileMenu() {
    const hamburger = document.querySelector('.hamburger');
    const drawer = document.querySelector('.mobile-drawer');
    const drawerClose = document.querySelector('.drawer-close');
    const overlay = document.querySelector('.drawer-overlay');
    
    if (hamburger && drawer) {
        hamburger.addEventListener('click', () => {
            drawer.classList.add('active');
            if (overlay) overlay.classList.add('active');
        });
    }
    
    if (drawerClose && drawer) {
        drawerClose.addEventListener('click', () => {
            drawer.classList.remove('active');
            if (overlay) overlay.classList.remove('active');
        });
    }
    
    if (overlay && drawer) {
        overlay.addEventListener('click', () => {
            drawer.classList.remove('active');
            overlay.classList.remove('active');
        });
    }
}

function initSearchOverlay() {
    const searchTrigger = document.querySelector('.search-trigger');
    const searchOverlay = document.querySelector('.search-overlay');
    const searchClose = document.querySelector('.search-close');
    const searchInput = document.querySelector('.search-input');
    const suggestionsList = document.querySelector('.search-suggestions');
    
    if (!searchOverlay) return;
    searchOverlay.setAttribute('aria-hidden', 'true');

    const closeSearch = () => {
        searchOverlay.classList.remove('active');
        searchOverlay.setAttribute('aria-hidden', 'true');
        if (searchInput) searchInput.value = '';
        if (suggestionsList) suggestionsList.innerHTML = '';
        if (searchTrigger) searchTrigger.focus();
    };

    if (searchTrigger) {
        searchTrigger.addEventListener('click', (e) => {
            e.preventDefault();
            searchOverlay.classList.add('active');
            searchOverlay.setAttribute('aria-hidden', 'false');
            setTimeout(() => searchInput && searchInput.focus(), 150);
        });
    }
    
    if (searchClose) {
        searchClose.addEventListener('click', closeSearch);
    }

    searchOverlay.addEventListener('click', (event) => {
        if (event.target === searchOverlay) closeSearch();
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && searchOverlay.classList.contains('active')) closeSearch();
    });
    
    if (searchInput) {
        let timeout = null;
        searchInput.addEventListener('input', () => {
            clearTimeout(timeout);
            timeout = setTimeout(() => {
                const query = searchInput.value.trim().toLowerCase();
                if (query.length < 2) {
                    suggestionsList.innerHTML = '';
                    return;
                }
                
                const matches = window.db.products.filter(p => 
                    p.name.toLowerCase().includes(query) || 
                    p.brand.toLowerCase().includes(query) ||
                    p.category.toLowerCase().includes(query) ||
                    p.tags.some(t => t.toLowerCase().includes(query))
                ).slice(0, 5);
                
                suggestionsList.innerHTML = '';
                if (matches.length === 0) {
                    const li = document.createElement('li');
                    li.className = 'no-suggest';
                    li.textContent = 'No products found.';
                    suggestionsList.appendChild(li);
                } else {
                    matches.forEach(p => {
                        const li = document.createElement('li');
                        li.innerHTML = `
                            <a href="product.html?id=${p.id}" class="suggest-item">
                                <img src="${p.images[0]}" alt="${p.name}">
                                <div class="suggest-info">
                                    <span class="suggest-title">${p.name}</span>
                                    <span class="suggest-brand">${p.brand}</span>
                                </div>
                                <span class="suggest-price">$${p.price.toFixed(2)}</span>
                            </a>
                        `;
                        suggestionsList.appendChild(li);
                    });
                }
            }, 250);
        });
    }
}

function initDarkMode() {
    const toggle = document.querySelector('.dark-mode-toggle');
    const saved = localStorage.getItem('shoestore_darkmode');
    
    const isDark = saved === 'true' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches);
    if (isDark) {
        document.body.classList.add('dark-mode');
        if (toggle) toggle.checked = true;
    }
    
    if (toggle) {
        toggle.checked = isDark;
        toggle.addEventListener('change', () => {
            if (toggle.checked) {
                document.body.classList.add('dark-mode');
                localStorage.setItem('shoestore_darkmode', 'true');
            } else {
                document.body.classList.remove('dark-mode');
                localStorage.setItem('shoestore_darkmode', 'false');
            }
        });
    }
}

function updateBadges() {
    const cartBadge = document.querySelector('.cart-badge');
    const wishlistBadge = document.querySelector('.wishlist-badge');
    
    const cart = window.Storage.getCart();
    const wishlist = window.Storage.getWishlist();
    
    const cartCount = cart.items.reduce((sum, item) => sum + item.quantity, 0);
    const wishlistCount = wishlist.length;
    
    if (cartBadge) {
        cartBadge.textContent = cartCount;
        cartBadge.style.display = cartCount > 0 ? 'flex' : 'none';
    }
    if (wishlistBadge) {
        wishlistBadge.textContent = wishlistCount;
        wishlistBadge.style.display = wishlistCount > 0 ? 'flex' : 'none';
    }
}

function initBackToTop() {
    const btt = document.createElement('button');
    btt.className = 'back-to-top';
    btt.setAttribute('aria-label', 'Back to top');
    btt.innerHTML = `<svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>`;
    document.body.appendChild(btt);
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            btt.classList.add('visible');
        } else {
            btt.classList.remove('visible');
        }
    });
    
    btt.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

function initNewsletterForm() {
    const forms = document.querySelectorAll('.newsletter-form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const input = form.querySelector('input');
            if (input && input.value.trim() !== '') {
                window.showToast("Subscription successful! Welcome to KicksElite.", "success");
                input.value = '';
            }
        });
    });
}

window.showToast = function(message, type = 'success') {
    let container = document.querySelector('.toast-container');
    if (!container) {
        container = document.createElement('div');
        container.className = 'toast-container';
        document.body.appendChild(container);
    }
    
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <span>${message}</span>
        <button class="toast-close" aria-label="Close Toast">&times;</button>
    `;
    container.appendChild(toast);
    
    setTimeout(() => toast.classList.add('visible'), 10);
    
    const timer = setTimeout(() => {
        toast.classList.remove('visible');
        setTimeout(() => toast.remove(), 300);
    }, 3500);
    
    toast.querySelector('.toast-close').addEventListener('click', () => {
        clearTimeout(timer);
        toast.classList.remove('visible');
        setTimeout(() => toast.remove(), 300);
    });
};



/* MULTIFACETED LIVE SHOP FILTER SYSTEM */
document.addEventListener('DOMContentLoaded', () => {
    initCatalogFilters();
});

function initCatalogFilters() {
    const grid = document.getElementById('catalogGrid');
    if (!grid) return;
    
    const brandCheckboxes = document.querySelectorAll('.brand-filter');
    const catCheckboxes = document.querySelectorAll('.category-filter');
    const sizeCheckboxes = document.querySelectorAll('.size-filter');
    const priceSlider = document.getElementById('priceRange');
    const priceOutput = document.getElementById('priceValue');
    const sortSelect = document.getElementById('sortSelect');
    const colorSwatches = document.querySelectorAll('.swatch-color');
    const ratingRadio = document.querySelectorAll('.rating-filter');
    
    let activeColor = null;
    let activeRating = null;
    
    // Listen to Preset Category from URL Queries
    const urlParams = new URLSearchParams(window.location.search);
    const catParam = urlParams.get('category');
    if (catParam) {
        catCheckboxes.forEach(cb => {
            if (cb.value.toLowerCase() === catParam.toLowerCase()) {
                cb.checked = true;
            }
        });
    }

    // Swatches listeners
    colorSwatches.forEach(swatch => {
        swatch.addEventListener('click', () => {
            if (swatch.classList.contains('active')) {
                swatch.classList.remove('active');
                activeColor = null;
            } else {
                colorSwatches.forEach(s => s.classList.remove('active'));
                swatch.classList.add('active');
                activeColor = swatch.dataset.color;
            }
            renderFilteredProducts();
        });
    });

    // Rating listener
    ratingRadio.forEach(radio => {
        radio.addEventListener('change', () => {
            activeRating = parseFloat(radio.value);
            renderFilteredProducts();
        });
    });

    // Event listeners registration
    [...brandCheckboxes, ...catCheckboxes, ...sizeCheckboxes].forEach(cb => {
        cb.addEventListener('change', renderFilteredProducts);
    });

    if (priceSlider) {
        priceSlider.addEventListener('input', () => {
            if (priceOutput) priceOutput.textContent = `$${priceSlider.value}`;
            renderFilteredProducts();
        });
    }

    if (sortSelect) {
        sortSelect.addEventListener('change', renderFilteredProducts);
    }

    // Initial render call
    renderFilteredProducts();

    function renderFilteredProducts() {
        // Show pulse skeletons
        grid.innerHTML = Array(4).fill(0).map(() => `
            <div style="height: 380px;" class="skeleton-box"></div>
        `).join('');

        setTimeout(() => {
            let products = [...window.db.products];

            // 1. Brand filtering
            const activeBrands = Array.from(brandCheckboxes).filter(c => c.checked).map(c => c.value);
            if (activeBrands.length > 0) {
                products = products.filter(p => activeBrands.includes(p.brand));
            }

            // 2. Category filtering
            const activeCats = Array.from(catCheckboxes).filter(c => c.checked).map(c => c.value);
            if (activeCats.length > 0) {
                products = products.filter(p => activeCats.includes(p.category));
            }

            // 3. Sizes filtering
            const activeSizes = Array.from(sizeCheckboxes).filter(c => c.checked).map(c => parseInt(c.value));
            if (activeSizes.length > 0) {
                products = products.filter(p => p.sizes.some(s => activeSizes.includes(s)));
            }

            // 4. Color Swatches filtering
            if (activeColor) {
                products = products.filter(p => p.colors.some(c => c.toLowerCase().includes(activeColor.toLowerCase())));
            }

            // 5. Rating filtering
            if (activeRating) {
                products = products.filter(p => p.rating >= activeRating);
            }

            // 6. Price Slider filtering
            if (priceSlider) {
                const maxPrice = parseFloat(priceSlider.value);
                products = products.filter(p => p.price <= maxPrice);
            }

            // 7. Sorting
            if (sortSelect) {
                const sortVal = sortSelect.value;
                if (sortVal === 'price-asc') {
                    products.sort((a,b) => a.price - b.price);
                } else if (sortVal === 'price-desc') {
                    products.sort((a,b) => b.price - a.price);
                } else if (sortVal === 'rating') {
                    products.sort((a,b) => b.rating - a.rating);
                }
            }

            // Output Dynamic Results
            if (products.length === 0) {
                grid.innerHTML = `
                    <div class="empty-state form-full" style="grid-column: span 3;">
                        <svg viewBox="0 0 24 24" width="60" height="60" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="8" y1="12" x2="16" y2="12"></line></svg>
                        <p style="color: var(--color-muted);">No sneakers match your filters.</p>
                        <button onclick="resetAllFilters();" class="btn btn-primary" style="margin-top: 1.5rem;">Reset Filters</button>
                    </div>
                `;
                return;
            }

            // Fetch state lists
            const wl = window.Storage.getWishlist();
            const cmp = window.Storage.getCompare();

            grid.innerHTML = products.map(p => {
                const isSaved = wl.includes(p.id);
                const isCmp = cmp.includes(p.id);
                return `
                    <article class="product-card">
                        <div class="card-img-wrapper">
                            ${p.onSale ? `<span class="card-badge">Sale</span>` : ''}
                            <img src="${p.images[0]}" alt="${p.name}">
                            <div class="card-actions">
                                <button onclick="toggleWishlistBtn('${p.id}');" class="card-btn" aria-label="Add to wishlist">
                                    <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="${isSaved ? 'currentColor' : 'none'}" stroke-linecap="round" stroke-linejoin="round" style="${isSaved ? 'color: var(--color-secondary)' : ''}"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                                </button>
                                <button onclick="toggleCompareBtn('${p.id}');" class="card-btn" aria-label="Compare" style="${isCmp ? 'background-color: var(--color-secondary); color: white;' : ''}">
                                    <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"></polyline><line x1="4" y1="20" x2="21" y2="3"></line><polyline points="21 16 21 21 16 21"></polyline><line x1="15" y1="15" x2="21" y2="21"></line><line x1="4" y1="4" x2="9" y2="9"></line></article>
                                </button>
                                <a href="product.html?id=${p.id}" class="card-btn" aria-label="View Details">
                                    <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                                </a>
                            </div>
                        </div>
                        <div class="card-info">
                            <span class="card-brand">${p.brand}</span>
                            <h3 class="card-title"><a href="product.html?id=${p.id}">${p.name}</a></h3>
                            <div class="card-rating">
                                <span class="stars">${renderStarsHTML(p.rating)}</span>
                                <span class="card-rating-text">(${p.reviewsCount})</span>
                            </div>
                            <div class="card-price-row">
                                <span class="card-price">$${p.price.toFixed(2)}</span>
                                ${p.originalPrice ? `<span class="card-price-old">$${p.originalPrice.toFixed(2)}</span>` : ''}
                            </div>
                        </div>
                    </article>
                `;
            }).join('');
        }, 300);
    }

    // Expose toggle utilities inside window
    window.toggleWishlistBtn = function(id) {
        const added = window.Storage.toggleWishlist(id);
        window.showToast(added ? "Added to Wishlist!" : "Removed from Wishlist!", added ? "success" : "info");
        renderFilteredProducts();
    };

    window.toggleCompareBtn = function(id) {
        const added = window.Storage.toggleCompare(id);
        if (added === "limit") {
            window.showToast("You can compare up to 3 products only!", "error");
        } else {
            window.showToast(added ? "Added to Compare list!" : "Removed from Compare list!", added ? "success" : "info");
            renderFilteredProducts();
        }
    };

    window.resetAllFilters = function() {
        [...brandCheckboxes, ...catCheckboxes, ...sizeCheckboxes].forEach(c => c.checked = false);
        colorSwatches.forEach(s => s.classList.remove('active'));
        ratingRadio.forEach(r => r.checked = false);
        if (priceSlider) priceSlider.value = 250;
        if (priceOutput) priceOutput.textContent = '$250';
        activeColor = null;
        activeRating = null;
        renderFilteredProducts();
    };
}

function renderStarsHTML(rating) {
    let html = '';
    const full = Math.floor(rating);
    const half = rating % 1 >= 0.5;
    for (let i = 1; i <= 5; i++) {
        if (i <= full) {
            html += '★';
        } else if (i === full + 1 && half) {
            html += '½';
        } else {
            html += '☆';
        }
    }
    return html;
}
