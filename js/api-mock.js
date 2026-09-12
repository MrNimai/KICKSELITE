/* RAW JSON DATABASE OBJECT SCHEMA */
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