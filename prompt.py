import os
import zipfile
import shutil

# Define the root directory name
ROOT_DIR = "premium-shoe-store"

# Dictionary of all files and their full, production-ready contents
project_files = {}

# ==========================================
# 1. DESIGN SYSTEM & CSS VARIABLES
# ==========================================
project_files['css/variables.css'] = """/* DESIGN SYSTEM & CORE TOKENS */
:root {
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    --font-heading: 'Poppins', sans-serif;

    /* Color Palette - Premium Luxury Archetype (Nike/Apple Aesthetic) */
    --color-primary: #000000;
    --color-primary-hover: #1e1e1e;
    --color-secondary: #e05a47;
    --color-bg: #ffffff;
    --color-text: #111111;
    --color-muted: #767676;
    --color-light-bg: #f5f5f7;
    --color-border: #e5e5e7;
    --color-success: #00aa6c;
    --color-error: #ff3b30;
    --color-card-bg: #ffffff;
    --color-input-bg: #ffffff;
    --color-gold: #ffb800;
    
    /* Shadows */
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.05);
    --shadow-md: 0 8px 16px rgba(0,0,0,0.08);
    --shadow-lg: 0 16px 32px rgba(0,0,0,0.12);
    
    /* Borders & Radius */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 16px;
    --radius-circle: 50%;
    
    /* Animations */
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    
    /* Layout Constants */
    --container-width: 1200px;
    --header-height: 80px;
}

/* Dark Mode Variables Override */
body.dark-mode {
    --color-primary: #ffffff;
    --color-primary-hover: #e5e5e7;
    --color-bg: #0b0b0c;
    --color-text: #f5f5f7;
    --color-muted: #8e8e93;
    --color-light-bg: #1c1c1e;
    --color-border: #2c2c2e;
    --color-card-bg: #121214;
    --color-input-bg: #1c1c1e;
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.3);
    --shadow-md: 0 8px 16px rgba(0,0,0,0.4);
    --shadow-lg: 0 16px 32px rgba(0,0,0,0.5);
}
"""

# ==========================================
# 2. BASE, RESETS, & SCROLLBARS
# ==========================================
project_files['css/base.css'] = """/* RESET & BASE STYLES */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-sans);
    background-color: var(--color-bg);
    color: var(--color-text);
    line-height: 1.6;
    overflow-x: hidden;
    transition: background-color 0.3s ease, color 0.3s ease;
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    font-weight: 700;
    color: var(--color-text);
}

a {
    color: inherit;
    text-decoration: none;
    transition: var(--transition);
}

img {
    max-width: 100%;
    height: auto;
    display: block;
}

button, input, select, textarea {
    font-family: inherit;
    font-size: inherit;
    background: none;
    border: none;
    outline: none;
}

button {
    cursor: pointer;
    transition: var(--transition);
}

ul, ol {
    list-style: none;
}

/* Scrollbar Customization */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: var(--color-light-bg);
}
::-webkit-scrollbar-thumb {
    background: var(--color-muted);
    border-radius: var(--radius-sm);
}
::-webkit-scrollbar-thumb:hover {
    background: var(--color-primary);
}

/* Shared Global Component Elements */
.container {
    width: 90%;
    max-width: var(--container-width);
    margin: 0 auto;
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.8rem 2rem;
    font-family: var(--font-heading);
    font-weight: 600;
    border-radius: var(--radius-sm);
    transition: var(--transition);
}

.btn-primary {
    background-color: var(--color-primary);
    color: var(--color-bg);
}

.btn-primary:hover {
    background-color: var(--color-primary-hover);
    transform: translateY(-2px);
}

.btn-secondary {
    background-color: transparent;
    border: 2px solid var(--color-primary);
    color: var(--color-text);
}

.btn-secondary:hover {
    background-color: var(--color-primary);
    color: var(--color-bg);
    transform: translateY(-2px);
}

.section-title {
    font-size: 2.2rem;
    margin-bottom: 2rem;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1px;
}
"""

# ==========================================
# 3. LAYOUT (HEADER, FOOTER, SEARCH OVERLAY)
# ==========================================
project_files['css/layout.css'] = """/* HEADER, NAV, FOOTER, OVERLAYS */
header {
    height: var(--header-height);
    background-color: rgba(var(--color-bg), 0.85);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--color-border);
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
    transition: var(--transition);
}

header.sticky {
    box-shadow: var(--shadow-sm);
    height: 70px;
}

.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 100%;
}

.logo {
    font-family: var(--font-heading);
    font-weight: 800;
    font-size: 1.5rem;
    letter-spacing: -0.5px;
}

.logo span {
    color: var(--color-secondary);
}

.nav-links {
    display: flex;
    gap: 2rem;
}

.nav-links a {
    font-weight: 500;
    letter-spacing: 0.5px;
    font-size: 0.95rem;
    position: relative;
    padding: 0.5rem 0;
}

.nav-links a::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background-color: var(--color-secondary);
    transition: var(--transition);
}

.nav-links a:hover::after, .nav-links a.active::after {
    width: 100%;
}

.nav-tools {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

.nav-tools a, .nav-tools button {
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--color-text);
    position: relative;
}

.nav-tools a:hover {
    color: var(--color-secondary);
}

/* Badge Counter */
.wishlist-badge, .cart-badge {
    position: absolute;
    top: -8px;
    right: -8px;
    background-color: var(--color-secondary);
    color: #ffffff;
    font-size: 0.7rem;
    font-weight: 700;
    width: 16px;
    height: 16px;
    border-radius: var(--radius-circle);
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Dark Mode Slider Toggle */
.theme-switch {
    display: inline-block;
    width: 44px;
    height: 22px;
    position: relative;
}

.theme-switch input {
    display: none;
}

.slider {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: var(--color-border);
    border-radius: 34px;
    cursor: pointer;
    transition: 0.4s;
}

.slider:before {
    position: absolute;
    content: "";
    height: 16px; width: 16px;
    left: 3px; bottom: 3px;
    background-color: white;
    border-radius: 50%;
    transition: 0.4s;
}

input:checked + .slider {
    background-color: var(--color-secondary);
}

input:checked + .slider:before {
    transform: translateX(22px);
}

/* Hamburger Mobile Toggle */
.hamburger {
    display: none;
    flex-direction: column;
    gap: 4px;
    width: 24px;
}

.hamburger span {
    width: 100%;
    height: 2px;
    background-color: var(--color-text);
    transition: var(--transition);
}

/* Footer Section */
footer {
    background-color: var(--color-light-bg);
    border-top: 1px solid var(--color-border);
    padding: 5rem 0 2rem 0;
    margin-top: 6rem;
}

.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1.5fr;
    gap: 3rem;
    margin-bottom: 4rem;
}

.footer-col h4 {
    font-size: 1.1rem;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.footer-col p {
    color: var(--color-muted);
    margin-bottom: 1rem;
}

.footer-links li {
    margin-bottom: 0.8rem;
}

.footer-links a {
    color: var(--color-muted);
}

.footer-links a:hover {
    color: var(--color-secondary);
    padding-left: 5px;
}

/* Newsletter Input Form */
.newsletter-form {
    display: flex;
    gap: 0.5rem;
    margin-top: 1rem;
}

.newsletter-form input {
    flex: 1;
    background-color: var(--color-input-bg);
    border: 1px solid var(--color-border);
    padding: 0.75rem;
    border-radius: var(--radius-sm);
    color: var(--color-text);
}

.newsletter-form button {
    background-color: var(--color-primary);
    color: var(--color-bg);
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    border-radius: var(--radius-sm);
}

.footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--color-border);
    padding-top: 2rem;
}

.footer-bottom p {
    color: var(--color-muted);
    font-size: 0.9rem;
}

.payment-logos {
    display: flex;
    gap: 1rem;
}

/* Mobile Navigation Drawer */
.mobile-drawer {
    position: fixed;
    top: 0;
    right: -300px;
    width: 300px;
    height: 100vh;
    background-color: var(--color-bg);
    box-shadow: var(--shadow-lg);
    z-index: 10000;
    padding: 3rem 2rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    transition: var(--transition);
}

.mobile-drawer.active {
    right: 0;
}

.drawer-close {
    font-size: 2rem;
    align-self: flex-end;
}

.drawer-links {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.drawer-links a {
    font-size: 1.2rem;
    font-weight: 600;
}

.drawer-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0,0,0,0.4);
    backdrop-filter: blur(4px);
    z-index: 9999;
    opacity: 0;
    pointer-events: none;
    transition: var(--transition);
}

.drawer-overlay.active {
    opacity: 1;
    pointer-events: auto;
}

/* Search Overlay Dialog */
.search-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background-color: rgba(var(--color-bg), 0.98);
    z-index: 10000;
    opacity: 0;
    pointer-events: none;
    transition: var(--transition);
    display: flex;
    align-items: center;
    justify-content: center;
}

.search-overlay.active {
    opacity: 1;
    pointer-events: auto;
}

.search-close {
    position: absolute;
    top: 2rem;
    right: 3rem;
    font-size: 2.5rem;
}

.search-box-panel {
    width: 90%;
    max-width: 700px;
    text-align: center;
}

.search-form input {
    width: 100%;
    border-bottom: 2px solid var(--color-border);
    font-size: 2rem;
    padding: 1rem 0;
    text-align: center;
    color: var(--color-text);
}

.search-form input:focus {
    border-color: var(--color-secondary);
}

.search-suggestions {
    margin-top: 2rem;
    max-height: 400px;
    overflow-y: auto;
    text-align: left;
}

.suggest-item {
    display: flex;
    align-items: center;
    padding: 0.8rem;
    border-bottom: 1px solid var(--color-border);
    transition: var(--transition);
}

.suggest-item:hover {
    background-color: var(--color-light-bg);
}

.suggest-item img {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: var(--radius-sm);
    margin-right: 1.5rem;
}

.suggest-info {
    flex: 1;
}

.suggest-title {
    display: block;
    font-weight: 600;
}

.suggest-brand {
    font-size: 0.8rem;
    color: var(--color-muted);
}

.suggest-price {
    font-weight: 700;
}

.no-suggest {
    color: var(--color-muted);
    padding: 1rem;
    text-align: center;
}
"""

# ==========================================
# 4. SHARED COMPONENTS (CARDS, MODALS, TOASTS)
# ==========================================
project_files['css/components.css'] = """/* CARDS, BADGES, SKELETONS, STARS, ACCORDIONS, TOASTS */

/* Product Card */
.product-card {
    background-color: var(--color-card-bg);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    overflow: hidden;
    position: relative;
    transition: var(--transition);
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
}

.card-img-wrapper {
    position: relative;
    background-color: var(--color-light-bg);
    overflow: hidden;
    aspect-ratio: 1;
}

.card-img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.product-card:hover .card-img-wrapper img {
    transform: scale(1.05);
}

.card-badge {
    position: absolute;
    top: 1rem;
    left: 1rem;
    background-color: var(--color-secondary);
    color: #ffffff;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.3rem 0.8rem;
    border-radius: var(--radius-sm);
    text-transform: uppercase;
}

.card-actions {
    position: absolute;
    bottom: -50px;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    padding: 1rem;
    background: linear-gradient(to top, rgba(0,0,0,0.6), transparent);
    transition: var(--transition);
}

.product-card:hover .card-actions {
    bottom: 0;
}

.card-btn {
    width: 40px;
    height: 40px;
    background-color: var(--color-bg);
    color: var(--color-text);
    border-radius: var(--radius-circle);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: var(--shadow-sm);
}

.card-btn:hover {
    background-color: var(--color-secondary);
    color: #ffffff;
}

.card-info {
    padding: 1.5rem;
}

.card-brand {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--color-muted);
    margin-bottom: 0.25rem;
}

.card-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.card-rating {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    margin-bottom: 0.5rem;
}

.card-rating-text {
    font-size: 0.8rem;
    color: var(--color-muted);
}

.card-price-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.card-price {
    font-weight: 700;
    font-size: 1.1rem;
}

.card-price-old {
    text-decoration: line-through;
    color: var(--color-muted);
    font-size: 0.95rem;
}

/* Star Rating Display */
.stars {
    display: flex;
    color: var(--color-gold);
}

/* Toast Container & Notification Box */
.toast-container {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    z-index: 11000;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}

.toast {
    background-color: var(--color-primary);
    color: var(--color-bg);
    padding: 1rem 1.5rem;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-lg);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.5rem;
    min-width: 280px;
    transform: translateX(120%);
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.toast.visible {
    transform: translateX(0);
}

.toast-success {
    border-left: 4px solid var(--color-success);
}

.toast-error {
    border-left: 4px solid var(--color-error);
}

.toast-close {
    color: inherit;
    font-size: 1.2rem;
    font-weight: 700;
}

/* Loading Skeleton Layout */
.skeleton-box {
    background: linear-gradient(90deg, var(--color-light-bg) 25%, var(--color-border) 50%, var(--color-light-bg) 75%);
    background-size: 200% 100%;
    animation: skeleton-pulsing 1.5s infinite;
    border-radius: var(--radius-sm);
}

@keyframes skeleton-pulsing {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

/* Interactive Accordion panel */
.accordion-item {
    border-bottom: 1px solid var(--color-border);
}

.accordion-header {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 0;
    font-weight: 600;
    font-family: var(--font-heading);
    text-align: left;
    color: var(--color-text);
}

.accordion-header svg {
    transition: var(--transition);
}

.accordion-header.active svg {
    transform: rotate(180deg);
}

.accordion-body {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s cubic-bezier(0, 1, 0, 1);
}

.accordion-body-inner {
    padding-bottom: 1.5rem;
    color: var(--color-muted);
}

/* Back To Top Button */
.back-to-top {
    position: fixed;
    bottom: 2rem;
    left: 2rem;
    width: 45px;
    height: 45px;
    background-color: var(--color-primary);
    color: var(--color-bg);
    border-radius: var(--radius-circle);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: var(--shadow-md);
    opacity: 0;
    visibility: hidden;
    z-index: 999;
}

.back-to-top.visible {
    opacity: 1;
    visibility: visible;
}

/* Modals General Framework */
.modal-wrapper {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background-color: rgba(0,0,0,0.5);
    backdrop-filter: blur(5px);
    z-index: 10001;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0; pointer-events: none;
    transition: var(--transition);
}

.modal-wrapper.active {
    opacity: 1; pointer-events: auto;
}

.modal-container {
    background-color: var(--color-bg);
    padding: 2rem;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    max-width: 600px;
    width: 90%;
    position: relative;
    transform: translateY(-50px);
    transition: var(--transition);
}

.modal-wrapper.active .modal-container {
    transform: translateY(0);
}

.modal-close {
    position: absolute;
    top: 1.5rem; right: 1.5rem;
    font-size: 1.5rem;
}
"""

# ==========================================
# 5. PAGES SPECIFIC STYLES
# ==========================================
project_files['css/pages.css'] = """/* PAGE UNIQUE LAYOUT STYLES COHESION */

/* Adjust body padding for sticky header */
body {
    padding-top: var(--header-height);
}

/* 5.1 HOME HERO BLOCK */
.hero-slider {
    position: relative;
    height: 80vh;
    background-color: var(--color-light-bg);
    overflow: hidden;
}

.slide {
    display: flex;
    align-items: center;
    height: 100%;
    padding: 0 5%;
}

.hero-text {
    flex: 1;
    z-index: 2;
}

.hero-text h1 {
    font-size: 4rem;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
}

.hero-text p {
    font-size: 1.2rem;
    color: var(--color-muted);
    margin-bottom: 2rem;
    max-width: 500px;
}

.hero-image-pane {
    flex: 1;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
}

.hero-img {
    max-height: 85%;
    object-fit: contain;
    transform: rotate(-15deg);
    transition: transform 0.5s ease;
}

.slide:hover .hero-img {
    transform: rotate(-5deg) scale(1.05);
}

/* Categories Section */
.categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.category-banner {
    position: relative;
    border-radius: var(--radius-md);
    overflow: hidden;
    height: 350px;
}

.category-banner img {
    width: 100%; height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.category-banner:hover img {
    transform: scale(1.05);
}

.category-overlay {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(to top, rgba(0,0,0,0.7), transparent);
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 2rem;
    color: #ffffff;
}

.category-overlay h3 {
    font-size: 1.5rem;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    color: #ffffff;
}

/* 5.2 SHOP CATALOG */
.shop-layout {
    display: grid;
    grid-template-columns: 260px 1fr;
    gap: 2.5rem;
    margin-top: 3rem;
}

/* Filter Sidebar panel */
.sidebar-filters h3 {
    font-size: 1.3rem;
    border-bottom: 2px solid var(--color-text);
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

.filter-group {
    margin-bottom: 2rem;
}

.filter-title {
    font-size: 0.95rem;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 1rem;
    display: block;
}

.checkbox-list {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
}

.checkbox-label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.9rem;
    cursor: pointer;
}

.checkbox-label input {
    accent-color: var(--color-secondary);
}

/* Color swatches widget */
.swatch-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.swatch-color {
    width: 25px; height: 25px;
    border-radius: var(--radius-circle);
    border: 1px solid var(--color-border);
    cursor: pointer;
    position: relative;
}

.swatch-color.active::after {
    content: '✓';
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 0.75rem;
    text-shadow: 0 1px 2px black;
}

/* Sort & Search control bar */
.catalog-toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.catalog-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.5rem;
}

/* Empty states */
.empty-state {
    text-align: center;
    padding: 5rem 0;
}

.empty-state svg {
    margin-bottom: 1.5rem;
    color: var(--color-muted);
}

/* 5.3 PRODUCT PAGE */
.product-hero {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 4rem;
    margin-top: 2rem;
}

/* Left Gallery viewer */
.gallery-layout {
    display: flex;
    gap: 1rem;
}

.thumbnails-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.thumbnail-pane {
    width: 80px; height: 80px;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-sm);
    overflow: hidden;
    cursor: pointer;
}

.thumbnail-pane.active {
    border-color: var(--color-secondary);
}

.thumbnail-pane img {
    width: 100%; height: 100%;
    object-fit: cover;
}

.main-view-container {
    flex: 1;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    overflow: hidden;
    background-color: var(--color-light-bg);
    position: relative;
    cursor: zoom-in;
}

.main-view-container img {
    width: 100%; height: 100%;
    object-fit: cover;
    transition: transform 0.1s ease-out;
}

/* Right Information column */
.product-title-block h1 {
    font-size: 2.2rem;
    margin-bottom: 0.5rem;
}

.product-brand {
    font-size: 0.9rem;
    color: var(--color-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.product-price-bar {
    font-size: 1.8rem;
    font-weight: 700;
    margin: 1.5rem 0;
}

.product-options-row {
    margin-bottom: 1.5rem;
}

.option-heading {
    font-size: 0.9rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
    text-transform: uppercase;
}

/* Buttons sizes selection */
.sizes-button-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.size-btn {
    width: 50px; height: 40px;
    border: 1px solid var(--color-border);
    background-color: var(--color-card-bg);
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: var(--radius-sm);
}

.size-btn.active {
    background-color: var(--color-primary);
    color: var(--color-bg);
    border-color: var(--color-primary);
}

.size-btn.disabled {
    opacity: 0.4;
    cursor: not-allowed;
    text-decoration: line-through;
}

/* Quantity Counter widget */
.qty-widget {
    display: inline-flex;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-sm);
    overflow: hidden;
    margin-right: 1.5rem;
}

.qty-btn {
    width: 40px; height: 40px;
    background-color: var(--color-light-bg);
    color: var(--color-text);
    font-size: 1.2rem;
}

.qty-input {
    width: 50px; height: 40px;
    text-align: center;
    font-weight: 700;
    background-color: var(--color-card-bg);
    color: var(--color-text);
}

/* Tabs Description/Reviews Block */
.tabs-navigation {
    display: flex;
    border-bottom: 1px solid var(--color-border);
    margin-top: 4rem;
    margin-bottom: 2rem;
}

.tab-btn {
    padding: 1rem 2rem;
    font-weight: 600;
    font-family: var(--font-heading);
    position: relative;
    color: var(--color-muted);
}

.tab-btn.active {
    color: var(--color-text);
}

.tab-btn.active::after {
    content: '';
    position: absolute;
    bottom: -1px; left: 0; width: 100%; height: 2px;
    background-color: var(--color-secondary);
}

.tab-pane {
    display: none;
}

.tab-pane.active {
    display: block;
}

/* Specifications Tab layout */
.specs-table {
    width: 100%;
    border-collapse: collapse;
}

.specs-table tr {
    border-bottom: 1px solid var(--color-border);
}

.specs-table td {
    padding: 1rem;
}

.specs-table td:first-child {
    font-weight: 700;
    width: 30%;
    background-color: var(--color-light-bg);
}

/* Reviews layout elements */
.reviews-grid {
    display: grid;
    grid-template-columns: 1fr 2fr;
    gap: 3rem;
}

.ratings-panel {
    background-color: var(--color-light-bg);
    padding: 2rem;
    border-radius: var(--radius-md);
    text-align: center;
}

.ratings-panel h2 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.stars-distribution {
    margin-top: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.dist-row {
    display: flex;
    align-items: center;
    gap: 1rem;
    font-size: 0.85rem;
}

.dist-bar {
    flex: 1;
    height: 8px;
    background-color: var(--color-border);
    border-radius: 4px;
    overflow: hidden;
}

.dist-fill {
    height: 100%;
    background-color: var(--color-gold);
}

/* 5.4 CART PAGE */
.cart-layout {
    display: grid;
    grid-template-columns: 1.8fr 1fr;
    gap: 3rem;
    margin-top: 3rem;
}

.cart-items-table {
    width: 100%;
    border-collapse: collapse;
}

.cart-items-table th {
    text-align: left;
    padding-bottom: 1rem;
    border-bottom: 2px solid var(--color-border);
    text-transform: uppercase;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
}

.cart-item-row {
    border-bottom: 1px solid var(--color-border);
}

.cart-item-row td {
    padding: 1.5rem 0;
}

.cart-product-cell {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

.cart-prod-img {
    width: 80px; height: 80px;
    object-fit: cover;
    border-radius: var(--radius-sm);
    background-color: var(--color-light-bg);
}

.cart-prod-name {
    font-weight: 600;
}

.cart-prod-meta {
    font-size: 0.8rem;
    color: var(--color-muted);
}

/* Sidebar Order Summary checkout calculations card */
.cart-summary-card {
    background-color: var(--color-light-bg);
    padding: 2rem;
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
    position: sticky;
    top: 100px;
}

.summary-totals-list {
    margin: 1.5rem 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.summary-row {
    display: flex;
    justify-content: space-between;
}

.summary-row-total {
    border-top: 1px solid var(--color-border);
    padding-top: 1rem;
    font-weight: 700;
    font-size: 1.2rem;
}

/* 5.5 CHECKOUT SYSTEM */
.checkout-layout {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 3rem;
    margin-top: 3rem;
}

/* Step tracker indicator */
.checkout-steps {
    display: flex;
    justify-content: space-between;
    margin-bottom: 3rem;
    position: relative;
}

.checkout-steps::before {
    content: '';
    position: absolute;
    top: 15px; left: 0; width: 100%; height: 2px;
    background-color: var(--color-border);
    z-index: 1;
}

.step-node {
    position: relative;
    z-index: 2;
    background-color: var(--color-bg);
    padding: 0 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}

.step-circle {
    width: 32px; height: 32px;
    border-radius: var(--radius-circle);
    border: 2px solid var(--color-border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    background-color: var(--color-bg);
    color: var(--color-muted);
}

.step-node.active .step-circle {
    border-color: var(--color-secondary);
    color: var(--color-secondary);
    background-color: var(--color-bg);
}

.step-node.completed .step-circle {
    background-color: var(--color-success);
    border-color: var(--color-success);
    color: white;
}

/* Form structure inputs */
.form-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.2rem;
}

.form-full {
    grid-column: span 2;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-group label {
    font-size: 0.85rem;
    font-weight: 600;
}

.form-group input, .form-group select {
    background-color: var(--color-input-bg);
    border: 1px solid var(--color-border);
    padding: 0.8rem;
    border-radius: var(--radius-sm);
    color: var(--color-text);
}

.form-group input:focus, .form-group select:focus {
    border-color: var(--color-primary);
}

/* Credit Card graphic interactive micro visual */
.card-preview-wrapper {
    margin: 2rem 0;
    perspective: 1000px;
}

.credit-card-inner {
    width: 380px; height: 220px;
    background: linear-gradient(135deg, #1c2a48 0%, #0c1220 100%);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    color: white;
    padding: 2rem;
    position: relative;
    transform-style: preserve-3d;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    margin: 0 auto;
}

.credit-card-inner.flipped {
    transform: rotateY(180deg);
}

.card-front, .card-back {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    backface-visibility: hidden;
    padding: 1.8rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.card-back {
    transform: rotateY(180deg);
    background: linear-gradient(135deg, #0c1220 0%, #111 100%);
}

.card-signature {
    width: 100%; height: 40px;
    background-color: #eee;
    margin-top: 1rem;
}

.card-cvv-strip {
    text-align: right;
    color: #000;
    padding: 0.5rem;
}

/* Custom visual layout elements */
.card-logo {
    font-family: var(--font-heading);
    font-weight: 800;
    font-style: italic;
    font-size: 1.2rem;
    text-align: right;
}

.card-chip {
    width: 45px; height: 35px;
    background-color: var(--color-gold);
    border-radius: var(--radius-sm);
}

.card-digits {
    font-size: 1.35rem;
    letter-spacing: 2px;
    font-family: monospace;
    margin: 1.5rem 0;
}

.card-info-row {
    display: flex;
    justify-content: space-between;
    text-transform: uppercase;
    font-size: 0.8rem;
}

/* Full-Screen Loading Overlay */
.loading-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background-color: rgba(0,0,0,0.85);
    backdrop-filter: blur(8px);
    z-index: 12000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    opacity: 0; pointer-events: none;
    transition: var(--transition);
}

.loading-overlay.active {
    opacity: 1; pointer-events: auto;
}

.spinner {
    width: 60px; height: 60px;
    border: 4px solid rgba(255,255,255,0.2);
    border-top-color: var(--color-secondary);
    border-radius: var(--radius-circle);
    animation: spinning 1s linear infinite;
    margin-bottom: 2rem;
}

@keyframes spinning {
    100% { transform: rotate(360deg); }
}

/* 5.6 CABINET DASHBOARD */
.account-layout {
    display: grid;
    grid-template-columns: 240px 1fr;
    gap: 3rem;
    margin-top: 3rem;
}

.cabinet-sidebar-nav {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.cabinet-nav-btn {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem;
    font-weight: 600;
    border-radius: var(--radius-sm);
    color: var(--color-muted);
}

.cabinet-nav-btn:hover, .cabinet-nav-btn.active {
    background-color: var(--color-light-bg);
    color: var(--color-text);
}

/* Status Timelines */
.timeline-stepper {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
}

.timeline-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    flex: 1;
    position: relative;
}

.timeline-node:not(:last-child)::after {
    content: '';
    position: absolute;
    top: 15px; left: 50%; width: 100%; height: 2px;
    background-color: var(--color-border);
}

.timeline-node.completed:not(:last-child)::after {
    background-color: var(--color-success);
}

.timeline-dot {
    width: 30px; height: 30px;
    border-radius: var(--radius-circle);
    background-color: var(--color-border);
}

.timeline-node.completed .timeline-dot {
    background-color: var(--color-success);
}

/* FAQ Accordion page content */
.faq-wrap {
    max-width: 800px;
    margin: 0 auto;
}

/* Blog Magazine Section */
.blog-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.blog-card {
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    overflow: hidden;
    background-color: var(--color-card-bg);
}

.blog-img-pane {
    height: 220px;
    overflow: hidden;
}

.blog-img-pane img {
    width: 100%; height: 100%;
    object-fit: cover;
}

.blog-card-body {
    padding: 1.5rem;
}

.blog-card-date {
    font-size: 0.8rem;
    color: var(--color-muted);
}

.blog-card-title {
    font-size: 1.25rem;
    margin: 0.5rem 0;
}
"""

# ==========================================
# 6. STATIC RAW JSON DATABASE
# ==========================================
project_files['js/api-mock.js'] = """/* RAW JSON DATABASE OBJECT SCHEMA */
window.db = {
    products: [
        {
            id: "SKU-001",
            name: "Air Max Apex 90",
            brand: "Nike",
            category: "Athletic",
            price: 159.99,
            originalPrice: 199.99,
            onSale: true,
            rating: 4.8,
            reviewsCount: 142,
            images: [
                "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?auto=format&fit=crop&w=800&q=80"
            ],
            colors: ["Varsity Red", "Noir Black", "Platinum White"],
            sizes: [7, 8, 9, 10, 11, 12],
            stock: {
                "Varsity Red-8": 12, "Varsity Red-9": 15, "Varsity Red-10": 0,
                "Noir Black-8": 4, "Noir Black-9": 8, "Noir Black-10": 14,
                "Platinum White-8": 9, "Platinum White-9": 11, "Platinum White-10": 6
            },
            description: "Step into greatness with the ultimate combination of luxury and performance. Features responsive Max Air cushioning, premium leather overlays, and deep-grooved traction waffle soles.",
            specs: {
                "Upper Material": "Premium Full Grain Leather & Mesh",
                "Sole Material": "Waffle Tread Rubber with Max Air Cushioning",
                "Weight": "0.42 kg (per shoe, size 9)",
                "Country of Origin": "Vietnam"
            },
            reviews: [
                { user: "Alexander G.", rating: 5, date: "2026-06-12", comment: "The comfort is unmatched. Perfect red tint that pops with any outfit!" },
                { user: "Marcus K.", rating: 4, date: "2026-05-30", comment: "Incredibly fast delivery. Sole is slightly stiff initially but breaks in beautifully." }
            ],
            tags: ["new", "bestseller", "red", "airmax"]
        },
        {
            id: "SKU-002",
            name: "Ultraboost Pure 22",
            brand: "Adidas",
            category: "Running",
            price: 180.00,
            originalPrice: null,
            onSale: false,
            rating: 4.9,
            reviewsCount: 96,
            images: [
                "https://images.unsplash.com/photo-1608231387042-66d1773070a5?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1587563871167-1ee981d634f4?auto=format&fit=crop&w=800&q=80"
            ],
            colors: ["Triple White", "Core Black"],
            sizes: [8, 9, 10, 11],
            stock: {
                "Triple White-8": 5, "Triple White-9": 3, "Triple White-10": 0,
                "Core Black-8": 7, "Core Black-9": 10, "Core Black-10": 12
            },
            description: "Designed for endless energy return, the Ultraboost features a soft Primeknit upper that adapts to your foot, coupled with our signature responsive Boost midsole.",
            specs: {
                "Upper Material": "Primeknit (50% recycled ocean plastic)",
                "Sole Material": "Continental™ Better Rubber Outsole",
                "Weight": "0.38 kg",
                "Country of Origin": "Germany"
            },
            reviews: [
                { user: "Sarah L.", rating: 5, date: "2026-07-01", comment: "Like walking on clouds. Highly recommend the Triple White variant!" }
            ],
            tags: ["running", "boost", "adidas"]
        },
        {
            id: "SKU-003",
            name: "Cali Suede Classic",
            brand: "Puma",
            category: "Lifestyle",
            price: 79.99,
            originalPrice: 89.99,
            onSale: true,
            rating: 4.5,
            reviewsCount: 54,
            images: [
                "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=800&q=80"
            ],
            colors: ["Forest Green", "Mustard Yellow"],
            sizes: [7, 8, 9, 10, 11],
            stock: {
                "Forest Green-8": 15, "Forest Green-9": 18, "Forest Green-10": 20,
                "Mustard Yellow-8": 8, "Mustard Yellow-9": 5, "Mustard Yellow-10": 3
            },
            description: "A heritage streetwear classic. Featuring velvet-soft suede, clean Puma side stripe overlays, and a retro vulcanized platform rubber outsole.",
            specs: {
                "Upper Material": "Genuine Suede Leather",
                "Sole Material": "Vulcanized Platform Rubber",
                "Weight": "0.45 kg",
                "Country of Origin": "Indonesia"
            },
            reviews: [
                { user: "Derrick J.", rating: 4, date: "2026-06-18", comment: "Super clean looking. The suede is very high quality for the price." }
            ],
            tags: ["retro", "lifestyle", "suede"]
        },
        {
            id: "SKU-004",
            name: "990v5 Heritage Trainer",
            brand: "New Balance",
            category: "Lifestyle",
            price: 199.99,
            originalPrice: null,
            onSale: false,
            rating: 4.7,
            reviewsCount: 88,
            images: [
                "https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=800&q=80"
            ],
            colors: ["Castlerock Grey", "Tan Suede"],
            sizes: [8, 9, 10, 11, 12],
            stock: {
                "Castlerock Grey-8": 4, "Castlerock Grey-9": 5, "Castlerock Grey-10": 6,
                "Tan Suede-8": 3, "Tan Suede-9": 5, "Tan Suede-10": 8
            },
            description: "Crafted in the USA. The 990v5 combines clean, premium suede panels with supportive ENCAP midsole technology to establish the gold-standard of luxury streetwear trainers.",
            specs: {
                "Upper Material": "Premium Pigskin Suede & Nylon Mesh",
                "Sole Material": "ENCAP Cushioning with Ndurance Rubber Outsole",
                "Weight": "0.44 kg",
                "Country of Origin": "USA"
            },
            reviews: [
                { user: "Bradley N.", rating: 5, date: "2026-07-04", comment: "Simply the best shoe ever made. The grey suede is gorgeous." }
            ],
            tags: ["newbalance", "retro", "990"]
        },
        {
            id: "SKU-005",
            name: "Jordan Retro High OG",
            brand: "Nike",
            category: "Basketball",
            price: 180.00,
            originalPrice: null,
            onSale: false,
            rating: 4.95,
            reviewsCount: 310,
            images: [
                "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=800&q=80"
            ],
            colors: ["Bred Red", "Royal Blue"],
            sizes: [8, 9, 10, 11, 12, 13],
            stock: {
                "Bred Red-8": 2, "Bred Red-9": 5, "Bred Red-10": 3, "Bred Red-11": 0,
                "Royal Blue-8": 4, "Royal Blue-9": 1, "Royal Blue-10": 6, "Royal Blue-11": 2
            },
            description: "The sneaker that changed sports and fashion forever. Inspired by Michael Jordan's rookie season, built with full premium grain leather and classic rubber cupsole.",
            specs: {
                "Upper Material": "Full Grain Semi-Aniline Leather",
                "Sole Material": "Rubber Cupsole with Air-Sole Unit",
                "Weight": "0.48 kg",
                "Country of Origin": "China"
            },
            reviews: [
                { user: "Sami A.", rating: 5, date: "2026-07-10", comment: "A masterpiece of design. Fits perfectly, color is iconic." }
            ],
            tags: ["bestseller", "jordan", "nike", "basketball"]
        }
    ],
    coupons: [
        { code: "SNEAKER10", discountType: "percentage", value: 10 },
        { code: "FREESHIP", discountType: "free_shipping", value: 0 },
        { code: "GOLD20", discountType: "fixed", value: 20 }
    ],
    blogs: [
        {
            slug: "sneaker-styling-guide-2026",
            title: "The Ultimate Sneaker Styling Guide for 2026",
            author: "Julian Sterling",
            date: "July 12, 2026",
            image: "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=1200&q=80",
            content: "Sneakers have transcended their athletic origins to become the bedrock of high-fashion and daily wear. Whether you are rocking a classic pair of Jordan Retros, minimalistic low-tops, or thick heritage New Balance 990s, styling them is an art of balance. In this comprehensive guide, we explore how to pair your favorite kicks with oversized tailored trousers, classic utility cargos, and structural linen fits...",
            comments: [
                { user: "Leo D.", date: "2026-07-13", text: "This guide is gold! Tried the tailored trousers pairing with my NB 990s and got so many compliments." }
            ]
        },
        {
            slug: "running-mechanics-and-footwear",
            title: "Understanding Running Mechanics & Footwear Choices",
            author: "Dr. Alena Thorne",
            date: "June 28, 2026",
            image: "https://images.unsplash.com/photo-1515955656352-a1fa3ffcd111?auto=format&fit=crop&w=1200&q=80",
            content: "When selecting a running shoe, understanding pronation, footstrike, and muscle activation is crucial. Neutral shoes like the Ultraboost series serve runners who require impact dampening without physical stabilization structures. We discuss how high-energy materials like expanded polyurethane foam (Boost) protect joint cartilage and lower fatigue indexes during long distance training runs...",
            comments: []
        }
    ],
    faqs: [
        { q: "What is your return and exchange policy?", a: "We offer a 30-day hassle-free return and exchange policy. Shoes must be unworn, in original packaging, and with tags attached. Return shipping is free for all orders." },
        { q: "How long does shipping take?", a: "Standard Shipping takes 3-5 business days and is free on all orders above $150. Express Shipping takes 1-2 business days for a flat rate of $15.00." },
        { q: "Are your sneakers authentic?", a: "100% authentic. We source our sneakers directly from the brands or verified official retailers, complete with original boxes, accessories, and certification tags." },
        { q: "How do I choose the right size?", a: "We recommend checking our detailed size chart on the product details page. Most of our Nike and Adidas running shoes run true to size, but specific recommendations are highlighted under each shoe's details." }
    ]
};
"""

# ==========================================
# 7. STATE MANAGEMENT MODULE (LOCALSTORAGE)
# ==========================================
project_files['js/storage.js'] = """/* LOCAL STORAGE ACCESS SYSTEM UTILITIES */
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
    getCurrentUser() {
        let user = localStorage.getItem('shoestore_user');
        return user ? JSON.parse(user) : null;
    },
    setCurrentUser(user) {
        localStorage.setItem('shoestore_user', JSON.stringify(user));
        window.dispatchEvent(new Event('authUpdated'));
    },
    logout() {
        localStorage.removeItem('shoestore_user');
        window.dispatchEvent(new Event('authUpdated'));
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
        return addr ? JSON.parse(addr) : [
            { id: "addr_1", name: "John Doe", line1: "742 Evergreen Terrace", city: "Springfield", state: "IL", zip: "62704", country: "United States", phone: "555-0199", isDefault: true }
        ];
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
"""

# ==========================================
# 8. GLOBAL SYSTEM BOOT (HEADER, DRAWER, SEARCH)
# ==========================================
project_files['js/app.js'] = """/* GLOBAL DOM MANIPULATIONS AND REGISTRATIONS */
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
    
    if (searchTrigger && searchOverlay) {
        searchTrigger.addEventListener('click', (e) => {
            e.preventDefault();
            searchOverlay.classList.add('active');
            setTimeout(() => searchInput.focus(), 300);
        });
    }
    
    if (searchClose && searchOverlay) {
        searchClose.addEventListener('click', () => {
            searchOverlay.classList.remove('active');
            if (searchInput) searchInput.value = '';
            if (suggestionsList) suggestionsList.innerHTML = '';
        });
    }
    
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
"""

# ==========================================
# 9. DYNAMIC CATALOG INTEGRATION (filter.js)
# ==========================================
project_files['js/filter.js'] = """/* MULTIFACETED LIVE SHOP FILTER SYSTEM */
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
"""

# ==========================================
# 10. DETAILED PRODUCT UTILITIES (product.js)
# ==========================================
project_files['js/product.js'] = """/* ZOOM EFFECT, VARIANTS SWAP, DYNAMIC REVIEW BOARD */
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
"""

# ==========================================
# 11. SHOPPING CART ENGINE (cart.js)
# ==========================================
project_files['js/cart.js'] = """/* CALCULATE DISCOUNTS, UPDATE QUANTITIES, CART CRUD */
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
"""

# ==========================================
# 12. MULTISTEP CHECKOUT SYSTEM (checkout.js)
# ==========================================
project_files['js/checkout.js'] = """/* PROGRESS TRAPS, STRIPE-LOOK REALTIME CREDIT CARD */
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

    // Submit / Mock processing transaction flow
    window.placeOrderSubmit = function() {
        const overlay = document.getElementById('checkoutLoaderOverlay');
        const statusMsg = document.getElementById('loaderStatusMessage');
        
        if (overlay) overlay.classList.add('active');
        
        setTimeout(() => {
            if (statusMsg) statusMsg.textContent = "Authorizing credit transaction details...";
        }, 800);
        
        setTimeout(() => {
            if (statusMsg) statusMsg.textContent = "Packing your premium shipment...";
        }, 1600);

        setTimeout(() => {
            // Generate mock receipt data
            const orderId = "ORD-" + Math.floor(100000 + Math.random() * 900000);
            const fname = document.getElementById('shpFname').value;
            const lname = document.getElementById('shpLname').value;
            
            const subtotalText = document.getElementById('summarySubtotal').textContent;
            const shippingText = document.getElementById('summaryShipping').textContent;
            const taxText = document.getElementById('summaryTax').textContent;
            const totalText = document.getElementById('summaryTotal').textContent;
            
            const newOrder = {
                orderId: orderId,
                date: new Date().toLocaleDateString(),
                customerName: `${fname} ${lname}`,
                subtotal: subtotalText,
                shipping: shippingText,
                tax: taxText,
                total: totalText,
                status: "Shipped",
                items: cart.items.map(item => {
                    const product = window.db.products.find(p => p.id === item.productId);
                    return {
                        name: product ? product.name : "Premium Shoe",
                        color: item.variant.color,
                        size: item.variant.size,
                        quantity: item.quantity,
                        price: product ? `$${product.price.toFixed(2)}` : "$0.00"
                    };
                })
            };

            // Commit order, clear cart and redirect
            window.Storage.saveOrder(newOrder);
            window.Storage.saveCart({ items: [], coupon: null });
            
            window.location.href = `success.html?orderId=${orderId}`;
        }, 2500);
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
"""

# ==========================================
# 13. CABINET VISUALS CONTROL (account.js)
# ==========================================
project_files['js/account.js'] = """/* MANAGE PAST ORDERS INVOICES, DYNAMIC SAVED ADDRESS CARDS */
document.addEventListener('DOMContentLoaded', () => {
    initCabinetDashboard();
});

function initCabinetDashboard() {
    const listContainer = document.getElementById('pastOrdersList');
    const addressContainer = document.getElementById('addressGrid');
    
    // Auth Guard simulation
    let currentUser = window.Storage.getCurrentUser();
    if (!currentUser) {
        currentUser = { name: "Jane Doe", email: "jane.doe@example.com" };
        window.Storage.setCurrentUser(currentUser);
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

        profileForm.addEventListener('submit', (e) => {
            e.preventDefault();
            currentUser.name = pName.value.trim();
            currentUser.email = pEmail.value.trim();
            window.Storage.setCurrentUser(currentUser);
            window.showToast("Profile details updated successfully!", "success");
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
    function renderOrders() {
        if (!listContainer) return;
        const orders = window.Storage.getOrders();
        
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
        const order = window.Storage.getOrders().find(o => o.orderId === orderId);
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
    function renderAddresses() {
        if (!addressContainer) return;
        const list = window.Storage.getAddresses();
        
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
        form.addEventListener('submit', (e) => {
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
                id: "addr_" + Math.floor(Math.random() * 100000),
                name, line1, city, state, zip, phone,
                country: "United States",
                isDefault: def
            };
            
            window.Storage.addAddress(newAddr);
            window.showToast("New address added successfully!", "success");
            form.reset();
            toggleAddressModal();
            renderAddresses();
        });
    }

    window.deleteAddressBtn = function(id) {
        window.Storage.deleteAddress(id);
        window.showToast("Address deleted.", "info");
        renderAddresses();
    };

    window.logoutSession = function() {
        window.Storage.logout();
        window.showToast("Session ended. Securely logged out.", "info");
        setTimeout(() => window.location.href = "index.html", 1000);
    };
}
"""

# ==========================================
# 14. INJECT COMMON MASTER TEMPLATES (SHARED HTML)
# ==========================================
def get_header(title="KicksElite"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Premium Shoes Store</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/variables.css">
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/layout.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/pages.css">
</head>
<body>
    <header class="header">
        <div class="container navbar">
            <div class="logo-area">
                <a href="index.html" class="logo">KICKS<span>ELITE</span></a>
            </div>
            <nav class="nav-links" aria-label="Main Navigation">
                <a href="shop.html">Shop</a>
                <a href="shop.html?category=Running">Running</a>
                <a href="shop.html?category=Basketball">Basketball</a>
                <a href="shop.html?category=Athletic">Athletic</a>
                <a href="shop.html?category=Lifestyle">Lifestyle</a>
                <a href="about.html">About</a>
                <a href="blog.html">Blog</a>
            </nav>
            <div class="nav-tools">
                <label class="theme-switch" aria-label="Toggle Dark Mode">
                    <input type="checkbox" class="dark-mode-toggle">
                    <span class="slider"></span>
                </label>
                <a href="#" class="search-trigger" aria-label="Open Search">
                    <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                </a>
                <a href="wishlist.html" class="wishlist-trigger" aria-label="Wishlist">
                    <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                    <span class="wishlist-badge" style="display:none;">0</span>
                </a>
                <a href="cart.html" class="cart-trigger" aria-label="Shopping Cart">
                    <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                    <span class="cart-badge" style="display:none;">0</span>
                </a>
                <a href="account.html" class="account-trigger" aria-label="My Account">
                    <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                </a>
                <button class="hamburger" aria-label="Toggle Mobile Menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </header>

    <div class="mobile-drawer">
        <button class="drawer-close" aria-label="Close drawer menu">&times;</button>
        <nav class="drawer-links" aria-label="Mobile links">
            <a href="index.html">Home</a>
            <a href="shop.html">Shop All</a>
            <a href="shop.html?category=Running">Running</a>
            <a href="shop.html?category=Basketball">Basketball</a>
            <a href="shop.html?category=Athletic">Athletic</a>
            <a href="shop.html?category=Lifestyle">Lifestyle</a>
            <a href="about.html">About Us</a>
            <a href="blog.html">Blog</a>
            <a href="contact.html">Contact</a>
            <a href="faq.html">FAQ</a>
            <a href="account.html">My Account</a>
        </nav>
    </div>
    <div class="drawer-overlay"></div>

    <div class="search-overlay">
        <button class="search-close" aria-label="Close search overlay">&times;</button>
        <div class="search-box-panel">
            <form class="search-form" onsubmit="event.preventDefault();">
                <input type="search" class="search-input" placeholder="Type shoe name, color or brand..." aria-label="Search inputs">
            </form>
            <ul class="search-suggestions" role="listbox"></ul>
        </div>
    </div>
"""

def get_footer():
    return """    <footer>
        <div class="container footer-grid">
            <div class="footer-col">
                <a href="index.html" class="logo" style="margin-bottom:1.5rem; display:block;">KICKS<span>ELITE</span></a>
                <p>We source only high-quality elite sneakers curated across global brands. Dedicated to performance runners, basketballers, and streetwear collectors alike.</p>
                <form class="newsletter-form">
                    <input type="email" placeholder="Enter your email" aria-label="Newsletter email input" required>
                    <button type="submit">Join</button>
                </form>
            </div>
            <div class="footer-col">
                <h4>Help & Support</h4>
                <ul class="footer-links">
                    <li><a href="contact.html">Contact Us</a></li>
                    <li><a href="faq.html">FAQs Accordion</a></li>
                    <li><a href="tracking.html">Track Order Shipment</a></li>
                    <li><a href="compare.html">Compare Products</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Collections</h4>
                <ul class="footer-links">
                    <li><a href="shop.html?category=Running">Performance Running</a></li>
                    <li><a href="shop.html?category=Basketball">High-top Basketball</a></li>
                    <li><a href="shop.html?category=Athletic">Athletic Gym Shoes</a></li>
                    <li><a href="shop.html?category=Lifestyle">Streetwear Lifestyle</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Luxury Contact</h4>
                <p>KicksElite Corporate Headquarters,<br>742 Evergreen Plaza,<br>New York, NY 10001</p>
                <p>Phone: +1 (555) 234-5678<br>Email: customercare@kickselite.com</p>
            </div>
        </div>
        <div class="container footer-bottom">
            <p>&copy; 2026 KicksElite. Crafted for Awwwards Premium Showcase. All Rights Reserved.</p>
            <div class="payment-logos" aria-label="Accepted Credit Cards">
                <span style="font-size:1.5rem; opacity:0.6;">💳</span>
            </div>
        </div>
    </footer>

    <script src="js/api-mock.js"></script>
    <script src="js/storage.js"></script>
    <script src="js/app.js"></script>
</body>
</html>
"""

# ==========================================
# 15. HTML PAGES COMPILATIONS
# ==========================================

# index.html
project_files['index.html'] = get_header("Home") + """
<main>
    <section class="hero-slider" aria-label="Banner Showcase">
        <div class="slide">
            <div class="hero-text">
                <h1>Step Into Elite Comfort</h1>
                <p>Discover our newly curated performance trainers built with structural responsive materials and next-generation comfort grids.</p>
                <a href="shop.html" class="btn btn-primary">Shop Collection</a>
            </div>
            <div class="hero-image-pane">
                <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80" alt="Nike Red Apex Sneaker" class="hero-img">
            </div>
        </div>
    </section>

    <section class="container" style="margin-top: 5rem;" aria-label="Explore Categories">
        <h2 class="section-title">CURATED SEGMENTS</h2>
        <div class="categories-grid">
            <div class="category-banner">
                <img src="https://images.unsplash.com/photo-1515955656352-a1fa3ffcd111?auto=format&fit=crop&w=600&q=80" alt="Running Shoes Category">
                <div class="category-overlay">
                    <h3>Performance Running</h3>
                    <a href="shop.html?category=Running" style="text-decoration:underline;">Explore</a>
                </div>
            </div>
            <div class="category-banner">
                <img src="https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=600&q=80" alt="Lifestyle Shoes Category">
                <div class="category-overlay">
                    <h3>Lifestyle Streetwear</h3>
                    <a href="shop.html?category=Lifestyle" style="text-decoration:underline;">Explore</a>
                </div>
            </div>
            <div class="category-banner">
                <img src="https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?auto=format&fit=crop&w=600&q=80" alt="Athletic Shoes Category">
                <div class="category-overlay">
                    <h3>Athletic Comfort</h3>
                    <a href="shop.html?category=Athletic" style="text-decoration:underline;">Explore</a>
                </div>
            </div>
        </div>
    </section>

    <section class="container" style="margin-top: 5rem;">
        <h2 class="section-title">EXCLUSIVE HOT RELEASES</h2>
        <div class="catalog-grid" id="featuredGrid">
            </div>
    </section>

    <section class="container" style="margin-top: 5rem; padding: 4rem 2rem; background-color: var(--color-light-bg); border-radius: var(--radius-lg); text-align:center;">
        <h2 class="section-title">Verified Sneakerheads</h2>
        <p style="font-size:1.5rem; font-style:italic; max-width: 800px; margin: 0 auto 1.5rem auto; line-height:1.8;">"KicksElite is the gold-standard. The shipping details and packaging boxes are immaculate. Best premium checkout experience."</p>
        <strong>- Tyler K., Collector</strong>
    </section>
</main>
<script>
    document.addEventListener('DOMContentLoaded', () => {
        const grid = document.getElementById('featuredGrid');
        if (grid) {
            const list = window.db.products.slice(0, 4);
            grid.innerHTML = list.map(p => `
                <article class="product-card">
                    <div class="card-img-wrapper">
                        <img src="${p.images[0]}" alt="${p.name}">
                        <div class="card-actions">
                            <a href="product.html?id=${p.id}" class="card-btn" aria-label="View Product"><svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></a>
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
    });
</script>
""" + get_footer()

# shop.html
project_files['shop.html'] = get_header("Shop Sneakers Catalog") + """
<main class="container">
    <div class="shop-layout">
        <aside class="sidebar-filters" aria-label="Filters Panel">
            <h3>FILTERS</h3>
            
            <div class="filter-group">
                <span class="filter-title">Brands</span>
                <div class="checkbox-list">
                    <label class="checkbox-label"><input type="checkbox" value="Nike" class="brand-filter"> Nike</label>
                    <label class="checkbox-label"><input type="checkbox" value="Adidas" class="brand-filter"> Adidas</label>
                    <label class="checkbox-label"><input type="checkbox" value="Puma" class="brand-filter"> Puma</label>
                    <label class="checkbox-label"><input type="checkbox" value="New Balance" class="brand-filter"> New Balance</label>
                </div>
            </div>

            <div class="filter-group">
                <span class="filter-title">Categories</span>
                <div class="checkbox-list">
                    <label class="checkbox-label"><input type="checkbox" value="Athletic" class="category-filter"> Athletic</label>
                    <label class="checkbox-label"><input type="checkbox" value="Running" class="category-filter"> Running</label>
                    <label class="checkbox-label"><input type="checkbox" value="Lifestyle" class="category-filter"> Lifestyle</label>
                    <label class="checkbox-label"><input type="checkbox" value="Basketball" class="category-filter"> Basketball</label>
                </div>
            </div>

            <div class="filter-group">
                <span class="filter-title">Max Budget</span>
                <input type="range" id="priceRange" min="50" max="250" value="250" style="width:100%; accent-color:var(--color-secondary);">
                <div style="display:flex; justify-content:space-between; font-size:0.85rem; margin-top:0.5rem;">
                    <span>$50</span>
                    <strong id="priceValue">$250</strong>
                </div>
            </div>

            <div class="filter-group">
                <span class="filter-title">Color tones</span>
                <div class="swatch-row">
                    <div class="swatch-color" data-color="Red" style="background-color: #ff3b30;" title="Red"></div>
                    <div class="swatch-color" data-color="White" style="background-color: #ffffff;" title="White"></div>
                    <div class="swatch-color" data-color="Black" style="background-color: #000000;" title="Black"></div>
                    <div class="swatch-color" data-color="Green" style="background-color: #28cd41;" title="Green"></div>
                    <div class="swatch-color" data-color="Grey" style="background-color: #8e8e93;" title="Grey"></div>
                    <div class="swatch-color" data-color="Yellow" style="background-color: #ffcc00;" title="Yellow"></div>
                </div>
            </div>

            <div class="filter-group">
                <span class="filter-title">Min Rating</span>
                <div class="checkbox-list">
                    <label class="checkbox-label"><input type="radio" name="ratingFilter" value="4.8" class="rating-filter"> 4.8★ & up</label>
                    <label class="checkbox-label"><input type="radio" name="ratingFilter" value="4.5" class="rating-filter"> 4.5★ & up</label>
                </div>
            </div>

            <div class="filter-group">
                <span class="filter-title">US Sizes</span>
                <div class="checkbox-list" style="display:grid; grid-template-columns: repeat(3, 1fr); gap:0.5rem;">
                    <label class="checkbox-label" style="border:1px solid var(--color-border); padding: 0.25rem; justify-content:center; border-radius:var(--radius-sm);"><input type="checkbox" value="7" class="size-filter" style="display:none;">7</label>
                    <label class="checkbox-label" style="border:1px solid var(--color-border); padding: 0.25rem; justify-content:center; border-radius:var(--radius-sm);"><input type="checkbox" value="8" class="size-filter" style="display:none;">8</label>
                    <label class="checkbox-label" style="border:1px solid var(--color-border); padding: 0.25rem; justify-content:center; border-radius:var(--radius-sm);"><input type="checkbox" value="9" class="size-filter" style="display:none;">9</label>
                    <label class="checkbox-label" style="border:1px solid var(--color-border); padding: 0.25rem; justify-content:center; border-radius:var(--radius-sm);"><input type="checkbox" value="10" class="size-filter" style="display:none;">10</label>
                    <label class="checkbox-label" style="border:1px solid var(--color-border); padding: 0.25rem; justify-content:center; border-radius:var(--radius-sm);"><input type="checkbox" value="11" class="size-filter" style="display:none;">11</label>
                    <label class="checkbox-label" style="border:1px solid var(--color-border); padding: 0.25rem; justify-content:center; border-radius:var(--radius-sm);"><input type="checkbox" value="12" class="size-filter" style="display:none;">12</label>
                </div>
            </div>
        </aside>

        <section class="catalog-area" aria-label="Search results products grid">
            <div class="catalog-toolbar">
                <span style="color:var(--color-muted); font-size:0.95rem;">Interactive Live Filter Results</span>
                <select id="sortSelect" style="padding:0.5rem 1rem; border:1px solid var(--color-border); background-color:var(--color-card-bg); color:var(--color-text); font-weight:600; border-radius:var(--radius-sm);">
                    <option value="popularity">Sort By: Featured</option>
                    <option value="price-asc">Price: Low to High</option>
                    <option value="price-desc">Price: High to Low</option>
                    <option value="rating">Reviews: Highly Rated</option>
                </select>
            </div>

            <div class="catalog-grid" id="catalogGrid">
                </div>
        </section>
    </div>
</main>
<script src="js/filter.js"></script>
""" + get_footer()

# product.html
project_files['product.html'] = get_header("Product Details") + """
<main class="container" style="margin-top: 2rem;">
    <nav aria-label="Breadcrumb" style="margin-bottom: 2rem; font-size:0.9rem;">
        <ol style="display:flex; gap:0.5rem; color:var(--color-muted);">
            <li><a href="index.html">Home</a></li>
            <li>/</li>
            <li><a href="shop.html">Shop</a></li>
            <li>/</li>
            <li><a id="breadcrumbCategory" href="shop.html">Category</a></li>
            <li>/</li>
            <li id="breadcrumbName" style="color:var(--color-text); font-weight:600;">Product</li>
        </ol>
    </nav>

    <section class="product-hero">
        <div class="gallery-layout">
            <div class="thumbnails-list" id="thumbnailsList">
                </div>
            <div class="main-view-container">
                <img id="mainImg" src="" alt="Main Image view zoomed window">
            </div>
        </div>

        <div class="product-info-column" aria-label="Purchase parameters options">
            <span id="prodBrand" class="product-brand">BRAND NAME</span>
            <h1 id="prodTitle">Product Sneaker Title</h1>
            
            <div id="prodPrice" class="product-price-bar">$0.00</div>
            
            <p id="prodDesc" style="color:var(--color-muted); margin-bottom:2rem; line-height:1.7;">Product descriptions detailed segment details here.</p>

            <div class="product-options-row">
                <span class="option-heading">Available Colors</span>
                <div class="swatch-row" id="colorsWrapper"></div>
            </div>

            <div class="product-options-row">
                <span class="option-heading">Choose US Sizing</span>
                <div class="sizes-button-grid" id="sizesWrapper"></div>
            </div>

            <div style="margin-bottom: 2rem; font-weight:700;" id="stockStatusWrapper">
                Status: <span id="stockStatusLabel">In Stock</span>
            </div>

            <div style="display:flex; align-items:center; margin-bottom: 2rem;">
                <div class="qty-widget">
                    <button class="qty-btn" id="qtyMinus">-</button>
                    <input class="qty-input" type="text" value="1" id="qtyValue" readonly>
                    <button class="qty-btn" id="qtyPlus">+</button>
                </div>
                
                <button class="btn btn-primary" id="addToCartBtn">Add To Cart</button>
                <button class="btn btn-secondary" id="addToWishlistBtn" style="padding:0.8rem; margin-left:0.5rem;" aria-label="Add to wishlist">♥</button>
            </div>
        </div>
    </section>

    <section>
        <div class="tabs-navigation">
            <button class="tab-btn active" data-tab="tabSpecs">Specifications</button>
            <button class="tab-btn" data-tab="tabReviews">Customer Reviews</button>
        </div>

        <div class="tab-pane active" id="tabSpecs">
            <table class="specs-table">
                <tbody id="specsBody">
                    </tbody>
            </table>
        </div>

        <div class="tab-pane" id="tabReviews">
            <div class="reviews-grid">
                <div class="ratings-panel">
                    <h2 id="averageRatingText">0.0</h2>
                    <div style="color:var(--color-gold); font-size:1.5rem; margin-bottom: 0.5rem;">★★★★★</div>
                    <span id="totalReviewsText">0 Reviews</span>
                    
                    <div class="stars-distribution">
                        <div class="dist-row">
                            <span>5★</span>
                            <div class="dist-bar"><div class="dist-fill" id="distBar5"></div></div>
                        </div>
                        <div class="dist-row">
                            <span>4★</span>
                            <div class="dist-bar"><div class="dist-fill" id="distBar4"></div></div>
                        </div>
                        <div class="dist-row">
                            <span>3★</span>
                            <div class="dist-bar"><div class="dist-fill" id="distBar3"></div></div>
                        </div>
                        <div class="dist-row">
                            <span>2★</span>
                            <div class="dist-bar"><div class="dist-fill" id="distBar2"></div></div>
                        </div>
                        <div class="dist-row">
                            <span>1★</span>
                            <div class="dist-bar"><div class="dist-fill" id="distBar1"></div></div>
                        </div>
                    </div>
                </div>

                <div>
                    <h3 style="margin-bottom:1.5rem;">User Thoughts</h3>
                    <div id="reviewsList" style="margin-bottom: 3rem;">
                        </div>

                    <form id="reviewForm" style="border-top: 1px solid var(--color-border); padding-top:2rem;">
                        <h4 style="margin-bottom:1.5rem; text-transform:uppercase;">Add Your Verified Thoughts</h4>
                        <div class="form-grid" style="margin-bottom:1rem;">
                            <div class="form-group">
                                <label for="revName">Enter Name</label>
                                <input type="text" id="revName" required>
                            </div>
                            <div class="form-group">
                                <label for="revRating">Rating score</label>
                                <select id="revRating" style="background-color: var(--color-input-bg); border:1px solid var(--color-border); padding: 0.8rem; border-radius: var(--radius-sm); color:var(--color-text);">
                                    <option value="5">5 Stars (Excellent)</option>
                                    <option value="4">4 Stars (Great)</option>
                                    <option value="3">3 Stars (Average)</option>
                                    <option value="2">2 Stars (Bad)</option>
                                    <option value="1">1 Star (Horrible)</option>
                                </select>
                            </div>
                        </div>
                        <div class="form-group" style="margin-bottom:1.5rem;">
                            <label for="revComment">Review comment</label>
                            <textarea id="revComment" rows="4" style="width:100%; padding:0.8rem; background-color: var(--color-input-bg); border:1px solid var(--color-border); border-radius:var(--radius-sm); color:var(--color-text);" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">Post Review</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <section style="margin-top: 6rem;">
        <h2 class="section-title">RELATED EXCLUSIVES</h2>
        <div class="catalog-grid" id="relatedGrid"></div>
    </section>
</main>
<script src="js/product.js"></script>
""" + get_footer()

# cart.html
project_files['cart.html'] = get_header("Shopping Cart") + """
<main class="container">
    <h1 class="section-title" style="margin-top:2rem; text-align:left;">YOUR BASKET</h1>
    
    <div class="cart-layout" id="cartPageLayout">
        <section style="overflow-x:auto;" aria-label="Shopping Cart Items List">
            <table class="cart-items-table">
                <thead>
                    <tr>
                        <th style="width:50%;">Details</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Subtotal</th>
                        <th style="text-align: right;">Action</th>
                    </tr>
                </thead>
                <tbody id="cartTableBody">
                    </tbody>
            </table>
        </section>

        <aside class="cart-summary-card" aria-label="Basket Invoice Summary">
            <h3>ORDER SUMMARY</h3>
            <div class="summary-totals-list">
                <div class="summary-row">
                    <span>Subtotal</span>
                    <span id="summarySubtotal">$0.00</span>
                </div>
                <div id="summaryDiscountRow" style="display:flex; flex-direction:column; gap:0.5rem;"></div>
                
                <div class="summary-row">
                    <span>Estimated Shipping</span>
                    <span id="summaryShipping">$0.00</span>
                </div>
                <div class="summary-row">
                    <span>Tax (8%)</span>
                    <span id="summaryTax">$0.00</span>
                </div>
                <div class="summary-row summary-row-total">
                    <span>Grand Total</span>
                    <strong id="summaryTotal">$0.00</strong>
                </div>
            </div>

            <form id="couponForm" class="newsletter-form" style="margin-bottom: 2rem;">
                <input type="text" id="couponCode" placeholder="Enter PROMO (e.g. SNEAKER10)" aria-label="Promo code input" required>
                <button type="submit" style="background-color:var(--color-primary); color:var(--color-bg);">Apply</button>
            </form>

            <a href="checkout.html" class="btn btn-primary" style="width:100%;">Proceed To Checkout</a>
        </aside>
    </div>
</main>
<script src="js/cart.js"></script>
""" + get_footer()

# checkout.html
project_files['checkout.html'] = get_header("Secure Checkout") + """
<main class="container">
    <div class="checkout-layout">
        <section>
            <div class="checkout-steps" aria-label="Checkout Progression Steps">
                <div class="step-node active">
                    <div class="step-circle">1</div>
                    <span style="font-size:0.85rem; font-weight:600;">Shipping</span>
                </div>
                <div class="step-node">
                    <div class="step-circle">2</div>
                    <span style="font-size:0.85rem; font-weight:600;">Payment</span>
                </div>
                <div class="step-node">
                    <div class="step-circle">3</div>
                    <span style="font-size:0.85rem; font-weight:600;">Order Review</span>
                </div>
            </div>

            <div id="shippingStep" style="display:block;">
                <h2 style="margin-bottom:1.5rem;">1. SHIPMENT DESTINATION</h2>
                <form class="form-grid" onsubmit="event.preventDefault();">
                    <div class="form-group">
                        <label for="shpFname">First Name *</label>
                        <input type="text" id="shpFname" required>
                    </div>
                    <div class="form-group">
                        <label for="shpLname">Last Name *</label>
                        <input type="text" id="shpLname" required>
                    </div>
                    <div class="form-group form-full">
                        <label for="shpAddr">Street Address *</label>
                        <input type="text" id="shpAddr" placeholder="Apt, Suite, House details" required>
                    </div>
                    <div class="form-group">
                        <label for="shpCity">City *</label>
                        <input type="text" id="shpCity" required>
                    </div>
                    <div class="form-group">
                        <label for="shpZip">ZIP Code *</label>
                        <input type="text" id="shpZip" required>
                    </div>
                    <div class="form-group">
                        <label for="shpCountry">Country *</label>
                        <select id="shpCountry">
                            <option value="United States">United States</option>
                            <option value="United Kingdom">United Kingdom</option>
                            <option value="Canada">Canada</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="shpEmail">Email Address *</label>
                        <input type="email" id="shpEmail" required>
                    </div>
                    <div class="form-group form-full">
                        <label for="shpPhone">Phone Number *</label>
                        <input type="tel" id="shpPhone" required>
                    </div>

                    <div class="form-full" style="margin-top:1.5rem;">
                        <span style="font-weight:700; font-size:0.9rem; text-transform:uppercase; display:block; margin-bottom:1rem;">Delivery Speeds</span>
                        <div class="checkbox-list">
                            <label class="checkbox-label" style="border:1px solid var(--color-border); padding: 1rem; border-radius: var(--radius-md);">
                                <input type="radio" name="shippingSpeed" value="standard" checked>
                                <div>
                                    <strong>Standard Ground Carrier (FREE over $150, or flat $15.00)</strong><br>
                                    <span style="color:var(--color-muted); font-size:0.85rem;">Estimated delivery duration is 3-5 business days.</span>
                                </div>
                            </label>
                            <label class="checkbox-label" style="border:1px solid var(--color-border); padding: 1rem; border-radius: var(--radius-md); margin-top:0.5rem;">
                                <input type="radio" name="shippingSpeed" value="express">
                                <div>
                                    <strong>Express Air Delivery Service (Flat $15.00)</strong><br>
                                    <span style="color:var(--color-muted); font-size:0.85rem;">Estimated delivery duration is 1-2 business days.</span>
                                </div>
                            </label>
                        </div>
                    </div>

                    <div class="form-full" style="margin-top:2rem; text-align:right;">
                        <button type="button" class="btn btn-primary" onclick="nextStep(1)">Go to Payment</button>
                    </div>
                </form>
            </div>

            <div id="paymentStep" style="display:none;">
                <h2 style="margin-bottom:1.5rem;">2. PAYMENT & CREDIT CARD</h2>
                
                <div class="card-preview-wrapper" aria-hidden="true">
                    <div class="credit-card-inner">
                        <div class="card-front">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <div class="card-chip"></div>
                                <div class="card-logo">KicksElite</div>
                            </div>
                            <div class="card-digits" id="previewCardNum">•••• •••• •••• ••••</div>
                            <div class="card-info-row">
                                <div>
                                    <div style="font-size:0.6rem; opacity:0.6;">Cardholder</div>
                                    <div id="previewCardName" style="font-weight:600;">CARDHOLDER NAME</div>
                                </div>
                                <div style="text-align:right;">
                                    <div style="font-size:0.6rem; opacity:0.6;">Expires</div>
                                    <div id="previewCardExp" style="font-weight:600;">MM/YY</div>
                                </div>
                            </div>
                        </div>
                        <div class="card-back">
                            <div class="card-signature"></div>
                            <div class="card-cvv-strip">
                                <div style="font-size:0.6rem; opacity:0.6; color:white; text-align:right; margin-bottom:2px;">CVV</div>
                                <span id="previewCardCvv" style="font-weight:700; font-family:monospace; background:white; padding:3px 10px; border-radius:3px;">•••</span>
                            </div>
                        </div>
                    </div>
                </div>

                <form class="form-grid" onsubmit="event.preventDefault();">
                    <div class="form-group form-full">
                        <label for="cardNum">Credit Card Number *</label>
                        <input type="text" id="cardNum" maxlength="19" placeholder="4111 2222 3333 4444" required>
                    </div>
                    <div class="form-group form-full">
                        <label for="cardName">Cardholder Printed Name *</label>
                        <input type="text" id="cardName" placeholder="JOHN DOE" required>
                    </div>
                    <div class="form-group">
                        <label for="cardExp">Expiration Dates *</label>
                        <input type="text" id="cardExp" maxlength="5" placeholder="MM/YY" required>
                    </div>
                    <div class="form-group">
                        <label for="cardCvv">CVV Code *</label>
                        <input type="password" id="cardCvv" maxlength="3" placeholder="123" required>
                    </div>

                    <div class="form-full" style="margin-top:2rem; display:flex; justify-content:space-between;">
                        <button type="button" class="btn btn-secondary" onclick="prevStep(0)">Back to Shipping</button>
                        <button type="button" class="btn btn-primary" onclick="nextStep(2)">Confirm Orders</button>
                    </div>
                </form>
            </div>

            <div id="reviewStep" style="display:none;">
                <h2 style="margin-bottom:1.5rem;">3. ORDER INVOICE CONFIRMATION</h2>
                <div style="background-color: var(--color-light-bg); padding:2rem; border-radius:var(--radius-md); border:1px solid var(--color-border); margin-bottom: 2rem;">
                    <h3 style="margin-bottom:1rem; font-size:1.1rem; text-transform:uppercase;">Shipment Destination Address</h3>
                    <div id="revAddressSummary" style="color:var(--color-muted); line-height:1.6;"></div>
                </div>

                <p style="font-size:0.9rem; color:var(--color-muted); margin-bottom:2rem;">By clicking "Place Order" you authorize KicksElite to securely process your verified transaction details using local client mock variables.</p>

                <div style="display:flex; justify-content:space-between;">
                    <button type="button" class="btn btn-secondary" onclick="prevStep(1)">Back to Payment</button>
                    <button type="button" class="btn btn-primary" onclick="placeOrderSubmit()" style="background-color:var(--color-success); border-color:var(--color-success);">Place Order</button>
                </div>
            </div>
        </section>

        <aside class="cart-summary-card" style="height:fit-content; position:sticky; top:100px;" aria-label="Invoice summary calculation details">
            <h3>ORDER DETAIL</h3>
            <div id="checkoutSummaryItems" style="margin-top:1.5rem;"></div>
            
            <div class="summary-totals-list" style="margin-top: 1.5rem; border-top:1px solid var(--color-border); padding-top:1rem;">
                <div class="summary-row">
                    <span>Subtotal</span>
                    <span id="summarySubtotal">$0.00</span>
                </div>
                <div class="summary-row">
                    <span>Shipping</span>
                    <span id="summaryShipping">$0.00</span>
                </div>
                <div class="summary-row">
                    <span>Tax (8%)</span>
                    <span id="summaryTax">$0.00</span>
                </div>
                <div class="summary-row summary-row-total">
                    <span>Invoice Total</span>
                    <strong id="summaryTotal">$0.00</strong>
                </div>
            </div>
        </aside>
    </div>
</main>

<div class="loading-overlay" id="checkoutLoaderOverlay">
    <div class="spinner"></div>
    <h2 id="loaderStatusMessage">Securing payments authorizations gateways...</h2>
    <p style="color:var(--color-muted); font-size:0.9rem; margin-top:0.5rem;">Do not refresh or click back buttons.</p>
</div>

<script src="js/checkout.js"></script>
""" + get_footer()

# success.html
project_files['success.html'] = get_header("Order Completed!") + """
<main class="container" style="text-align:center; padding: 5rem 0;">
    <div style="width: 80px; height: 80px; background-color: var(--color-success); color: white; font-size:3rem; border-radius: var(--radius-circle); display:inline-flex; align-items:center; justify-content:center; margin-bottom: 2rem;">✓</div>
    
    <h1>ORDER CONFIRMED & REGISTERED!</h1>
    <p style="color:var(--color-muted); margin-bottom: 3rem;">Thank you for your purchase. Your premium package is registered in our database system.</p>

    <section class="cart-summary-card" style="max-width: 600px; margin: 0 auto 3rem auto; text-align: left;" aria-label="Order receipts specifics">
        <h3 style="border-bottom:1px solid var(--color-border); padding-bottom: 0.5rem; margin-bottom: 1.5rem;">RECEIPT DETAILS</h3>
        <div style="display:flex; justify-content:space-between; margin-bottom:0.8rem; font-size:0.95rem;">
            <span>Order Number:</span>
            <strong id="recId">ORD-000000</strong>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:0.8rem; font-size:0.95rem;">
            <span>Estimated Shipment Courier:</span>
            <strong>Standard Ground (Fastest)</strong>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:0.8rem; font-size:0.95rem;">
            <span>Delivery Timeline Date:</span>
            <strong id="recDate">3-5 business days</strong>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:0.8rem; font-size:0.95rem; border-top:1px solid var(--color-border); padding-top:0.8rem;">
            <strong>Invoice Total Paid:</strong>
            <strong id="recBill" style="font-size:1.2rem; color:var(--color-success);">$0.00</strong>
        </div>
    </section>

    <section class="cart-summary-card" style="max-width: 800px; margin