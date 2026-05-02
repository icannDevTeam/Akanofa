"""
One-shot site generator for Akanofa.
Creates: index.html, services.html, about.html, why-us.html, contact.html
Run: python3 build_pages.py
"""
from pathlib import Path
import math

ROOT = Path(__file__).parent
WHATSAPP_NUMBER = "6282385449541"
EMAIL = "info@akanofa.com"

# Generate Archimedean spiral path (2 turns, inward)
def _spiral_path():
    pts = []
    for i in range(0, 721, 4):  # 0..720 deg
        theta = math.radians(i - 90)  # start from top
        r = 240 - (i / 720.0) * 215  # 240 -> 25
        x = 320 + r * math.cos(theta)
        y = 320 + r * math.sin(theta)
        pts.append(f"{x:.1f},{y:.1f}")
    return "M" + pts[0] + " L" + " L".join(pts[1:])

SPIRAL_D = _spiral_path()

def _spiral_node_pos(deg, r):
    theta = math.radians(deg - 90)
    return 320 + r * math.cos(theta), 320 + r * math.sin(theta)

# ============================================================
# Shared HEAD (with security headers via meta + Tailwind config + styles)
# ============================================================
def head(title, description="Intelligent software, built for your business — Akanofa builds AI, cloud, mobile, security, and data solutions tailored to your business."):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <meta name="theme-color" content="#0B3D2E">
    <!-- Security headers (defense-in-depth; primary headers should be set by host) -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com https://unpkg.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com data:; img-src 'self' data: https:; connect-src 'self' https://formsubmit.co; frame-src https://www.google.com; form-action 'self' https://formsubmit.co; base-uri 'self'; object-src 'none'; upgrade-insecure-requests;">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">
    <meta http-equiv="Permissions-Policy" content="camera=(), microphone=(), geolocation=(), interest-cohort=()">
    <title>{title}</title>
    <link rel="icon" type="image/png" href="images/Logo.png">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'brand-dark': '#0B3D2E',
                        'brand-green': '#14694A',
                        'brand-light': '#1A8C5E',
                        'brand-yellow': '#F5E6A3',
                        'brand-yellow-light': '#FBF4D8',
                        'brand-cream': '#FFFDF5',
                    }},
                    fontFamily: {{ 'display': ['Inter', 'system-ui', 'sans-serif'] }}
                }}
            }}
        }}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', sans-serif; }}
        html {{ scroll-behavior: smooth; }}
        .gradient-hero {{ background: linear-gradient(155deg, #0B3D2E 0%, #14694A 40%, #1A8C5E 70%, #0B3D2E 100%); }}
        .gradient-card:hover {{ transform: translateY(-6px); box-shadow: 0 25px 50px -12px rgba(11, 61, 46, 0.25); }}
        .gradient-card {{ transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); }}
        .text-gradient {{ background: linear-gradient(135deg, #1A8C5E, #F5E6A3); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }}
        .dot-pattern {{ background-image: radial-gradient(circle, #14694A 1px, transparent 1px); background-size: 30px 30px; opacity: 0.06; }}
        .float-animation {{ animation: float 6s ease-in-out infinite; }}
        .float-animation-delayed {{ animation: float 6s ease-in-out 2s infinite; }}
        @keyframes float {{ 0%,100%{{transform:translateY(0)}} 50%{{transform:translateY(-20px)}} }}
        @keyframes fadeInUp {{ from{{opacity:0;transform:translateY(40px)}} to{{opacity:1;transform:translateY(0)}} }}
        .animate-fade-in-up {{ animation: fadeInUp 0.8s ease-out forwards; }}
        .animate-fade-in-up-delay-1 {{ animation: fadeInUp 0.8s 0.2s ease-out forwards; opacity: 0; }}
        .animate-fade-in-up-delay-2 {{ animation: fadeInUp 0.8s 0.4s ease-out forwards; opacity: 0; }}
        .animate-fade-in-up-delay-3 {{ animation: fadeInUp 0.8s 0.6s ease-out forwards; opacity: 0; }}
        @keyframes pulse-ring {{ 0%{{transform:scale(1);opacity:.4}} 100%{{transform:scale(1.5);opacity:0}} }}
        .pulse-ring::before {{ content:''; position:absolute; inset:-8px; border-radius:50%; border:2px solid #F5E6A3; animation: pulse-ring 2s ease-out infinite; }}
        .nav-blur {{ backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); }}
        .counter-value {{ font-variant-numeric: tabular-nums; }}
        .marquee-track {{ display: flex; animation: marquee 30s linear infinite; }}
        @keyframes marquee {{ 0%{{transform:translateX(0)}} 100%{{transform:translateX(-50%)}} }}
        .service-icon-wrap {{ transition: all 0.3s ease; }}
        .gradient-card:hover .service-icon-wrap {{ background: #F5E6A3; color: #0B3D2E; }}
        .mobile-menu {{ transform: translateX(100%); transition: transform 0.3s ease; }}
        .mobile-menu.active {{ transform: translateX(0); }}
        ::selection {{ background: #F5E6A3; color: #0B3D2E; }}
        /* Modal */
        .modal-backdrop {{ background: rgba(11,61,46,0.75); backdrop-filter: blur(4px); }}
        .modal-enter {{ animation: modalIn 0.25s ease-out; }}
        @keyframes modalIn {{ from{{opacity:0;transform:scale(.95) translateY(10px)}} to{{opacity:1;transform:scale(1) translateY(0)}} }}
        /* Spiral process */
        .spiral-svg .spiral-path {{ stroke-dasharray: 2400; stroke-dashoffset: 2400; transition: stroke-dashoffset 2.5s ease-out; }}
        .spiral-svg.in-view .spiral-path {{ stroke-dashoffset: 0; }}
        .spiral-node {{ opacity: 0; transform: scale(.6); transform-origin: center; transition: opacity .6s ease, transform .6s cubic-bezier(.34,1.56,.64,1); }}
        .spiral-svg.in-view .spiral-node {{ opacity: 1; transform: scale(1); }}
        .spiral-svg.in-view .spiral-node.n1 {{ transition-delay: .4s; }}
        .spiral-svg.in-view .spiral-node.n2 {{ transition-delay: .8s; }}
        .spiral-svg.in-view .spiral-node.n3 {{ transition-delay: 1.2s; }}
        .spiral-svg.in-view .spiral-node.n4 {{ transition-delay: 1.6s; }}
        .spiral-svg.in-view .spiral-node.n5 {{ transition-delay: 2.0s; }}
        .spiral-svg.in-view .spiral-node.n6 {{ transition-delay: 2.4s; }}
        .process-card {{ opacity: 0; transform: translateY(20px); transition: all .6s cubic-bezier(.4,0,.2,1); }}
        .process-card.in-view {{ opacity: 1; transform: translateY(0); }}
        /* Reveal */
        .reveal {{ opacity: 0; transform: translateY(30px); transition: opacity .7s ease, transform .7s cubic-bezier(.4,0,.2,1); }}
        .reveal.in-view {{ opacity: 1; transform: translateY(0); }}
        .reveal-left {{ opacity: 0; transform: translateX(-40px); transition: opacity .7s ease, transform .7s cubic-bezier(.4,0,.2,1); }}
        .reveal-left.in-view {{ opacity: 1; transform: translateX(0); }}
        .reveal-right {{ opacity: 0; transform: translateX(40px); transition: opacity .7s ease, transform .7s cubic-bezier(.4,0,.2,1); }}
        .reveal-right.in-view {{ opacity: 1; transform: translateX(0); }}
        /* Glow */
        .glow-ring {{ position: relative; }}
        .glow-ring::after {{ content:''; position:absolute; inset:-2px; border-radius:inherit; padding:2px; background: linear-gradient(135deg, #F5E6A3, #1A8C5E, #F5E6A3); -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); -webkit-mask-composite: xor; mask-composite: exclude; opacity: 0; transition: opacity .4s; }}
        .glow-ring:hover::after {{ opacity: 1; }}
        /* Map frame */
        .map-frame {{ filter: grayscale(.2) contrast(1.05); transition: filter .4s; }}
        .map-frame:hover {{ filter: grayscale(0) contrast(1); }}
        /* Tilt cards */
        .tilt-card {{ transition: transform .5s cubic-bezier(.4,0,.2,1), box-shadow .5s; transform-style: preserve-3d; }}
        .tilt-card:hover {{ transform: perspective(1000px) rotateX(2deg) rotateY(-3deg) translateY(-6px); box-shadow: 0 30px 60px -20px rgba(11,61,46,.35); }}
        /* Pulsing dot */
        .live-dot {{ position: relative; width: 10px; height: 10px; border-radius: 50%; background: #22c55e; }}
        .live-dot::before {{ content:''; position:absolute; inset:-4px; border-radius:50%; background: #22c55e; opacity:.4; animation: livePulse 1.8s ease-out infinite; }}
        @keyframes livePulse {{ 0%{{transform:scale(.6);opacity:.6}} 100%{{transform:scale(2);opacity:0}} }}
    </style>
</head>
<body class="bg-white text-gray-900 overflow-x-hidden">
"""

# ============================================================
# NAV (with active page highlighting via data-page)
# ============================================================
def nav(active=""):
    def link(href, label, page_key):
        cls_active = "text-brand-green" if active == page_key else "text-brand-dark/75 hover:text-brand-green"
        return f'<a href="{href}" class="nav-link {cls_active} transition-colors text-sm font-semibold">{label}</a>'

    def mlink(href, label, page_key):
        cls_active = "text-brand-yellow" if active == page_key else "text-white hover:text-brand-yellow"
        return f'<a href="{href}" class="mobile-link {cls_active} text-2xl font-medium transition-colors">{label}</a>'

    return f"""    <!-- Navigation -->
    <nav id="navbar" class="fixed top-0 left-0 right-0 z-50 bg-white/70 nav-blur border-b border-white/40 shadow-sm shadow-brand-dark/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20 gap-6">
                <!-- Logo + Wordmark -->
                <a href="/" class="flex items-center gap-2 group shrink-0">
                    <img src="images/Logo.png" alt="Akanofa" class="h-16 w-auto group-hover:scale-110 transition-transform drop-shadow-sm">
                    <span class="text-brand-dark font-extrabold text-lg tracking-tight hidden sm:inline">Akanofa</span>
                </a>

                <!-- Desktop Menu (centered) -->
                <div class="hidden md:flex items-center gap-14 lg:gap-20 mx-auto">
                    {link("/", "Home", "home")}
                    {link("services", "Services", "services")}
                    {link("about", "About", "about")}
                    {link("why-us", "Why Us", "why-us")}
                    {link("contact", "Contact", "contact")}
                </div>

                <!-- Desktop CTA -->
                <button type="button" data-open-quote class="hidden md:inline-flex shrink-0 bg-brand-dark text-white px-6 py-2.5 rounded-full text-sm font-semibold hover:bg-brand-green transition-all duration-300 hover:shadow-lg shadow-md shadow-brand-dark/20">Get Started</button>

                <!-- Mobile Menu Toggle -->
                <button id="menuToggle" class="md:hidden text-brand-dark p-2" aria-label="Open menu">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>
            </div>
        </div>
    </nav>

    <!-- Mobile Menu -->
    <div id="mobileMenu" class="mobile-menu fixed inset-0 z-[60] bg-brand-dark">
        <div class="flex justify-between items-center p-6">
            <a href="/" class="flex items-center">
                <img src="images/Logo.png" alt="Akanofa" class="h-9 w-auto">
            </a>
            <button id="menuClose" class="text-white p-2" aria-label="Close menu">
                <i data-lucide="x" class="w-6 h-6"></i>
            </button>
        </div>
        <div class="flex flex-col items-center gap-6 mt-16">
            {mlink("/", "Home", "home")}
            {mlink("services", "Services", "services")}
            {mlink("about", "About", "about")}
            {mlink("why-us", "Why Us", "why-us")}
            {mlink("contact", "Contact", "contact")}
            <button type="button" data-open-quote class="mt-8 bg-brand-yellow text-brand-dark px-8 py-3 rounded-full text-lg font-semibold hover:bg-white transition-all">Get Started</button>
        </div>
    </div>
"""

# ============================================================
# Page sub-hero (used by all subpages)
# ============================================================
def subhero(eyebrow, title_html, subtitle):
    return f"""    <!-- Page Hero -->
    <section class="gradient-hero relative pt-32 pb-20 overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="absolute top-20 right-10 w-72 h-72 bg-brand-yellow/10 rounded-full blur-3xl float-animation"></div>
        <div class="absolute bottom-10 left-10 w-80 h-80 bg-brand-yellow/5 rounded-full blur-3xl float-animation-delayed"></div>
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
            <span class="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full px-4 py-1.5 text-brand-yellow text-sm font-medium mb-5">
                <span class="w-2 h-2 bg-brand-yellow rounded-full animate-pulse"></span>
                {eyebrow}
            </span>
            <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-5">{title_html}</h1>
            <p class="text-lg text-white/70 max-w-2xl mx-auto">{subtitle}</p>
        </div>
        <div class="absolute bottom-0 left-0 right-0 leading-none">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 80" fill="#ffffff" preserveAspectRatio="none" class="w-full h-12 sm:h-16">
                <path d="M0,40L60,42C120,44,240,48,360,46C480,44,600,36,720,34C840,32,960,36,1080,40C1200,44,1320,48,1380,50L1440,52L1440,80L0,80Z"></path>
            </svg>
        </div>
    </section>
"""

# ============================================================
# CTA strip (reusable)
# ============================================================
CTA_STRIP = """    <section class="bg-brand-dark py-16 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern" style="opacity:.04"></div>
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
            <h2 class="text-3xl sm:text-4xl font-extrabold text-white mb-4">Ready to start your project?</h2>
            <p class="text-white/60 mb-8 max-w-xl mx-auto">Tell us what you're building. We'll respond within 24 hours.</p>
            <div class="flex flex-col sm:flex-row justify-center gap-4">
                <button type="button" data-open-quote class="bg-brand-yellow text-brand-dark px-8 py-4 rounded-full font-semibold hover:bg-white transition-all duration-300 hover:shadow-xl">
                    Request a Quote
                </button>
                <a href="contact.html" class="border-2 border-white/30 text-white px-8 py-4 rounded-full font-semibold hover:bg-white/10 transition-all duration-300">
                    Contact Us
                </a>
            </div>
        </div>
    </section>
"""

# ============================================================
# FOOTER
# ============================================================
FOOTER = f"""    <!-- Footer -->
    <footer class="bg-brand-dark pt-16 pb-8 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern" style="opacity:0.02;"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
                <div class="lg:col-span-1">
                    <a href="/" class="flex items-center gap-2 mb-4">
                        <img src="images/Logo.png" alt="Akanofa" class="h-10 w-auto">
                        <span class="text-xl font-bold text-white">Akanofa</span>
                    </a>
                    <p class="text-white/40 text-sm leading-relaxed mb-4">Intelligent software, built for your business. Being your technology company is our one objective.</p>
                    <div class="text-white/35 text-xs leading-relaxed mb-5 space-y-0.5">
                        <div class="text-white/60 font-semibold">PT Teknologi Akanofa Mandala</div>
                        <div>Infiniti Office, Bellezza BSA Lt. 1 Unit 106</div>
                        <div>Jl. Letjen Soepeno, Kebayoran Lama Utara</div>
                        <div>Kebayoran Lama, Jakarta Selatan 12210</div>
                        <div>Tel: <a href="tel:+622158905002" class="hover:text-brand-yellow">021-58905002</a></div>
                    </div>
                    <div class="flex gap-3">
                        <a href="#" rel="noopener noreferrer" aria-label="LinkedIn" class="w-10 h-10 bg-white/5 rounded-lg flex items-center justify-center text-white/50 hover:bg-brand-yellow hover:text-brand-dark transition-all duration-300"><i data-lucide="linkedin" class="w-4 h-4"></i></a>
                        <a href="#" rel="noopener noreferrer" aria-label="Twitter" class="w-10 h-10 bg-white/5 rounded-lg flex items-center justify-center text-white/50 hover:bg-brand-yellow hover:text-brand-dark transition-all duration-300"><i data-lucide="twitter" class="w-4 h-4"></i></a>
                        <a href="#" rel="noopener noreferrer" aria-label="GitHub" class="w-10 h-10 bg-white/5 rounded-lg flex items-center justify-center text-white/50 hover:bg-brand-yellow hover:text-brand-dark transition-all duration-300"><i data-lucide="github" class="w-4 h-4"></i></a>
                        <a href="#" rel="noopener noreferrer" aria-label="Instagram" class="w-10 h-10 bg-white/5 rounded-lg flex items-center justify-center text-white/50 hover:bg-brand-yellow hover:text-brand-dark transition-all duration-300"><i data-lucide="instagram" class="w-4 h-4"></i></a>
                    </div>
                </div>
                <div>
                    <h4 class="text-white font-semibold mb-4">Services</h4>
                    <ul class="space-y-3">
                        <li><a href="services.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">AI &amp; Machine Learning</a></li>
                        <li><a href="services.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">Cloud Solutions</a></li>
                        <li><a href="services.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">Mobile Development</a></li>
                        <li><a href="services.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">Cybersecurity</a></li>
                        <li><a href="services.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">Data Engineering</a></li>
                        <li><a href="services.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">DevOps &amp; Automation</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-semibold mb-4">Company</h4>
                    <ul class="space-y-3">
                        <li><a href="about.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">About Us</a></li>
                        <li><a href="why-us.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">Why Choose Us</a></li>
                        <li><a href="contact.html" class="text-white/40 hover:text-brand-yellow transition-colors text-sm">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-semibold mb-4">Stay Updated</h4>
                    <p class="text-white/40 text-sm mb-4">Get the latest insights on technology trends.</p>
                    <form id="newsletterForm" action="https://formsubmit.co/{EMAIL}" method="POST" class="flex gap-2" autocomplete="off">
                        <input type="hidden" name="_subject" value="New Newsletter Subscription">
                        <input type="hidden" name="_template" value="table">
                        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
                        <input type="email" name="Subscriber Email" required maxlength="120" autocomplete="email" class="flex-1 bg-white/5 border border-white/10 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/30 focus:border-brand-yellow focus:ring-1 focus:ring-brand-yellow outline-none transition-all" placeholder="Your email">
                        <button type="submit" class="bg-brand-yellow text-brand-dark px-4 py-2.5 rounded-lg text-sm font-semibold hover:bg-white transition-all duration-300 shrink-0" aria-label="Subscribe">
                            <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </button>
                    </form>
                    <div id="newsletterSuccess" class="hidden text-brand-yellow text-sm mt-2">&#10003; Subscribed!</div>
                </div>
            </div>
            <div class="border-t border-white/10 pt-8 flex flex-col sm:flex-row justify-between items-center gap-4">
                <p class="text-white/30 text-sm">&copy; 2026 PT Teknologi Akanofa Mandala. All rights reserved. <span class="hidden sm:inline">&middot; KBLI 58200 (Software Publishing) &middot; PMDN</span></p>
                <div class="flex gap-6">
                    <a href="#" class="text-white/30 hover:text-brand-yellow transition-colors text-sm">Privacy Policy</a>
                    <a href="#" class="text-white/30 hover:text-brand-yellow transition-colors text-sm">Terms of Service</a>
                    <a href="#" class="text-white/30 hover:text-brand-yellow transition-colors text-sm">Cookies</a>
                </div>
            </div>
        </div>
    </footer>
"""

# ============================================================
# Floating widgets + Modal
# ============================================================
FLOATING = f"""    <!-- Back to Top -->
    <button id="backToTop" class="fixed bottom-24 left-6 w-12 h-12 bg-brand-dark text-brand-yellow rounded-full shadow-lg flex items-center justify-center hover:bg-brand-green transition-all duration-300 opacity-0 pointer-events-none z-40" aria-label="Back to top">
        <i data-lucide="chevron-up" class="w-6 h-6"></i>
    </button>

    <!-- Floating WhatsApp (bottom-left) -->
    <a id="whatsappBtn" href="https://wa.me/{WHATSAPP_NUMBER}?text=Hi%20Akanofa%2C%20I%27d%20like%20to%20learn%20more%20about%20your%20services." target="_blank" rel="noopener noreferrer" class="fixed bottom-6 left-6 z-40 group w-14 h-14 bg-[#25D366] text-white rounded-full shadow-xl flex items-center justify-center hover:scale-110 transition-transform" aria-label="Chat on WhatsApp">
        <span class="absolute inset-0 rounded-full bg-[#25D366] animate-ping opacity-30"></span>
        <svg class="w-7 h-7 relative" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.817 11.817 0 0 1 8.413 3.488 11.824 11.824 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.51 5.26l.6.953-1 3.648 3.748-.982.631.422zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413z"/>
        </svg>
    </a>

    <!-- Floating Chatbot (bottom-right) -->
    <div class="fixed bottom-6 right-6 z-40 flex flex-col items-end gap-3">
        <div id="chatbotWindow" class="hidden w-80 max-w-[calc(100vw-3rem)] bg-white rounded-2xl shadow-2xl border border-gray-100 overflow-hidden flex-col" style="max-height: 480px;">
            <div class="bg-gradient-to-r from-brand-dark to-brand-green p-4 flex items-center gap-3">
                <div class="w-10 h-10 bg-white rounded-full flex items-center justify-center shrink-0 overflow-hidden ring-2 ring-white/40">
                    <img src="images/Logo.png" alt="Akanofa" class="w-full h-full object-contain">
                </div>
                <div class="flex-1">
                    <div class="text-white font-semibold text-sm">Akanofa Assistant</div>
                    <div class="text-white/60 text-xs flex items-center gap-1">
                        <span class="w-2 h-2 bg-green-400 rounded-full"></span> Online now
                    </div>
                </div>
                <button id="chatbotClose" class="text-white/70 hover:text-white p-1" aria-label="Close chat">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>
            <div id="chatbotMessages" class="flex-1 overflow-y-auto p-4 space-y-3 bg-brand-cream" style="min-height: 240px; max-height: 280px;"></div>
            <div class="p-3 border-t border-gray-100 bg-white">
                <div id="chatbotQuickReplies" class="flex flex-wrap gap-2 mb-3"></div>
                <a href="https://wa.me/{WHATSAPP_NUMBER}?text=Hi%20Akanofa%2C%20I%27d%20like%20to%20talk%20to%20a%20human." target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 w-full bg-brand-green text-white py-2.5 rounded-lg text-sm font-semibold hover:bg-brand-dark transition-colors">
                    <i data-lucide="message-circle" class="w-4 h-4"></i>
                    Talk to a human on WhatsApp
                </a>
            </div>
        </div>
        <button id="chatbotToggle" class="group w-16 h-16 bg-white rounded-full shadow-2xl shadow-brand-dark/30 flex items-center justify-center hover:scale-110 transition-all relative ring-2 ring-brand-green/30 hover:ring-brand-green overflow-hidden" aria-label="Open chat assistant">
            <span class="absolute inset-0 rounded-full bg-brand-green/20 animate-ping opacity-40"></span>
            <span class="absolute -top-0.5 -right-0.5 w-3.5 h-3.5 bg-green-400 rounded-full ring-2 ring-white z-10"></span>
            <img src="images/Logo.png" alt="Akanofa AI" class="w-full h-full object-contain relative p-1" id="chatbotIconOpen">
            <i data-lucide="x" class="w-6 h-6 hidden text-brand-dark" id="chatbotIconClose"></i>
        </button>
    </div>
"""

QUOTE_MODAL = f"""    <!-- Get Started / Quote Modal -->
    <div id="quoteModal" class="hidden fixed inset-0 z-[100] items-center justify-center p-4 modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="quoteModalTitle">
        <div class="modal-enter bg-white rounded-2xl shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto relative">
            <div class="sticky top-0 bg-gradient-to-r from-brand-dark to-brand-green p-6 flex items-center justify-between z-10">
                <div>
                    <h3 id="quoteModalTitle" class="text-white text-xl font-bold">Let's Get Started</h3>
                    <p class="text-white/70 text-sm mt-1">Tell us about your project — we reply within 24 hours.</p>
                </div>
                <button type="button" id="quoteModalClose" class="text-white/80 hover:text-white p-2" aria-label="Close">
                    <i data-lucide="x" class="w-6 h-6"></i>
                </button>
            </div>
            <div class="p-6">
                <form id="quoteForm" action="https://formsubmit.co/{EMAIL}" method="POST" class="space-y-4" autocomplete="on">
                    <input type="hidden" name="_subject" value="New Quote Request from Akanofa Website">
                    <input type="hidden" name="_template" value="table">
                    <input type="hidden" name="_captcha" value="true">
                    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
                    <div class="grid sm:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-medium text-brand-dark mb-1.5">Full Name</label>
                            <input type="text" name="Name" required maxlength="100" autocomplete="name" class="w-full px-4 py-2.5 rounded-xl border border-gray-200 bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none text-brand-dark" placeholder="Your name">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-brand-dark mb-1.5">Email</label>
                            <input type="email" name="Email" required maxlength="120" autocomplete="email" class="w-full px-4 py-2.5 rounded-xl border border-gray-200 bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none text-brand-dark" placeholder="you@company.com">
                        </div>
                    </div>
                    <div class="grid sm:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-medium text-brand-dark mb-1.5">Company</label>
                            <input type="text" name="Company" maxlength="100" autocomplete="organization" class="w-full px-4 py-2.5 rounded-xl border border-gray-200 bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none text-brand-dark" placeholder="Optional">
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-brand-dark mb-1.5">Phone / WhatsApp</label>
                            <input type="tel" name="Phone" maxlength="30" autocomplete="tel" pattern="[0-9+\\-\\s()]*" class="w-full px-4 py-2.5 rounded-xl border border-gray-200 bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none text-brand-dark" placeholder="Optional">
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-brand-dark mb-1.5">Service of Interest</label>
                        <select name="Service" required class="w-full px-4 py-2.5 rounded-xl border border-gray-200 bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none text-brand-dark">
                            <option value="" disabled selected>Choose a service</option>
                            <option>AI &amp; Machine Learning</option>
                            <option>Cloud Solutions</option>
                            <option>Mobile Development</option>
                            <option>Cybersecurity</option>
                            <option>Data Engineering</option>
                            <option>DevOps &amp; Automation</option>
                            <option>Other / Not sure yet</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-brand-dark mb-1.5">Project Brief</label>
                        <textarea name="Project Brief" rows="3" required maxlength="2000" class="w-full px-4 py-2.5 rounded-xl border border-gray-200 bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none text-brand-dark resize-none" placeholder="What are you trying to build or solve?"></textarea>
                    </div>
                    <button type="submit" class="w-full bg-brand-dark text-white py-3.5 rounded-xl font-semibold hover:bg-brand-green transition-all duration-300 flex items-center justify-center gap-2 group">
                        Send Request
                        <i data-lucide="send" class="w-5 h-5 group-hover:translate-x-1 transition-transform"></i>
                    </button>
                    <p class="text-xs text-gray-400 text-center">By submitting, you agree to be contacted by Akanofa. We never share your info.</p>
                </form>
                <div id="quoteSuccess" class="hidden text-center py-10">
                    <div class="w-16 h-16 bg-brand-green/10 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i data-lucide="check-circle" class="w-8 h-8 text-brand-green"></i>
                    </div>
                    <h4 class="text-xl font-bold text-brand-dark mb-2">Request Sent!</h4>
                    <p class="text-gray-500">We'll reach out within 24 hours.</p>
                </div>
            </div>
        </div>
    </div>
"""

# ============================================================
# SHARED SCRIPTS (chatbot uses safe DOM construction; no innerHTML w/ user data)
# ============================================================
SCRIPTS = f"""    <script src="https://unpkg.com/lucide@0.294.0/dist/umd/lucide.min.js"></script>
    <script>
        (function() {{
            'use strict';
            lucide.createIcons();

            // ===== Mobile Menu =====
            var menuToggle = document.getElementById('menuToggle');
            var menuClose = document.getElementById('menuClose');
            var mobileMenu = document.getElementById('mobileMenu');
            if (menuToggle && menuClose && mobileMenu) {{
                menuToggle.addEventListener('click', function() {{
                    mobileMenu.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }});
                menuClose.addEventListener('click', function() {{
                    mobileMenu.classList.remove('active');
                    document.body.style.overflow = '';
                }});
                document.querySelectorAll('.mobile-link').forEach(function(link) {{
                    link.addEventListener('click', function() {{
                        mobileMenu.classList.remove('active');
                        document.body.style.overflow = '';
                    }});
                }});
            }}

            // ===== Navbar (solid background, no scroll color swap needed) =====

            // ===== Back to Top =====
            var backToTop = document.getElementById('backToTop');
            if (backToTop) {{
                window.addEventListener('scroll', function() {{
                    if (window.scrollY > 400) {{
                        backToTop.classList.remove('opacity-0', 'pointer-events-none');
                        backToTop.classList.add('opacity-100');
                    }} else {{
                        backToTop.classList.add('opacity-0', 'pointer-events-none');
                        backToTop.classList.remove('opacity-100');
                    }}
                }});
                backToTop.addEventListener('click', function() {{
                    window.scrollTo({{ top: 0, behavior: 'smooth' }});
                }});
            }}

            // ===== Counter Animation =====
            var counters = document.querySelectorAll('.counter-value');
            var counterAnimated = false;
            function animateCounters() {{
                counters.forEach(function(counter) {{
                    var target = parseInt(counter.getAttribute('data-target'), 10);
                    if (isNaN(target)) return;
                    var duration = 2000;
                    var startTime = performance.now();
                    function step(currentTime) {{
                        var elapsed = currentTime - startTime;
                        var progress = Math.min(elapsed / duration, 1);
                        var ease = 1 - Math.pow(1 - progress, 3);
                        counter.textContent = String(Math.floor(target * ease));
                        if (progress < 1) requestAnimationFrame(step);
                        else counter.textContent = String(target);
                    }}
                    requestAnimationFrame(step);
                }});
            }}
            if (counters.length) {{
                var counterObserver = new IntersectionObserver(function(entries) {{
                    entries.forEach(function(entry) {{
                        if (entry.isIntersecting && !counterAnimated) {{
                            counterAnimated = true;
                            animateCounters();
                        }}
                    }});
                }}, {{ threshold: 0.3 }});
                counters.forEach(function(c) {{ counterObserver.observe(c); }});
            }}

            // ===== Form submit helper (AJAX -> FormSubmit) =====
            function ajaxSubmit(form, onSuccess, onError) {{
                form.addEventListener('submit', function(e) {{
                    e.preventDefault();
                    var btn = form.querySelector('button[type="submit"]');
                    var originalHTML = btn ? btn.innerHTML : '';
                    if (btn) {{ btn.disabled = true; btn.textContent = 'Sending...'; }}
                    fetch(form.action, {{
                        method: 'POST',
                        body: new FormData(form),
                        headers: {{ 'Accept': 'application/json' }}
                    }}).then(function(r) {{
                        if (!r.ok) throw new Error('Network');
                        return r.json().catch(function() {{ return {{}}; }});
                    }}).then(function() {{
                        if (typeof onSuccess === 'function') onSuccess();
                        form.reset();
                        lucide.createIcons();
                    }}).catch(function() {{
                        if (typeof onError === 'function') onError();
                        else alert('Something went wrong. Please email {EMAIL} directly.');
                        if (btn) {{ btn.disabled = false; btn.innerHTML = originalHTML; }}
                        lucide.createIcons();
                    }});
                }});
            }}

            // Newsletter
            var newsletterForm = document.getElementById('newsletterForm');
            var newsletterSuccess = document.getElementById('newsletterSuccess');
            if (newsletterForm) {{
                ajaxSubmit(newsletterForm, function() {{
                    newsletterForm.classList.add('hidden');
                    if (newsletterSuccess) newsletterSuccess.classList.remove('hidden');
                }}, function() {{ /* silent */ }});
            }}

            // Contact form on contact page
            var contactForm = document.getElementById('contactForm');
            var formSuccess = document.getElementById('formSuccess');
            if (contactForm) {{
                ajaxSubmit(contactForm, function() {{
                    contactForm.classList.add('hidden');
                    if (formSuccess) formSuccess.classList.remove('hidden');
                }});
            }}

            // ===== Quote Modal =====
            var quoteModal = document.getElementById('quoteModal');
            var quoteForm = document.getElementById('quoteForm');
            var quoteSuccess = document.getElementById('quoteSuccess');
            var quoteClose = document.getElementById('quoteModalClose');
            function openQuote() {{
                if (!quoteModal) return;
                quoteModal.classList.remove('hidden');
                quoteModal.classList.add('flex');
                document.body.style.overflow = 'hidden';
                lucide.createIcons();
            }}
            function closeQuote() {{
                if (!quoteModal) return;
                quoteModal.classList.add('hidden');
                quoteModal.classList.remove('flex');
                document.body.style.overflow = '';
            }}
            document.querySelectorAll('[data-open-quote]').forEach(function(btn) {{
                btn.addEventListener('click', openQuote);
            }});
            if (quoteClose) quoteClose.addEventListener('click', closeQuote);
            if (quoteModal) quoteModal.addEventListener('click', function(e) {{
                if (e.target === quoteModal) closeQuote();
            }});
            document.addEventListener('keydown', function(e) {{
                if (e.key === 'Escape') closeQuote();
            }});
            if (quoteForm) {{
                ajaxSubmit(quoteForm, function() {{
                    quoteForm.classList.add('hidden');
                    if (quoteSuccess) quoteSuccess.classList.remove('hidden');
                }});
            }}

            // ===== Reveal animations =====
            var revealObserver = new IntersectionObserver(function(entries) {{
                entries.forEach(function(entry) {{
                    if (entry.isIntersecting) {{
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }}
                }});
            }}, {{ threshold: 0.1 }});
            document.querySelectorAll('.gradient-card').forEach(function(el) {{
                el.style.opacity = '0';
                el.style.transform = 'translateY(30px)';
                el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                revealObserver.observe(el);
            }});

            // ===== Class-based reveal (.reveal, .reveal-left, .reveal-right, .spiral-svg, .process-card) =====
            var classReveal = new IntersectionObserver(function(entries) {{
                entries.forEach(function(entry) {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('in-view');
                        classReveal.unobserve(entry.target);
                    }}
                }});
            }}, {{ threshold: 0.15 }});
            document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .spiral-svg, .process-card').forEach(function(el) {{
                classReveal.observe(el);
            }});

            // ===== Smooth scroll for in-page hashes =====
            document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(function(anchor) {{
                anchor.addEventListener('click', function(e) {{
                    var href = this.getAttribute('href');
                    var target = document.querySelector(href);
                    if (target) {{
                        e.preventDefault();
                        var pos = target.getBoundingClientRect().top + window.pageYOffset - 70;
                        window.scrollTo({{ top: pos, behavior: 'smooth' }});
                    }}
                }});
            }});

            // ===== Chatbot (safe DOM construction) =====
            var chatbotToggle = document.getElementById('chatbotToggle');
            var chatbotWindow = document.getElementById('chatbotWindow');
            var chatbotClose = document.getElementById('chatbotClose');
            var chatbotMessages = document.getElementById('chatbotMessages');
            var chatbotQuickReplies = document.getElementById('chatbotQuickReplies');
            var iconOpen = document.getElementById('chatbotIconOpen');
            var iconClose = document.getElementById('chatbotIconClose');

            var botKnowledge = {{
                services: "We offer AI & Machine Learning, Cloud Solutions, Mobile Development, Cybersecurity, Data Engineering, and DevOps & Automation. Visit our Services page for details.",
                pricing: "Pricing depends on scope. Most projects start with a free discovery call. Tap 'Get Started' to share your brief, or message us on WhatsApp.",
                contact: "Email: {EMAIL}. WhatsApp: +62 823-8544-9541. Or use our Contact page.",
                location: "We're based in Jakarta, Indonesia, serving clients in 15+ countries.",
                hours: "We respond within 24 hours, Mon\u2013Fri. WhatsApp is fastest for urgent matters.",
                "default": "I can help with: services, pricing, contact, location, or response times. Tap WhatsApp below to chat with a human."
            }};

            var quickReplies = [
                {{ label: 'Our Services', key: 'services' }},
                {{ label: 'Pricing', key: 'pricing' }},
                {{ label: 'Contact Info', key: 'contact' }},
                {{ label: 'Location', key: 'location' }},
                {{ label: 'Response Time', key: 'hours' }}
            ];

            function el(tag, cls, text) {{
                var n = document.createElement(tag);
                if (cls) n.className = cls;
                if (text != null) n.textContent = text;
                return n;
            }}

            function addBotMessage(text) {{
                var wrap = el('div', 'flex gap-2 items-start');
                var avatar = el('div', 'w-7 h-7 bg-white rounded-full flex items-center justify-center shrink-0 mt-0.5 overflow-hidden ring-1 ring-brand-green/20');
                var img = document.createElement('img');
                img.src = 'images/Logo.png';
                img.alt = 'Akanofa';
                img.className = 'w-full h-full object-contain';
                avatar.appendChild(img);
                var bubble = el('div', 'bg-white rounded-2xl rounded-tl-sm px-3 py-2 text-sm text-brand-dark shadow-sm max-w-[85%]', text);
                wrap.appendChild(avatar);
                wrap.appendChild(bubble);
                chatbotMessages.appendChild(wrap);
                chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
            }}

            function addUserMessage(text) {{
                var wrap = el('div', 'flex justify-end');
                wrap.appendChild(el('div', 'bg-brand-dark text-white rounded-2xl rounded-tr-sm px-3 py-2 text-sm max-w-[85%]', text));
                chatbotMessages.appendChild(wrap);
                chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
            }}

            function renderQuickReplies() {{
                chatbotQuickReplies.textContent = '';
                quickReplies.forEach(function(qr) {{
                    var btn = el('button', 'text-xs bg-brand-yellow-light text-brand-dark px-3 py-1.5 rounded-full hover:bg-brand-yellow transition-colors font-medium', qr.label);
                    btn.type = 'button';
                    btn.addEventListener('click', function() {{
                        addUserMessage(qr.label);
                        setTimeout(function() {{
                            addBotMessage(botKnowledge[qr.key] || botKnowledge['default']);
                        }}, 350);
                    }});
                    chatbotQuickReplies.appendChild(btn);
                }});
            }}

            var chatInitialized = false;
            function openChat() {{
                chatbotWindow.classList.remove('hidden');
                chatbotWindow.classList.add('flex');
                if (iconOpen) iconOpen.classList.add('hidden');
                if (iconClose) iconClose.classList.remove('hidden');
                if (!chatInitialized) {{
                    addBotMessage("\N{WAVING HAND SIGN} Hi there! I'm Akanofa's virtual assistant. How can I help today?");
                    renderQuickReplies();
                    chatInitialized = true;
                }}
            }}
            function closeChat() {{
                chatbotWindow.classList.add('hidden');
                chatbotWindow.classList.remove('flex');
                if (iconOpen) iconOpen.classList.remove('hidden');
                if (iconClose) iconClose.classList.add('hidden');
            }}
            if (chatbotToggle) chatbotToggle.addEventListener('click', function() {{
                if (chatbotWindow.classList.contains('hidden')) openChat();
                else closeChat();
            }});
            if (chatbotClose) chatbotClose.addEventListener('click', closeChat);
        }})();
    </script>
</body>
</html>
"""

# ============================================================
# PAGE BODIES
# ============================================================

INDEX_BODY = """    <!-- Hero Section -->
    <section id="home" class="gradient-hero relative min-h-screen flex items-center overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="absolute top-20 right-10 w-72 h-72 bg-brand-yellow/10 rounded-full blur-3xl float-animation"></div>
        <div class="absolute bottom-20 left-10 w-96 h-96 bg-brand-yellow/5 rounded-full blur-3xl float-animation-delayed"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-32 relative z-10">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div>
                    <div class="animate-fade-in-up">
                        <span class="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full px-4 py-1.5 text-brand-yellow text-sm font-medium mb-6">
                            <span class="w-2 h-2 bg-brand-yellow rounded-full animate-pulse"></span>
                            Your Technology Partner
                        </span>
                    </div>
                    <h1 class="animate-fade-in-up-delay-1 text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6">
                        Intelligent software,<br>
                        <span class="text-brand-yellow">built for your</span><br>
                        business.
                    </h1>
                    <p class="animate-fade-in-up-delay-2 text-lg text-white/70 max-w-lg mb-8 leading-relaxed">
                        We craft cutting-edge software solutions that empower businesses to thrive in the digital age. Innovation meets reliability \u2014 that's the Akanofa promise.
                    </p>
                    <div class="animate-fade-in-up-delay-3 flex flex-col sm:flex-row gap-4">
                        <button type="button" data-open-quote class="bg-brand-yellow text-brand-dark px-8 py-4 rounded-full font-semibold text-base hover:bg-white transition-all duration-300 hover:shadow-xl group">
                            Start Your Project
                            <span class="inline-block ml-1 group-hover:translate-x-1 transition-transform">\u2192</span>
                        </button>
                        <a href="services.html" class="border-2 border-white/30 text-white px-8 py-4 rounded-full font-semibold text-base hover:bg-white/10 transition-all duration-300 text-center">
                            Explore Services
                        </a>
                    </div>
                    <div class="flex gap-8 mt-12 pt-8 border-t border-white/10">
                        <div><div class="text-3xl font-bold text-brand-yellow counter-value" data-target="150">0</div><div class="text-sm text-white/50 mt-1">Projects Delivered</div></div>
                        <div><div class="text-3xl font-bold text-brand-yellow counter-value" data-target="98">0</div><div class="text-sm text-white/50 mt-1">Client Satisfaction %</div></div>
                        <div><div class="text-3xl font-bold text-brand-yellow counter-value" data-target="12">0</div><div class="text-sm text-white/50 mt-1">Years of Excellence</div></div>
                    </div>
                </div>
                <div class="hidden lg:flex justify-center items-center relative">
                    <div class="relative w-full max-w-md">
                        <div class="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-6 float-animation">
                            <div class="flex items-center gap-3 mb-4">
                                <div class="w-10 h-10 bg-brand-yellow/20 rounded-lg flex items-center justify-center"><i data-lucide="cpu" class="w-5 h-5 text-brand-yellow"></i></div>
                                <div><div class="text-white font-semibold text-sm">AI Processing</div><div class="text-white/50 text-xs">Real-time Analytics</div></div>
                            </div>
                            <div class="space-y-3">
                                <div class="flex justify-between text-xs text-white/60"><span>Model Training</span><span>94%</span></div>
                                <div class="w-full bg-white/10 rounded-full h-1.5"><div class="bg-brand-yellow h-1.5 rounded-full" style="width:94%"></div></div>
                                <div class="flex justify-between text-xs text-white/60"><span>Data Processing</span><span>87%</span></div>
                                <div class="w-full bg-white/10 rounded-full h-1.5"><div class="bg-brand-light h-1.5 rounded-full" style="width:87%"></div></div>
                            </div>
                        </div>
                        <div class="absolute -bottom-8 -left-8 bg-brand-yellow text-brand-dark rounded-xl p-4 shadow-2xl float-animation-delayed">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 bg-brand-dark/10 rounded-full flex items-center justify-center"><i data-lucide="trending-up" class="w-5 h-5"></i></div>
                                <div><div class="font-bold text-lg">+340%</div><div class="text-xs text-brand-dark/70">Performance Boost</div></div>
                            </div>
                        </div>
                        <div class="absolute -top-4 -right-4 bg-white/10 backdrop-blur-md border border-white/20 rounded-xl p-4 float-animation">
                            <div class="flex items-center gap-2">
                                <div class="w-8 h-8 bg-green-500/20 rounded-full flex items-center justify-center"><i data-lucide="check-circle" class="w-4 h-4 text-green-400"></i></div>
                                <span class="text-white text-sm font-medium">System Online</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="absolute bottom-0 left-0 right-0">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 120" fill="#ffffff"><path d="M0,64L48,69.3C96,75,192,85,288,80C384,75,480,53,576,48C672,43,768,55,864,64C960,73,1056,80,1152,77.3C1248,75,1344,64,1392,58.7L1440,53.3L1440,120L1392,120C1344,120,1248,120,1152,120C1056,120,960,120,864,120C768,120,672,120,576,120C480,120,384,120,288,120C192,120,96,120,48,120L0,120Z"></path></svg>
        </div>
    </section>

    <!-- Trusted By Marquee -->
    <section class="bg-white py-12 overflow-hidden border-b border-gray-100">
        <div class="max-w-7xl mx-auto px-4 mb-6">
            <p class="text-center text-sm text-gray-400 font-medium uppercase tracking-widest">Trusted by Industry Leaders</p>
        </div>
        <div class="overflow-hidden">
            <div class="marquee-track">
                <div class="flex items-center gap-16 px-8 min-w-max">
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">TechCorp</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">DataFlow</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">CloudNest</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">QuantumAI</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">Synergetics</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">VeloCity</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">NexGen Labs</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">ByteShift</span>
                </div>
                <div class="flex items-center gap-16 px-8 min-w-max">
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">TechCorp</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">DataFlow</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">CloudNest</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">QuantumAI</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">Synergetics</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">VeloCity</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">NexGen Labs</span>
                    <span class="text-2xl font-bold text-gray-300 whitespace-nowrap">ByteShift</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Teaser -->
    <section class="bg-white py-24 relative">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-12">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">Our Services</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-4">Solutions that drive <span class="text-gradient">real results</span></h2>
                <p class="text-gray-500 text-lg">From concept to deployment, we deliver intelligent software tailored to your business.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-6 mb-10">
                <div class="gradient-card bg-white border border-gray-100 rounded-2xl p-8"><div class="service-icon-wrap w-14 h-14 bg-brand-dark/5 rounded-xl flex items-center justify-center mb-6 text-brand-dark"><i data-lucide="brain" class="w-7 h-7"></i></div><h3 class="text-xl font-bold text-brand-dark mb-3">AI &amp; Machine Learning</h3><p class="text-gray-500 leading-relaxed">Automate processes, gain insights, and make smarter decisions.</p></div>
                <div class="gradient-card bg-white border border-gray-100 rounded-2xl p-8"><div class="service-icon-wrap w-14 h-14 bg-brand-dark/5 rounded-xl flex items-center justify-center mb-6 text-brand-dark"><i data-lucide="cloud" class="w-7 h-7"></i></div><h3 class="text-xl font-bold text-brand-dark mb-3">Cloud Solutions</h3><p class="text-gray-500 leading-relaxed">Scalable, secure, and cost-efficient cloud infrastructure.</p></div>
                <div class="gradient-card bg-white border border-gray-100 rounded-2xl p-8"><div class="service-icon-wrap w-14 h-14 bg-brand-dark/5 rounded-xl flex items-center justify-center mb-6 text-brand-dark"><i data-lucide="smartphone" class="w-7 h-7"></i></div><h3 class="text-xl font-bold text-brand-dark mb-3">Mobile Development</h3><p class="text-gray-500 leading-relaxed">Native and cross-platform apps with seamless UX.</p></div>
            </div>
            <div class="text-center">
                <a href="services.html" class="inline-flex items-center gap-2 text-brand-green font-semibold hover:text-brand-dark transition-colors">View all services <i data-lucide="arrow-right" class="w-4 h-4"></i></a>
            </div>
        </div>
    </section>
"""

# Spiral process section (built with Python so we can compute exact node positions)
def _build_spiral_section():
    steps = [
        ("01", "Discover", "We listen, audit, and map your goals into a concrete brief.", "search", 320.0, 80.0),
        ("02", "Design", "UX, architecture, and prototypes validated with your team.", "pen-tool", 510.2, 258.2),
        ("03", "Develop", "Clean, tested code shipped in fast, transparent sprints.", "code-2", 414.0, 449.4),
        ("04", "Test", "Automated + manual QA, performance, and security audits.", "shield-check", 249.5, 417.1),
        ("05", "Deploy", "Zero-downtime release pipelines on scalable cloud infra.", "rocket", 243.9, 295.3),
        ("06", "Support", "Ongoing monitoring, iteration, and 24/7 partnership.", "life-buoy", 320.0, 295.0),
    ]
    nodes_svg = ""
    for i, (num, name, _desc, _icon, x, y) in enumerate(steps, 1):
        nodes_svg += f"""
                <g class="spiral-node n{i}">
                    <circle cx="{x}" cy="{y}" r="28" fill="#0B3D2E" stroke="#F5E6A3" stroke-width="3"/>
                    <text x="{x}" y="{y+5}" text-anchor="middle" fill="#F5E6A3" font-size="16" font-weight="800" font-family="Inter">{num}</text>
                </g>
                <text x="{x}" y="{y-40}" text-anchor="middle" fill="#0B3D2E" font-size="14" font-weight="700" font-family="Inter" class="spiral-node n{i}">{name}</text>"""
    cards_html = ""
    for i, (num, name, desc, icon, _x, _y) in enumerate(steps, 1):
        cards_html += f"""
                <div class="process-card flex gap-4 items-start p-5 rounded-2xl bg-white border border-gray-100 hover:border-brand-green/30 hover:shadow-lg transition-all" style="transition-delay:{i*0.1}s">
                    <div class="shrink-0 w-12 h-12 rounded-xl bg-gradient-to-br from-brand-dark to-brand-green text-brand-yellow flex items-center justify-center font-extrabold text-lg shadow-md">{num}</div>
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <i data-lucide="{icon}" class="w-4 h-4 text-brand-green"></i>
                            <h4 class="font-bold text-brand-dark">{name}</h4>
                        </div>
                        <p class="text-sm text-gray-500 leading-relaxed">{desc}</p>
                    </div>
                </div>"""
    return f"""    <!-- Process / Spiral Infographic -->
    <section class="bg-gradient-to-b from-brand-cream via-white to-brand-cream py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="absolute top-1/4 -left-20 w-72 h-72 bg-brand-yellow/20 rounded-full blur-3xl"></div>
        <div class="absolute bottom-1/4 -right-20 w-80 h-80 bg-brand-green/10 rounded-full blur-3xl"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-16 reveal">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">How We Work</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-4">A spiral toward <span class="text-gradient">your success</span></h2>
                <p class="text-gray-500 text-lg">Six iterative steps that turn your vision into shipped, supported software.</p>
            </div>
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <!-- Spiral SVG -->
                <div class="reveal-left order-2 lg:order-1">
                    <div class="relative aspect-square max-w-xl mx-auto">
                        <svg class="spiral-svg w-full h-full" viewBox="0 0 640 540" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                            <defs>
                                <linearGradient id="spiralGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" stop-color="#1A8C5E"/>
                                    <stop offset="50%" stop-color="#F5E6A3"/>
                                    <stop offset="100%" stop-color="#0B3D2E"/>
                                </linearGradient>
                            </defs>
                            <path class="spiral-path" d="{SPIRAL_D}" fill="none" stroke="url(#spiralGrad)" stroke-width="4" stroke-linecap="round"/>
                            {nodes_svg}
                        </svg>
                    </div>
                </div>
                <!-- Steps cards -->
                <div class="space-y-3 order-1 lg:order-2">
                    {cards_html}
                </div>
            </div>
        </div>
    </section>
"""

PROCESS_SECTION = _build_spiral_section()

# What-we-do image cards + industry partners
WHAT_WE_DO_SECTION = """    <!-- What We Do (image cards) -->
    <section class="bg-white py-20 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-12 reveal">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">In Action</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-4">What our engineers are <span class="text-gradient">building today</span></h2>
                <p class="text-gray-500 text-lg">A peek into the work we love \u2014 from AI experiments to production deployments.</p>
            </div>
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
                <article class="reveal tilt-card group bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-md hover:shadow-2xl hover:shadow-brand-dark/15 transition-all">
                    <div class="relative h-44 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=70" alt="Engineer coding at workstation" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark/80 via-transparent to-transparent"></div>
                        <span class="absolute top-3 left-3 bg-brand-yellow text-brand-dark text-xs font-bold px-2.5 py-1 rounded-full">AI / ML</span>
                    </div>
                    <div class="p-5">
                        <h3 class="font-bold text-brand-dark mb-1.5">Smart Automation</h3>
                        <p class="text-sm text-gray-500 leading-relaxed">Custom ML models that automate workflows and surface insights from your business data.</p>
                    </div>
                </article>
                <article class="reveal tilt-card group bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-md hover:shadow-2xl hover:shadow-brand-dark/15 transition-all" style="transition-delay:.1s">
                    <div class="relative h-44 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=800&q=70" alt="Server room cloud infrastructure" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark/80 via-transparent to-transparent"></div>
                        <span class="absolute top-3 left-3 bg-brand-yellow text-brand-dark text-xs font-bold px-2.5 py-1 rounded-full">Cloud</span>
                    </div>
                    <div class="p-5">
                        <h3 class="font-bold text-brand-dark mb-1.5">Cloud-Native Apps</h3>
                        <p class="text-sm text-gray-500 leading-relaxed">Scalable architectures on AWS, Azure, and GCP \u2014 with cost optimization built in.</p>
                    </div>
                </article>
                <article class="reveal tilt-card group bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-md hover:shadow-2xl hover:shadow-brand-dark/15 transition-all" style="transition-delay:.2s">
                    <div class="relative h-44 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=70" alt="Data dashboard analytics" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark/80 via-transparent to-transparent"></div>
                        <span class="absolute top-3 left-3 bg-brand-yellow text-brand-dark text-xs font-bold px-2.5 py-1 rounded-full">Data</span>
                    </div>
                    <div class="p-5">
                        <h3 class="font-bold text-brand-dark mb-1.5">Live Dashboards</h3>
                        <p class="text-sm text-gray-500 leading-relaxed">Real-time analytics platforms that turn raw data into decisions you can act on.</p>
                    </div>
                </article>
                <article class="reveal tilt-card group bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-md hover:shadow-2xl hover:shadow-brand-dark/15 transition-all" style="transition-delay:.3s">
                    <div class="relative h-44 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=800&q=70" alt="Cybersecurity code on screen" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark/80 via-transparent to-transparent"></div>
                        <span class="absolute top-3 left-3 bg-brand-yellow text-brand-dark text-xs font-bold px-2.5 py-1 rounded-full">Security</span>
                    </div>
                    <div class="p-5">
                        <h3 class="font-bold text-brand-dark mb-1.5">Secure by Design</h3>
                        <p class="text-sm text-gray-500 leading-relaxed">Penetration testing, hardened pipelines, and compliance baked into every release.</p>
                    </div>
                </article>
            </div>
        </div>
    </section>

    <!-- Industry Partners -->
    <section class="bg-brand-cream py-20 relative overflow-hidden border-t border-gray-100">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="absolute -top-20 left-1/2 -translate-x-1/2 w-[600px] h-[300px] bg-brand-yellow/15 rounded-full blur-3xl"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-12 reveal">
                <span class="inline-block bg-white text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4 border border-gray-200">Ecosystem</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-dark mb-3">Powered by the <span class="text-gradient">best in tech</span></h2>
                <p class="text-gray-500">We partner with industry leaders so you get enterprise-grade tooling \u2014 every time.</p>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4 mb-10">
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">AWS</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.05s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">Microsoft Azure</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.1s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">Google Cloud</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.15s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">OpenAI</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.2s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">Stripe</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.25s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">MongoDB</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.3s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">Cloudflare</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.35s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">Docker</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.4s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">Kubernetes</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.45s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">PostgreSQL</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.5s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">Vercel</span>
                </div>
                <div class="reveal aspect-[3/2] bg-white rounded-2xl border border-gray-100 flex items-center justify-center shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all p-4" style="transition-delay:.55s">
                    <span class="text-brand-dark font-bold text-lg tracking-tight">GitHub</span>
                </div>
            </div>
            <!-- Industry verticals -->
            <div class="text-center mt-16 mb-8 reveal">
                <h3 class="text-xl font-bold text-brand-dark mb-2">Industries we serve</h3>
                <p class="text-gray-500 text-sm">Trusted across sectors that demand reliability and innovation.</p>
            </div>
            <div class="flex flex-wrap justify-center gap-3">
                <span class="reveal inline-flex items-center gap-2 bg-white border border-gray-200 px-4 py-2 rounded-full text-sm font-medium text-brand-dark hover:border-brand-green transition-colors"><i data-lucide="landmark" class="w-4 h-4 text-brand-green"></i> Fintech</span>
                <span class="reveal inline-flex items-center gap-2 bg-white border border-gray-200 px-4 py-2 rounded-full text-sm font-medium text-brand-dark hover:border-brand-green transition-colors" style="transition-delay:.05s"><i data-lucide="shopping-bag" class="w-4 h-4 text-brand-green"></i> E-commerce</span>
                <span class="reveal inline-flex items-center gap-2 bg-white border border-gray-200 px-4 py-2 rounded-full text-sm font-medium text-brand-dark hover:border-brand-green transition-colors" style="transition-delay:.1s"><i data-lucide="heart-pulse" class="w-4 h-4 text-brand-green"></i> Healthcare</span>
                <span class="reveal inline-flex items-center gap-2 bg-white border border-gray-200 px-4 py-2 rounded-full text-sm font-medium text-brand-dark hover:border-brand-green transition-colors" style="transition-delay:.15s"><i data-lucide="graduation-cap" class="w-4 h-4 text-brand-green"></i> EdTech</span>
                <span class="reveal inline-flex items-center gap-2 bg-white border border-gray-200 px-4 py-2 rounded-full text-sm font-medium text-brand-dark hover:border-brand-green transition-colors" style="transition-delay:.2s"><i data-lucide="factory" class="w-4 h-4 text-brand-green"></i> Manufacturing</span>
                <span class="reveal inline-flex items-center gap-2 bg-white border border-gray-200 px-4 py-2 rounded-full text-sm font-medium text-brand-dark hover:border-brand-green transition-colors" style="transition-delay:.25s"><i data-lucide="truck" class="w-4 h-4 text-brand-green"></i> Logistics</span>
                <span class="reveal inline-flex items-center gap-2 bg-white border border-gray-200 px-4 py-2 rounded-full text-sm font-medium text-brand-dark hover:border-brand-green transition-colors" style="transition-delay:.3s"><i data-lucide="building" class="w-4 h-4 text-brand-green"></i> Real Estate</span>
                <span class="reveal inline-flex items-center gap-2 bg-white border border-gray-200 px-4 py-2 rounded-full text-sm font-medium text-brand-dark hover:border-brand-green transition-colors" style="transition-delay:.35s"><i data-lucide="utensils" class="w-4 h-4 text-brand-green"></i> Hospitality</span>
            </div>
        </div>
    </section>
"""

# ---------- SERVICES PAGE ----------
SERVICE_DETAILS = [
    {
        "icon": "brain",
        "tag": "AI / ML",
        "title": "AI & Machine Learning",
        "img": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=900&q=70",
        "desc": "Custom ML models, intelligent automation, and predictive analytics that turn your data into competitive advantage.",
        "features": ["Predictive models", "NLP & chatbots", "Computer vision", "Recommendation engines"],
        "stack": ["Python", "PyTorch", "TensorFlow", "OpenAI", "LangChain"],
    },
    {
        "icon": "cloud",
        "tag": "Cloud",
        "title": "Cloud Solutions",
        "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=900&q=70",
        "desc": "Scalable, secure, cost-efficient infrastructure on AWS, Azure & GCP \u2014 with auto-scaling and disaster recovery built in.",
        "features": ["Multi-cloud strategy", "Serverless apps", "Cost optimization", "Migration planning"],
        "stack": ["AWS", "Azure", "GCP", "Terraform", "CloudFormation"],
    },
    {
        "icon": "smartphone",
        "tag": "Mobile",
        "title": "Mobile Development",
        "img": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=900&q=70",
        "desc": "Native iOS / Android and cross-platform apps with delightful UX, offline-first design, and 60fps performance.",
        "features": ["iOS & Android native", "React Native / Flutter", "Push & analytics", "App store launch"],
        "stack": ["Swift", "Kotlin", "React Native", "Flutter", "Firebase"],
    },
    {
        "icon": "shield-check",
        "tag": "Security",
        "title": "Cybersecurity",
        "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=900&q=70",
        "desc": "Penetration testing, SOC 2 readiness, and zero-trust architectures that protect your customers and your reputation.",
        "features": ["Pen testing", "Compliance audits", "SIEM setup", "Incident response"],
        "stack": ["OWASP", "Burp Suite", "Snyk", "Vault", "Zero-Trust"],
    },
    {
        "icon": "database",
        "tag": "Data",
        "title": "Data Engineering",
        "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=900&q=70",
        "desc": "Modern data pipelines, warehouses, and real-time dashboards that turn raw events into decisions you can trust.",
        "features": ["ETL pipelines", "Data warehousing", "Real-time streaming", "BI dashboards"],
        "stack": ["PostgreSQL", "Snowflake", "Kafka", "dbt", "Airflow"],
    },
    {
        "icon": "settings",
        "tag": "DevOps",
        "title": "DevOps & Automation",
        "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=70",
        "desc": "CI/CD pipelines, containerization, and infrastructure-as-code that ship features faster and break less in production.",
        "features": ["CI/CD pipelines", "Container orchestration", "IaC", "Observability"],
        "stack": ["Docker", "Kubernetes", "GitHub Actions", "Terraform", "Grafana"],
    },
]

def _build_service_cards():
    cards = ""
    for i, s in enumerate(SERVICE_DETAILS):
        feats = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-600"><i data-lucide="check-circle-2" class="w-4 h-4 text-brand-green shrink-0 mt-0.5"></i><span>{f}</span></li>' for f in s["features"]])
        tags = "".join([f'<span class="inline-flex items-center text-[11px] font-semibold bg-brand-yellow-light text-brand-dark px-2.5 py-1 rounded-md">{t}</span>' for t in s["stack"]])
        delay = f"transition-delay:{(i%3)*0.1:.1f}s"
        cards += f"""
                <article class="reveal tilt-card group bg-white rounded-3xl overflow-hidden border border-gray-100 shadow-md hover:shadow-2xl hover:shadow-brand-dark/15 transition-all flex flex-col" style="{delay}">
                    <div class="relative h-44 overflow-hidden">
                        <img src="{s['img']}" alt="{s['title']}" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-dark/90 via-brand-dark/30 to-transparent"></div>
                        <span class="absolute top-3 right-3 bg-brand-yellow text-brand-dark text-[11px] font-bold px-2.5 py-1 rounded-full">{s['tag']}</span>
                        <div class="absolute bottom-4 left-5 flex items-center gap-3">
                            <div class="w-11 h-11 bg-brand-yellow rounded-xl flex items-center justify-center shadow-lg"><i data-lucide="{s['icon']}" class="w-6 h-6 text-brand-dark"></i></div>
                            <h3 class="text-white font-bold text-lg drop-shadow">{s['title']}</h3>
                        </div>
                    </div>
                    <div class="p-6 flex flex-col flex-1">
                        <p class="text-gray-500 text-sm leading-relaxed mb-5">{s['desc']}</p>
                        <ul class="space-y-2 mb-5">{feats}</ul>
                        <div class="flex flex-wrap gap-1.5 mb-6">{tags}</div>
                        <button type="button" data-open-quote class="mt-auto inline-flex items-center justify-center gap-2 w-full bg-brand-dark text-white py-3 rounded-xl font-semibold text-sm hover:bg-brand-green transition-all group/btn">
                            Get a quote
                            <i data-lucide="arrow-right" class="w-4 h-4 group-hover/btn:translate-x-1 transition-transform"></i>
                        </button>
                    </div>
                </article>"""
    return cards

SERVICES_BODY = subhero(
    "What We Do",
    'Solutions that drive <span class="text-brand-yellow">real results</span>',
    "From concept to deployment, we deliver intelligent software tailored to your unique business needs."
) + f"""    <!-- Quick stats bar -->
    <section class="bg-white -mt-8 relative z-20 pb-4">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 bg-white rounded-2xl shadow-2xl shadow-brand-dark/10 border border-gray-100 overflow-hidden">
                <div class="p-6 text-center border-b md:border-b-0 md:border-r border-gray-100">
                    <div class="text-3xl font-extrabold text-brand-dark"><span class="counter-value" data-target="6">0</span></div>
                    <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold mt-1">Core Services</div>
                </div>
                <div class="p-6 text-center border-b md:border-b-0 md:border-r border-gray-100">
                    <div class="text-3xl font-extrabold text-brand-dark"><span class="counter-value" data-target="40">0</span>+</div>
                    <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold mt-1">Tech Stacks</div>
                </div>
                <div class="p-6 text-center md:border-r border-gray-100">
                    <div class="text-3xl font-extrabold text-brand-dark"><span class="counter-value" data-target="98">0</span>%</div>
                    <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold mt-1">On-Time Delivery</div>
                </div>
                <div class="p-6 text-center">
                    <div class="text-3xl font-extrabold text-brand-dark">24<span class="text-brand-green">h</span></div>
                    <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold mt-1">Response Time</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Capabilities intro -->
    <section class="bg-white py-20 relative">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div class="reveal-left order-2 lg:order-1">
                    <div class="relative">
                        <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=900&q=70" alt="Code on developer monitor" loading="lazy" class="w-full rounded-3xl shadow-2xl shadow-brand-dark/15">
                        <div class="absolute -bottom-6 -right-6 bg-brand-yellow text-brand-dark p-5 rounded-2xl shadow-xl max-w-[200px] hidden sm:block">
                            <div class="text-3xl font-extrabold leading-none">12<span class="text-base font-bold ml-1">yrs</span></div>
                            <div class="text-xs font-semibold mt-1 text-brand-dark/80">building intelligent software</div>
                        </div>
                        <div class="absolute -top-6 -left-6 bg-brand-dark text-white p-4 rounded-2xl shadow-xl hidden sm:flex items-center gap-3">
                            <div class="w-10 h-10 bg-brand-yellow rounded-lg flex items-center justify-center"><i data-lucide="award" class="w-5 h-5 text-brand-dark"></i></div>
                            <div>
                                <div class="text-xs text-white/60 uppercase tracking-wider">Certified</div>
                                <div class="text-sm font-bold">ISO 27001 Ready</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="reveal-right order-1 lg:order-2">
                    <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">Capabilities</span>
                    <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-5 leading-tight">A full-stack technology partner \u2014 <span class="text-gradient">end to end</span></h2>
                    <p class="text-gray-500 text-lg mb-6 leading-relaxed">From discovery workshops to production monitoring, we cover every stage of the software lifecycle so you can stay focused on your business.</p>
                    <div class="grid sm:grid-cols-2 gap-3">
                        <div class="flex items-center gap-3 p-3 rounded-xl bg-brand-cream"><i data-lucide="layers" class="w-5 h-5 text-brand-green shrink-0"></i><span class="text-brand-dark font-medium text-sm">Architecture & design</span></div>
                        <div class="flex items-center gap-3 p-3 rounded-xl bg-brand-cream"><i data-lucide="code-2" class="w-5 h-5 text-brand-green shrink-0"></i><span class="text-brand-dark font-medium text-sm">Custom development</span></div>
                        <div class="flex items-center gap-3 p-3 rounded-xl bg-brand-cream"><i data-lucide="shield" class="w-5 h-5 text-brand-green shrink-0"></i><span class="text-brand-dark font-medium text-sm">Security & compliance</span></div>
                        <div class="flex items-center gap-3 p-3 rounded-xl bg-brand-cream"><i data-lucide="line-chart" class="w-5 h-5 text-brand-green shrink-0"></i><span class="text-brand-dark font-medium text-sm">Analytics & growth</span></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Detailed service cards -->
    <section class="bg-brand-cream py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern" style="opacity:.05"></div>
        <div class="absolute top-0 right-0 w-96 h-96 bg-brand-yellow/15 rounded-full blur-3xl"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-14 reveal">
                <span class="inline-block bg-white text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4 border border-gray-200">Service Lines</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-4">Everything you need to <span class="text-gradient">ship & scale</span></h2>
                <p class="text-gray-500 text-lg">Six service lines, one accountable team, zero hand-offs.</p>
            </div>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">{_build_service_cards()}
            </div>
        </div>
    </section>

    <!-- Tech stack infographic -->
    <section class="bg-brand-dark py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern" style="opacity:.04"></div>
        <div class="absolute top-1/2 -left-20 w-96 h-96 bg-brand-yellow/5 rounded-full blur-3xl"></div>
        <div class="absolute -bottom-20 right-0 w-96 h-96 bg-brand-green/20 rounded-full blur-3xl"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-14 reveal">
                <span class="inline-block bg-white/10 border border-white/20 text-brand-yellow px-4 py-1.5 rounded-full text-sm font-semibold mb-4">Our Toolbox</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-4">A modern stack, <span class="text-brand-yellow">battle-tested</span> in production</h2>
                <p class="text-white/60 text-lg">We pick the right tool for the job \u2014 here are the ones we reach for most.</p>
            </div>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-5">
                <div class="reveal bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-brand-yellow/30 transition-all">
                    <div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 rounded-lg bg-brand-yellow/15 text-brand-yellow flex items-center justify-center"><i data-lucide="monitor" class="w-5 h-5"></i></div><h3 class="font-bold text-white">Frontend</h3></div>
                    <div class="flex flex-wrap gap-2">
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">React</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Next.js</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Vue</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">TypeScript</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Tailwind</span>
                    </div>
                </div>
                <div class="reveal bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-brand-yellow/30 transition-all" style="transition-delay:.05s">
                    <div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 rounded-lg bg-brand-yellow/15 text-brand-yellow flex items-center justify-center"><i data-lucide="server" class="w-5 h-5"></i></div><h3 class="font-bold text-white">Backend</h3></div>
                    <div class="flex flex-wrap gap-2">
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Node.js</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Python</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Go</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Java</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">GraphQL</span>
                    </div>
                </div>
                <div class="reveal bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-brand-yellow/30 transition-all" style="transition-delay:.1s">
                    <div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 rounded-lg bg-brand-yellow/15 text-brand-yellow flex items-center justify-center"><i data-lucide="cloud" class="w-5 h-5"></i></div><h3 class="font-bold text-white">Cloud & DevOps</h3></div>
                    <div class="flex flex-wrap gap-2">
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">AWS</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Azure</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">GCP</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Docker</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Kubernetes</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Terraform</span>
                    </div>
                </div>
                <div class="reveal bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-brand-yellow/30 transition-all" style="transition-delay:.15s">
                    <div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 rounded-lg bg-brand-yellow/15 text-brand-yellow flex items-center justify-center"><i data-lucide="database" class="w-5 h-5"></i></div><h3 class="font-bold text-white">Data</h3></div>
                    <div class="flex flex-wrap gap-2">
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">PostgreSQL</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">MongoDB</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Redis</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Snowflake</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Kafka</span>
                    </div>
                </div>
                <div class="reveal bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-brand-yellow/30 transition-all" style="transition-delay:.2s">
                    <div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 rounded-lg bg-brand-yellow/15 text-brand-yellow flex items-center justify-center"><i data-lucide="brain" class="w-5 h-5"></i></div><h3 class="font-bold text-white">AI & ML</h3></div>
                    <div class="flex flex-wrap gap-2">
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">PyTorch</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">TensorFlow</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">OpenAI</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">LangChain</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Hugging Face</span>
                    </div>
                </div>
                <div class="reveal bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 hover:border-brand-yellow/30 transition-all" style="transition-delay:.25s">
                    <div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 rounded-lg bg-brand-yellow/15 text-brand-yellow flex items-center justify-center"><i data-lucide="smartphone" class="w-5 h-5"></i></div><h3 class="font-bold text-white">Mobile</h3></div>
                    <div class="flex flex-wrap gap-2">
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Swift</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Kotlin</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">React Native</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Flutter</span>
                        <span class="text-xs bg-white/10 text-white/80 px-3 py-1.5 rounded-full">Firebase</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Engagement model — horizontal flow infographic -->
    <section class="bg-white py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-16 reveal">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">Engagement Models</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-dark mb-3">Flexible ways to <span class="text-gradient">work with us</span></h2>
                <p class="text-gray-500">Whether you need a focused sprint, an embedded team, or a trusted advisor \u2014 we adapt to where you are.</p>
            </div>

            <div class="relative">
                <!-- Connecting line -->
                <div class="hidden md:block absolute top-10 left-[16.67%] right-[16.67%] h-0.5 bg-gradient-to-r from-brand-yellow via-brand-green to-brand-dark opacity-40"></div>

                <div class="grid md:grid-cols-3 gap-12 md:gap-8 relative">
                    <div class="reveal text-center md:text-left">
                        <div class="flex justify-center md:justify-start mb-5">
                            <div class="w-20 h-20 rounded-full bg-brand-yellow-light border-2 border-brand-yellow flex items-center justify-center relative shadow-md">
                                <i data-lucide="zap" class="w-9 h-9 text-brand-dark"></i>
                                <span class="absolute -top-1 -right-1 w-7 h-7 bg-brand-dark text-brand-yellow text-xs font-extrabold rounded-full flex items-center justify-center ring-2 ring-white">01</span>
                            </div>
                        </div>
                        <div class="text-xs font-bold uppercase tracking-[0.15em] text-brand-green mb-2">Focused Sprint</div>
                        <h3 class="text-xl font-extrabold text-brand-dark mb-2">Ship a defined deliverable, fast</h3>
                        <p class="text-sm text-gray-500 leading-relaxed mb-3">Best when you have a clear scope \u2014 an MVP, a prototype, or a discrete module you need built and shipped in weeks, not months.</p>
                        <div class="text-xs text-brand-dark/70"><span class="font-semibold">Typical:</span> 2\u20136 weeks \u00b7 small senior team</div>
                    </div>

                    <div class="reveal text-center md:text-left" style="transition-delay:.1s">
                        <div class="flex justify-center md:justify-start mb-5">
                            <div class="w-20 h-20 rounded-full bg-brand-green/10 border-2 border-brand-green flex items-center justify-center relative shadow-md">
                                <i data-lucide="users" class="w-9 h-9 text-brand-green"></i>
                                <span class="absolute -top-1 -right-1 w-7 h-7 bg-brand-dark text-brand-yellow text-xs font-extrabold rounded-full flex items-center justify-center ring-2 ring-white">02</span>
                            </div>
                        </div>
                        <div class="text-xs font-bold uppercase tracking-[0.15em] text-brand-green mb-2">Embedded Squad</div>
                        <h3 class="text-xl font-extrabold text-brand-dark mb-2">Become your in-house team</h3>
                        <p class="text-sm text-gray-500 leading-relaxed mb-3">A cross-functional pod \u2014 PM, designers, engineers \u2014 working alongside you in your tools, your standups, your roadmap.</p>
                        <div class="text-xs text-brand-dark/70"><span class="font-semibold">Typical:</span> 3+ months \u00b7 direct Slack access</div>
                    </div>

                    <div class="reveal text-center md:text-left" style="transition-delay:.2s">
                        <div class="flex justify-center md:justify-start mb-5">
                            <div class="w-20 h-20 rounded-full bg-brand-dark/5 border-2 border-brand-dark flex items-center justify-center relative shadow-md">
                                <i data-lucide="compass" class="w-9 h-9 text-brand-dark"></i>
                                <span class="absolute -top-1 -right-1 w-7 h-7 bg-brand-dark text-brand-yellow text-xs font-extrabold rounded-full flex items-center justify-center ring-2 ring-white">03</span>
                            </div>
                        </div>
                        <div class="text-xs font-bold uppercase tracking-[0.15em] text-brand-green mb-2">Trusted Advisor</div>
                        <h3 class="text-xl font-extrabold text-brand-dark mb-2">CTO-level guidance on demand</h3>
                        <p class="text-sm text-gray-500 leading-relaxed mb-3">Architecture reviews, security audits, hiring help, and strategic technical direction \u2014 without the full-time hire.</p>
                        <div class="text-xs text-brand-dark/70"><span class="font-semibold">Typical:</span> Workshops \u00b7 written reports \u00b7 office hours</div>
                    </div>
                </div>
            </div>

            <div class="text-center mt-14 reveal">
                <p class="text-sm text-gray-500 mb-4">Not sure which one fits? We'll help you figure it out on a free 30-minute call.</p>
                <button type="button" data-open-quote class="inline-flex items-center gap-2 text-brand-green font-semibold hover:text-brand-dark transition-colors group">
                    Talk to our team
                    <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                </button>
            </div>
        </div>
    </section>
""" + CTA_STRIP

ABOUT_BODY = subhero(
    "About Akanofa",
    'Being your <span class="text-brand-yellow">technology company</span> is our mission',
    "We don't just build software \u2014 we become an extension of your team."
) + """    <!-- Story + image -->
    <section class="bg-white py-20 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid lg:grid-cols-2 gap-14 items-center">
                <div class="reveal-left">
                    <div class="relative">
                        <img src="images/Office.jpg" alt="Akanofa office at Bellezza BSA, Jakarta" loading="lazy" class="w-full aspect-[4/3] object-cover rounded-3xl shadow-2xl shadow-brand-dark/20">
                        <div class="absolute -bottom-6 -left-6 bg-brand-yellow text-brand-dark p-5 rounded-2xl shadow-xl max-w-[220px] hidden sm:block">
                            <div class="flex items-center gap-2 mb-1"><i data-lucide="map-pin" class="w-4 h-4"></i><span class="text-xs font-bold uppercase tracking-wider">HQ</span></div>
                            <div class="font-extrabold leading-tight">Bellezza BSA, Jakarta</div>
                            <div class="text-xs text-brand-dark/70 mt-1">Where it all began \u2014 2014</div>
                        </div>
                        <div class="absolute -top-6 -right-6 bg-brand-dark text-white p-4 rounded-2xl shadow-xl hidden sm:flex items-center gap-3">
                            <div class="w-12 h-12 bg-brand-yellow rounded-full flex items-center justify-center"><i data-lucide="trending-up" class="w-6 h-6 text-brand-dark"></i></div>
                            <div>
                                <div class="text-2xl font-extrabold text-brand-yellow leading-none">+340%</div>
                                <div class="text-[10px] uppercase tracking-wider text-white/60">Avg client growth</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="reveal-right">
                    <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">Our Story</span>
                    <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-6 leading-tight">A partnership, <span class="text-gradient">not just a project</span></h2>
                    <p class="text-gray-500 text-lg mb-5 leading-relaxed">At Akanofa, we don't just build software \u2014 we become an extension of your team. Our approach combines deep technical expertise with genuine partnership, ensuring that every solution we create is perfectly aligned with your business goals.</p>
                    <p class="text-gray-500 mb-7 leading-relaxed">Founded in Jakarta on the principle that technology should empower \u2014 not complicate \u2014 we've helped over 150 businesses across 15 countries transform their operations through intelligent software that delivers measurable results.</p>
                    <div class="grid sm:grid-cols-2 gap-3 mb-8">
                        <div class="flex items-center gap-3 p-3 rounded-xl bg-brand-cream"><div class="w-9 h-9 bg-brand-green/10 rounded-lg flex items-center justify-center shrink-0"><i data-lucide="check" class="w-5 h-5 text-brand-green"></i></div><span class="text-brand-dark font-medium text-sm">End-to-end solutions</span></div>
                        <div class="flex items-center gap-3 p-3 rounded-xl bg-brand-cream"><div class="w-9 h-9 bg-brand-green/10 rounded-lg flex items-center justify-center shrink-0"><i data-lucide="check" class="w-5 h-5 text-brand-green"></i></div><span class="text-brand-dark font-medium text-sm">Agile methodology</span></div>
                        <div class="flex items-center gap-3 p-3 rounded-xl bg-brand-cream"><div class="w-9 h-9 bg-brand-green/10 rounded-lg flex items-center justify-center shrink-0"><i data-lucide="check" class="w-5 h-5 text-brand-green"></i></div><span class="text-brand-dark font-medium text-sm">24/7 dedicated support</span></div>
                        <div class="flex items-center gap-3 p-3 rounded-xl bg-brand-cream"><div class="w-9 h-9 bg-brand-green/10 rounded-lg flex items-center justify-center shrink-0"><i data-lucide="check" class="w-5 h-5 text-brand-green"></i></div><span class="text-brand-dark font-medium text-sm">Scalable architecture</span></div>
                    </div>
                    <button type="button" data-open-quote class="inline-flex items-center gap-2 bg-brand-dark text-white px-8 py-4 rounded-full font-semibold hover:bg-brand-green transition-all duration-300 group">
                        Partner With Us
                        <i data-lucide="arrow-right" class="w-5 h-5 group-hover:translate-x-1 transition-transform"></i>
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats grid -->
    <section class="bg-brand-cream py-20 relative overflow-hidden">
        <div class="absolute top-0 right-0 w-96 h-96 bg-brand-yellow/15 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-12 reveal">
                <span class="inline-block bg-white text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4 border border-gray-200">By the Numbers</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-dark">A decade of <span class="text-gradient">delivered impact</span></h2>
            </div>
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="reveal bg-brand-dark text-white rounded-2xl p-6 hover:scale-105 transition-transform">
                    <div class="w-12 h-12 bg-brand-yellow/15 text-brand-yellow rounded-xl flex items-center justify-center mb-4"><i data-lucide="calendar-clock" class="w-6 h-6"></i></div>
                    <div class="text-4xl font-extrabold text-brand-yellow counter-value" data-target="12">0</div>
                    <div class="text-sm text-white/60 mt-1">Years of Innovation</div>
                </div>
                <div class="reveal bg-brand-yellow-light text-brand-dark rounded-2xl p-6 hover:scale-105 transition-transform" style="transition-delay:.05s">
                    <div class="w-12 h-12 bg-white text-brand-green rounded-xl flex items-center justify-center mb-4"><i data-lucide="globe" class="w-6 h-6"></i></div>
                    <div class="text-4xl font-extrabold counter-value" data-target="15">0</div>
                    <div class="text-sm text-brand-dark/70 mt-1">Countries Served</div>
                </div>
                <div class="reveal bg-brand-yellow text-brand-dark rounded-2xl p-6 hover:scale-105 transition-transform" style="transition-delay:.1s">
                    <div class="w-12 h-12 bg-brand-dark text-brand-yellow rounded-xl flex items-center justify-center mb-4"><i data-lucide="users" class="w-6 h-6"></i></div>
                    <div class="text-4xl font-extrabold counter-value" data-target="50">0</div>
                    <div class="text-sm text-brand-dark/70 mt-1">Expert Engineers</div>
                </div>
                <div class="reveal bg-brand-green text-white rounded-2xl p-6 hover:scale-105 transition-transform" style="transition-delay:.15s">
                    <div class="w-12 h-12 bg-brand-yellow/15 text-brand-yellow rounded-xl flex items-center justify-center mb-4"><i data-lucide="heart" class="w-6 h-6"></i></div>
                    <div class="text-4xl font-extrabold text-brand-yellow counter-value" data-target="98">0</div>
                    <div class="text-sm text-white/70 mt-1">Client Retention %</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Timeline / Journey infographic -->
    <section class="bg-white py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-16 reveal">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">Our Journey</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-3">From three engineers <span class="text-gradient">to fifty</span></h2>
                <p class="text-gray-500 text-lg">A timeline of milestones that shaped Akanofa.</p>
            </div>
            <div class="relative">
                <!-- Vertical center line -->
                <div class="absolute left-4 md:left-1/2 top-0 bottom-0 w-0.5 bg-gradient-to-b from-brand-yellow via-brand-green to-brand-dark md:-translate-x-1/2"></div>
                <div class="space-y-10">
                    <div class="reveal-left relative md:grid md:grid-cols-2 md:gap-12 items-center">
                        <div class="md:text-right md:pr-12 pl-12 md:pl-0">
                            <div class="inline-block bg-brand-yellow text-brand-dark text-xs font-bold px-3 py-1 rounded-full mb-2">2014</div>
                            <h3 class="text-xl font-bold text-brand-dark mb-2">The spark</h3>
                            <p class="text-sm text-gray-500 leading-relaxed">Founded in Jakarta by three engineers who believed enterprise software shouldn\u2019t feel like enterprise software.</p>
                        </div>
                        <div class="hidden md:block"></div>
                        <div class="absolute left-4 md:left-1/2 top-0 w-8 h-8 -translate-x-1/2 rounded-full bg-brand-yellow ring-4 ring-white shadow-lg flex items-center justify-center"><i data-lucide="sparkles" class="w-4 h-4 text-brand-dark"></i></div>
                    </div>
                    <div class="reveal-right relative md:grid md:grid-cols-2 md:gap-12 items-center">
                        <div class="hidden md:block"></div>
                        <div class="md:pl-12 pl-12">
                            <div class="inline-block bg-brand-yellow text-brand-dark text-xs font-bold px-3 py-1 rounded-full mb-2">2017</div>
                            <h3 class="text-xl font-bold text-brand-dark mb-2">First international clients</h3>
                            <p class="text-sm text-gray-500 leading-relaxed">Crossed borders \u2014 partnered with fintechs in Singapore and Australia. Team grew to 15.</p>
                        </div>
                        <div class="absolute left-4 md:left-1/2 top-0 w-8 h-8 -translate-x-1/2 rounded-full bg-brand-green ring-4 ring-white shadow-lg flex items-center justify-center"><i data-lucide="globe" class="w-4 h-4 text-white"></i></div>
                    </div>
                    <div class="reveal-left relative md:grid md:grid-cols-2 md:gap-12 items-center">
                        <div class="md:text-right md:pr-12 pl-12 md:pl-0">
                            <div class="inline-block bg-brand-yellow text-brand-dark text-xs font-bold px-3 py-1 rounded-full mb-2">2020</div>
                            <h3 class="text-xl font-bold text-brand-dark mb-2">Cloud-first pivot</h3>
                            <p class="text-sm text-gray-500 leading-relaxed">Built dedicated cloud and DevOps practices. Achieved AWS Advanced Tier partnership.</p>
                        </div>
                        <div class="hidden md:block"></div>
                        <div class="absolute left-4 md:left-1/2 top-0 w-8 h-8 -translate-x-1/2 rounded-full bg-brand-green ring-4 ring-white shadow-lg flex items-center justify-center"><i data-lucide="cloud" class="w-4 h-4 text-white"></i></div>
                    </div>
                    <div class="reveal-right relative md:grid md:grid-cols-2 md:gap-12 items-center">
                        <div class="hidden md:block"></div>
                        <div class="md:pl-12 pl-12">
                            <div class="inline-block bg-brand-yellow text-brand-dark text-xs font-bold px-3 py-1 rounded-full mb-2">2023</div>
                            <h3 class="text-xl font-bold text-brand-dark mb-2">AI &amp; ML practice launched</h3>
                            <p class="text-sm text-gray-500 leading-relaxed">Stood up our applied AI lab \u2014 shipped LLM and computer-vision products to production.</p>
                        </div>
                        <div class="absolute left-4 md:left-1/2 top-0 w-8 h-8 -translate-x-1/2 rounded-full bg-brand-dark ring-4 ring-white shadow-lg flex items-center justify-center"><i data-lucide="brain" class="w-4 h-4 text-brand-yellow"></i></div>
                    </div>
                    <div class="reveal-left relative md:grid md:grid-cols-2 md:gap-12 items-center">
                        <div class="md:text-right md:pr-12 pl-12 md:pl-0">
                            <div class="inline-block bg-brand-yellow text-brand-dark text-xs font-bold px-3 py-1 rounded-full mb-2">2026</div>
                            <h3 class="text-xl font-bold text-brand-dark mb-2">150+ projects shipped</h3>
                            <p class="text-sm text-gray-500 leading-relaxed">Today \u2014 50 engineers, 15 countries served, and a 98% client retention rate.</p>
                        </div>
                        <div class="hidden md:block"></div>
                        <div class="absolute left-4 md:left-1/2 top-0 w-8 h-8 -translate-x-1/2 rounded-full bg-brand-dark ring-4 ring-brand-yellow shadow-lg flex items-center justify-center"><i data-lucide="rocket" class="w-4 h-4 text-brand-yellow"></i></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Mission / Vision / Values rich cards -->
    <section class="bg-brand-cream py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern" style="opacity:.05"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-14 reveal">
                <span class="inline-block bg-white text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4 border border-gray-200">What Drives Us</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-3">Our north <span class="text-gradient">stars</span></h2>
                <p class="text-gray-500 text-lg">The principles behind every line of code we ship.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <div class="reveal group bg-white rounded-3xl p-8 border border-gray-100 hover:shadow-2xl hover:shadow-brand-dark/10 hover:-translate-y-1 transition-all">
                    <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-brand-dark to-brand-green text-brand-yellow flex items-center justify-center mb-5 group-hover:scale-110 transition-transform"><i data-lucide="target" class="w-8 h-8"></i></div>
                    <div class="text-xs font-bold uppercase tracking-wider text-brand-green mb-1">Mission</div>
                    <h3 class="text-2xl font-extrabold text-brand-dark mb-3">Empower with intelligence</h3>
                    <p class="text-gray-500 leading-relaxed">Build software that gives every business \u2014 not just the giants \u2014 access to enterprise-grade intelligence.</p>
                </div>
                <div class="reveal group bg-white rounded-3xl p-8 border border-gray-100 hover:shadow-2xl hover:shadow-brand-dark/10 hover:-translate-y-1 transition-all" style="transition-delay:.1s">
                    <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-brand-dark to-brand-green text-brand-yellow flex items-center justify-center mb-5 group-hover:scale-110 transition-transform"><i data-lucide="eye" class="w-8 h-8"></i></div>
                    <div class="text-xs font-bold uppercase tracking-wider text-brand-green mb-1">Vision</div>
                    <h3 class="text-2xl font-extrabold text-brand-dark mb-3">Be your tech department</h3>
                    <p class="text-gray-500 leading-relaxed">A world where every business has a world-class technology partner who feels like an in-house team.</p>
                </div>
                <div class="reveal group bg-white rounded-3xl p-8 border border-gray-100 hover:shadow-2xl hover:shadow-brand-dark/10 hover:-translate-y-1 transition-all" style="transition-delay:.2s">
                    <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-brand-dark to-brand-green text-brand-yellow flex items-center justify-center mb-5 group-hover:scale-110 transition-transform"><i data-lucide="heart" class="w-8 h-8"></i></div>
                    <div class="text-xs font-bold uppercase tracking-wider text-brand-green mb-1">Values</div>
                    <h3 class="text-2xl font-extrabold text-brand-dark mb-3">Integrity, always</h3>
                    <p class="text-gray-500 leading-relaxed">Honest communication, transparent pricing, and code we'd be proud to put our name on \u2014 every time.</p>
                </div>
            </div>
            <!-- Sub-values strip -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mt-10">
                <div class="reveal flex items-center gap-3 bg-white p-4 rounded-xl border border-gray-100"><div class="w-10 h-10 bg-brand-yellow-light rounded-lg flex items-center justify-center"><i data-lucide="handshake" class="w-5 h-5 text-brand-dark"></i></div><span class="text-sm font-semibold text-brand-dark">Partnership</span></div>
                <div class="reveal flex items-center gap-3 bg-white p-4 rounded-xl border border-gray-100" style="transition-delay:.05s"><div class="w-10 h-10 bg-brand-yellow-light rounded-lg flex items-center justify-center"><i data-lucide="lightbulb" class="w-5 h-5 text-brand-dark"></i></div><span class="text-sm font-semibold text-brand-dark">Innovation</span></div>
                <div class="reveal flex items-center gap-3 bg-white p-4 rounded-xl border border-gray-100" style="transition-delay:.1s"><div class="w-10 h-10 bg-brand-yellow-light rounded-lg flex items-center justify-center"><i data-lucide="gem" class="w-5 h-5 text-brand-dark"></i></div><span class="text-sm font-semibold text-brand-dark">Quality</span></div>
                <div class="reveal flex items-center gap-3 bg-white p-4 rounded-xl border border-gray-100" style="transition-delay:.15s"><div class="w-10 h-10 bg-brand-yellow-light rounded-lg flex items-center justify-center"><i data-lucide="leaf" class="w-5 h-5 text-brand-dark"></i></div><span class="text-sm font-semibold text-brand-dark">Sustainability</span></div>
            </div>
        </div>
    </section>

    <!-- Leadership / Team section removed per design direction -->

    <!-- Office / Culture gallery removed per design direction -->
""" + CTA_STRIP

WHY_BODY = subhero(
    "Why Akanofa",
    'What <span class="text-brand-yellow">sets us apart</span>',
    "We combine innovation, precision, and partnership to deliver outcomes that matter."
) + """    <!-- 4 Differentiators (improved with images) -->
    <section class="bg-brand-dark py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern" style="opacity:0.03;"></div>
        <div class="absolute -top-40 -right-40 w-[500px] h-[500px] bg-brand-yellow/5 rounded-full blur-3xl"></div>
        <div class="absolute -bottom-40 -left-40 w-[500px] h-[500px] bg-brand-green/15 rounded-full blur-3xl"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-5">
                <div class="reveal group bg-gradient-to-br from-white/10 to-white/5 border border-white/10 rounded-3xl p-7 hover:border-brand-yellow/40 hover:-translate-y-1 transition-all">
                    <div class="text-5xl font-extrabold text-brand-yellow/20 mb-1">01</div>
                    <div class="w-14 h-14 bg-brand-yellow/15 rounded-2xl flex items-center justify-center mb-5 group-hover:bg-brand-yellow group-hover:text-brand-dark transition-all relative pulse-ring text-brand-yellow"><i data-lucide="zap" class="w-7 h-7"></i></div>
                    <h3 class="text-white font-bold text-lg mb-2">Lightning Delivery</h3>
                    <p class="text-white/50 text-sm leading-relaxed mb-4">Average MVP shipped in 6 weeks. Fast cycles without compromising quality.</p>
                    <div class="flex items-baseline gap-2 pt-3 border-t border-white/10">
                        <span class="text-2xl font-extrabold text-brand-yellow">2.4x</span>
                        <span class="text-xs text-white/40">faster than industry avg</span>
                    </div>
                </div>
                <div class="reveal group bg-gradient-to-br from-white/10 to-white/5 border border-white/10 rounded-3xl p-7 hover:border-brand-yellow/40 hover:-translate-y-1 transition-all" style="transition-delay:.05s">
                    <div class="text-5xl font-extrabold text-brand-yellow/20 mb-1">02</div>
                    <div class="w-14 h-14 bg-brand-yellow/15 rounded-2xl flex items-center justify-center mb-5 group-hover:bg-brand-yellow group-hover:text-brand-dark transition-all text-brand-yellow"><i data-lucide="users" class="w-7 h-7"></i></div>
                    <h3 class="text-white font-bold text-lg mb-2">Dedicated Squads</h3>
                    <p class="text-white/50 text-sm leading-relaxed mb-4">A team that operates as your own tech department \u2014 not contractors.</p>
                    <div class="flex items-baseline gap-2 pt-3 border-t border-white/10">
                        <span class="text-2xl font-extrabold text-brand-yellow">98%</span>
                        <span class="text-xs text-white/40">client retention rate</span>
                    </div>
                </div>
                <div class="reveal group bg-gradient-to-br from-white/10 to-white/5 border border-white/10 rounded-3xl p-7 hover:border-brand-yellow/40 hover:-translate-y-1 transition-all" style="transition-delay:.1s">
                    <div class="text-5xl font-extrabold text-brand-yellow/20 mb-1">03</div>
                    <div class="w-14 h-14 bg-brand-yellow/15 rounded-2xl flex items-center justify-center mb-5 group-hover:bg-brand-yellow group-hover:text-brand-dark transition-all text-brand-yellow"><i data-lucide="lock" class="w-7 h-7"></i></div>
                    <h3 class="text-white font-bold text-lg mb-2">Enterprise Security</h3>
                    <p class="text-white/50 text-sm leading-relaxed mb-4">Bank-grade protocols, OWASP-aligned reviews, and full SOC 2 readiness.</p>
                    <div class="flex items-baseline gap-2 pt-3 border-t border-white/10">
                        <span class="text-2xl font-extrabold text-brand-yellow">0</span>
                        <span class="text-xs text-white/40">security incidents to date</span>
                    </div>
                </div>
                <div class="reveal group bg-gradient-to-br from-white/10 to-white/5 border border-white/10 rounded-3xl p-7 hover:border-brand-yellow/40 hover:-translate-y-1 transition-all" style="transition-delay:.15s">
                    <div class="text-5xl font-extrabold text-brand-yellow/20 mb-1">04</div>
                    <div class="w-14 h-14 bg-brand-yellow/15 rounded-2xl flex items-center justify-center mb-5 group-hover:bg-brand-yellow group-hover:text-brand-dark transition-all text-brand-yellow"><i data-lucide="refresh-cw" class="w-7 h-7"></i></div>
                    <h3 class="text-white font-bold text-lg mb-2">Continuous Evolution</h3>
                    <p class="text-white/50 text-sm leading-relaxed mb-4">We don't disappear at launch \u2014 we iterate, optimize, and grow alongside you.</p>
                    <div class="flex items-baseline gap-2 pt-3 border-t border-white/10">
                        <span class="text-2xl font-extrabold text-brand-yellow">24/7</span>
                        <span class="text-xs text-white/40">monitoring &amp; support</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Comparison infographic -->
    <section class="bg-white py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-12 reveal">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">The Difference</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-3">Akanofa vs. <span class="text-gradient">a typical agency</span></h2>
                <p class="text-gray-500 text-lg">Why our clients keep choosing us, project after project.</p>
            </div>
            <div class="reveal rounded-3xl border border-gray-100 shadow-2xl shadow-brand-dark/10 overflow-hidden bg-white">
                <div class="grid grid-cols-3 bg-brand-dark text-white">
                    <div class="p-5 font-semibold text-sm uppercase tracking-wider text-white/60">Comparison</div>
                    <div class="p-5 text-center font-bold text-sm uppercase tracking-wider bg-brand-green text-brand-yellow">Akanofa</div>
                    <div class="p-5 text-center font-semibold text-sm uppercase tracking-wider text-white/60">Typical Agency</div>
                </div>
                <div class="divide-y divide-gray-100 text-sm">
                    <div class="grid grid-cols-3 items-center"><div class="p-5 font-medium text-brand-dark">Time to first demo</div><div class="p-5 text-center bg-brand-green/5 text-brand-dark font-bold">7 days</div><div class="p-5 text-center text-gray-400">3\u20134 weeks</div></div>
                    <div class="grid grid-cols-3 items-center"><div class="p-5 font-medium text-brand-dark">Dedicated team</div><div class="p-5 text-center bg-brand-green/5"><i data-lucide="check-circle-2" class="w-5 h-5 text-brand-green inline"></i></div><div class="p-5 text-center"><i data-lucide="x-circle" class="w-5 h-5 text-gray-300 inline"></i></div></div>
                    <div class="grid grid-cols-3 items-center"><div class="p-5 font-medium text-brand-dark">Direct Slack access</div><div class="p-5 text-center bg-brand-green/5"><i data-lucide="check-circle-2" class="w-5 h-5 text-brand-green inline"></i></div><div class="p-5 text-center"><i data-lucide="x-circle" class="w-5 h-5 text-gray-300 inline"></i></div></div>
                    <div class="grid grid-cols-3 items-center"><div class="p-5 font-medium text-brand-dark">Transparent pricing</div><div class="p-5 text-center bg-brand-green/5"><i data-lucide="check-circle-2" class="w-5 h-5 text-brand-green inline"></i></div><div class="p-5 text-center text-gray-400">Often hidden fees</div></div>
                    <div class="grid grid-cols-3 items-center"><div class="p-5 font-medium text-brand-dark">Post-launch support</div><div class="p-5 text-center bg-brand-green/5 text-brand-dark font-bold">24/7 included</div><div class="p-5 text-center text-gray-400">Extra contract</div></div>
                    <div class="grid grid-cols-3 items-center"><div class="p-5 font-medium text-brand-dark">Source code ownership</div><div class="p-5 text-center bg-brand-green/5 text-brand-dark font-bold">100% yours</div><div class="p-5 text-center text-gray-400">Often shared</div></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Performance metrics infographic -->
    <section class="bg-brand-cream py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern" style="opacity:.05"></div>
        <div class="absolute top-1/4 right-0 w-96 h-96 bg-brand-yellow/15 rounded-full blur-3xl"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid lg:grid-cols-2 gap-14 items-center">
                <div class="reveal-left">
                    <span class="inline-block bg-white text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4 border border-gray-200">Proven Performance</span>
                    <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-5 leading-tight">Numbers that <span class="text-gradient">speak louder</span> than promises</h2>
                    <p class="text-gray-500 text-lg mb-8 leading-relaxed">We benchmark every project against industry standards. Here's how Akanofa stacks up across the metrics that matter most to our clients.</p>
                    <div class="space-y-5">
                        <div>
                            <div class="flex justify-between mb-2"><span class="text-sm font-semibold text-brand-dark">Code quality score</span><span class="text-sm font-bold text-brand-green">96 / 100</span></div>
                            <div class="h-2.5 bg-white rounded-full overflow-hidden border border-gray-100"><div class="h-full bg-gradient-to-r from-brand-green to-brand-light rounded-full" style="width:96%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-2"><span class="text-sm font-semibold text-brand-dark">On-time delivery</span><span class="text-sm font-bold text-brand-green">98%</span></div>
                            <div class="h-2.5 bg-white rounded-full overflow-hidden border border-gray-100"><div class="h-full bg-gradient-to-r from-brand-green to-brand-light rounded-full" style="width:98%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-2"><span class="text-sm font-semibold text-brand-dark">Client satisfaction (NPS)</span><span class="text-sm font-bold text-brand-green">+72</span></div>
                            <div class="h-2.5 bg-white rounded-full overflow-hidden border border-gray-100"><div class="h-full bg-gradient-to-r from-brand-green to-brand-light rounded-full" style="width:92%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-2"><span class="text-sm font-semibold text-brand-dark">Test coverage (avg)</span><span class="text-sm font-bold text-brand-green">88%</span></div>
                            <div class="h-2.5 bg-white rounded-full overflow-hidden border border-gray-100"><div class="h-full bg-gradient-to-r from-brand-green to-brand-light rounded-full" style="width:88%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-2"><span class="text-sm font-semibold text-brand-dark">Avg. uptime</span><span class="text-sm font-bold text-brand-green">99.97%</span></div>
                            <div class="h-2.5 bg-white rounded-full overflow-hidden border border-gray-100"><div class="h-full bg-gradient-to-r from-brand-green to-brand-light rounded-full" style="width:99%"></div></div>
                        </div>
                    </div>
                </div>
                <div class="reveal-right">
                    <div class="relative">
                        <img src="https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=900&q=70" alt="Engineers reviewing performance dashboards" loading="lazy" class="w-full rounded-3xl shadow-2xl shadow-brand-dark/20">
                        <div class="absolute -bottom-6 -left-6 bg-white p-5 rounded-2xl shadow-2xl border border-gray-100 max-w-[220px] hidden sm:block">
                            <div class="flex items-center gap-2 mb-1"><div class="w-8 h-8 bg-brand-green/10 rounded-lg flex items-center justify-center"><i data-lucide="trending-up" class="w-4 h-4 text-brand-green"></i></div><span class="text-xs font-bold uppercase tracking-wider text-brand-dark">Avg. ROI</span></div>
                            <div class="text-3xl font-extrabold text-brand-dark mt-2">340%</div>
                            <div class="text-xs text-gray-500 mt-0.5">across our last 50 launches</div>
                        </div>
                        <div class="absolute -top-5 -right-5 bg-brand-yellow text-brand-dark px-4 py-3 rounded-2xl shadow-xl flex items-center gap-2 hidden sm:flex">
                            <i data-lucide="award" class="w-5 h-5"></i>
                            <div>
                                <div class="text-xs font-semibold leading-none">Top Rated</div>
                                <div class="text-xs text-brand-dark/70 mt-0.5">Clutch 2025</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="bg-white py-24 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-14 reveal">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">Client Stories</span>
                <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark mb-3">What our partners <span class="text-gradient">say about us</span></h2>
                <p class="text-gray-500 text-lg">Real words from teams we've helped scale.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <div class="reveal bg-white border border-gray-100 rounded-3xl p-7 hover:shadow-2xl hover:shadow-brand-dark/10 hover:-translate-y-1 transition-all">
                    <div class="flex gap-1 mb-4 text-brand-yellow">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-brand-dark leading-relaxed mb-6">"Akanofa felt like an extension of our team from day one. They shipped our MVP in 5 weeks \u2014 we'd budgeted for three months."</p>
                    <div class="flex items-center gap-3 pt-4 border-t border-gray-100">
                        <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&q=70" alt="Sarah Chen portrait" loading="lazy" class="w-12 h-12 rounded-full object-cover">
                        <div>
                            <div class="font-bold text-brand-dark text-sm">Sarah Chen</div>
                            <div class="text-xs text-gray-500">CTO, FinPay Singapore</div>
                        </div>
                    </div>
                </div>
                <div class="reveal bg-white border border-gray-100 rounded-3xl p-7 hover:shadow-2xl hover:shadow-brand-dark/10 hover:-translate-y-1 transition-all" style="transition-delay:.1s">
                    <div class="flex gap-1 mb-4 text-brand-yellow">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-brand-dark leading-relaxed mb-6">"Their AI team rebuilt our recommendation engine and lifted conversion by 41%. The ROI paid for the project in two months."</p>
                    <div class="flex items-center gap-3 pt-4 border-t border-gray-100">
                        <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=200&q=70" alt="Daniel Rey portrait" loading="lazy" class="w-12 h-12 rounded-full object-cover">
                        <div>
                            <div class="font-bold text-brand-dark text-sm">Daniel Rey</div>
                            <div class="text-xs text-gray-500">Head of Product, ShopFlux</div>
                        </div>
                    </div>
                </div>
                <div class="reveal bg-gradient-to-br from-brand-dark to-brand-green text-white rounded-3xl p-7 shadow-xl shadow-brand-dark/20" style="transition-delay:.2s">
                    <div class="flex gap-1 mb-4 text-brand-yellow">
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                        <i data-lucide="star" class="w-5 h-5 fill-current"></i>
                    </div>
                    <p class="text-white leading-relaxed mb-6">"Three years in, they're still the team I call first. Senior engineers, no nonsense, and a security mindset I trust completely."</p>
                    <div class="flex items-center gap-3 pt-4 border-t border-white/20">
                        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=200&q=70" alt="Marcus Tan portrait" loading="lazy" class="w-12 h-12 rounded-full object-cover ring-2 ring-brand-yellow">
                        <div>
                            <div class="font-bold text-white text-sm">Marcus Tan</div>
                            <div class="text-xs text-white/60">VP Engineering, Velocity Labs</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Certifications & recognition -->
    <section class="bg-brand-cream py-16 relative overflow-hidden border-y border-gray-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-8 reveal">
                <span class="text-xs uppercase tracking-widest font-semibold text-gray-400">Certifications &amp; Recognition</span>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
                <div class="reveal flex flex-col items-center justify-center bg-white rounded-2xl p-5 border border-gray-100 hover:shadow-lg transition-all"><i data-lucide="shield-check" class="w-7 h-7 text-brand-green mb-2"></i><span class="text-xs font-bold text-brand-dark text-center">ISO 27001<br>Ready</span></div>
                <div class="reveal flex flex-col items-center justify-center bg-white rounded-2xl p-5 border border-gray-100 hover:shadow-lg transition-all" style="transition-delay:.05s"><i data-lucide="award" class="w-7 h-7 text-brand-green mb-2"></i><span class="text-xs font-bold text-brand-dark text-center">AWS Advanced<br>Tier</span></div>
                <div class="reveal flex flex-col items-center justify-center bg-white rounded-2xl p-5 border border-gray-100 hover:shadow-lg transition-all" style="transition-delay:.1s"><i data-lucide="badge-check" class="w-7 h-7 text-brand-green mb-2"></i><span class="text-xs font-bold text-brand-dark text-center">SOC 2<br>Type II Aligned</span></div>
                <div class="reveal flex flex-col items-center justify-center bg-white rounded-2xl p-5 border border-gray-100 hover:shadow-lg transition-all" style="transition-delay:.15s"><i data-lucide="trophy" class="w-7 h-7 text-brand-green mb-2"></i><span class="text-xs font-bold text-brand-dark text-center">Clutch Top<br>B2B 2025</span></div>
                <div class="reveal flex flex-col items-center justify-center bg-white rounded-2xl p-5 border border-gray-100 hover:shadow-lg transition-all" style="transition-delay:.2s"><i data-lucide="star" class="w-7 h-7 text-brand-green mb-2"></i><span class="text-xs font-bold text-brand-dark text-center">GoodFirms<br>5.0 Rated</span></div>
                <div class="reveal flex flex-col items-center justify-center bg-white rounded-2xl p-5 border border-gray-100 hover:shadow-lg transition-all" style="transition-delay:.25s"><i data-lucide="briefcase" class="w-7 h-7 text-brand-green mb-2"></i><span class="text-xs font-bold text-brand-dark text-center">PMDN<br>KBLI 58200</span></div>
            </div>
        </div>
    </section>

    <!-- Yellow stats band -->
    <section class="bg-brand-yellow py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
                <div><div class="text-4xl sm:text-5xl font-extrabold text-brand-dark counter-value" data-target="150">0</div><div class="text-brand-dark/60 font-medium mt-2">Projects Completed</div></div>
                <div><div class="text-4xl sm:text-5xl font-extrabold text-brand-dark counter-value" data-target="98">0</div><div class="text-brand-dark/60 font-medium mt-2">Client Retention %</div></div>
                <div><div class="text-4xl sm:text-5xl font-extrabold text-brand-dark counter-value" data-target="50">0</div><div class="text-brand-dark/60 font-medium mt-2">Team Members</div></div>
                <div><div class="text-4xl sm:text-5xl font-extrabold text-brand-dark counter-value" data-target="15">0</div><div class="text-brand-dark/60 font-medium mt-2">Countries Served</div></div>
            </div>
        </div>
    </section>
""" + CTA_STRIP

CONTACT_BODY = subhero(
    "Get in Touch",
    'Let\u2019s build the <span class="text-brand-yellow">future together</span>',
    "Whether you have a project in mind or just want to explore possibilities, we're here to help."
) + f"""    <!-- Quick Contact Tiles -->
    <section class="bg-white -mt-10 relative z-20 pb-4">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <a href="mailto:{EMAIL}" class="reveal tilt-card group bg-white rounded-2xl p-6 border border-gray-100 shadow-xl shadow-brand-dark/5 hover:border-brand-green/30">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-brand-dark to-brand-green text-brand-yellow flex items-center justify-center mb-4 group-hover:scale-110 transition-transform"><i data-lucide="mail" class="w-6 h-6"></i></div>
                    <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold">Email</div>
                    <div class="text-brand-dark font-bold mt-1 text-sm break-all">{EMAIL}</div>
                </a>
                <a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank" rel="noopener noreferrer" class="reveal tilt-card group bg-white rounded-2xl p-6 border border-gray-100 shadow-xl shadow-brand-dark/5 hover:border-brand-green/30" style="transition-delay:.1s">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-[#25D366] to-[#128C7E] text-white flex items-center justify-center mb-4 group-hover:scale-110 transition-transform"><i data-lucide="message-circle" class="w-6 h-6"></i></div>
                    <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold">WhatsApp</div>
                    <div class="text-brand-dark font-bold mt-1">+62 823-8544-9541</div>
                </a>
                <a href="tel:+622158905002" class="reveal tilt-card group bg-white rounded-2xl p-6 border border-gray-100 shadow-xl shadow-brand-dark/5 hover:border-brand-green/30" style="transition-delay:.2s">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-brand-yellow to-brand-yellow-light text-brand-dark flex items-center justify-center mb-4 group-hover:scale-110 transition-transform"><i data-lucide="phone" class="w-6 h-6"></i></div>
                    <div class="text-xs uppercase tracking-wider text-gray-400 font-semibold">Office</div>
                    <div class="text-brand-dark font-bold mt-1">021-58905002</div>
                </a>
                <div class="reveal tilt-card group bg-gradient-to-br from-brand-dark to-brand-green text-white rounded-2xl p-6 shadow-xl shadow-brand-dark/20" style="transition-delay:.3s">
                    <div class="w-12 h-12 rounded-xl bg-brand-yellow text-brand-dark flex items-center justify-center mb-4 group-hover:scale-110 transition-transform"><i data-lucide="clock" class="w-6 h-6"></i></div>
                    <div class="text-xs uppercase tracking-wider text-brand-yellow font-semibold flex items-center gap-2">Live Status <span class="live-dot"></span></div>
                    <div class="text-white font-bold mt-1 text-sm">Mon\u2013Fri \u00b7 09:00\u201318:00 WIB</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Form + Address -->
    <section class="bg-white py-20 relative">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid lg:grid-cols-5 gap-10">
                <!-- Address card -->
                <div class="lg:col-span-2 reveal-left">
                    <div class="bg-gradient-to-br from-brand-dark via-brand-green to-brand-dark text-white rounded-3xl p-8 sm:p-10 relative overflow-hidden h-full">
                        <div class="absolute inset-0 dot-pattern" style="opacity:.04"></div>
                        <div class="absolute -top-10 -right-10 w-40 h-40 bg-brand-yellow/10 rounded-full blur-2xl"></div>
                        <div class="relative z-10">
                            <span class="inline-flex items-center gap-2 bg-white/10 border border-white/20 rounded-full px-3 py-1 text-brand-yellow text-xs font-semibold mb-6">
                                <i data-lucide="building-2" class="w-3.5 h-3.5"></i>
                                Headquarters
                            </span>
                            <h3 class="text-2xl font-extrabold mb-2">PT Teknologi Akanofa Mandala</h3>
                            <p class="text-white/60 text-sm mb-8">Jakarta-based, serving clients across 15+ countries.</p>

                            <div class="space-y-5">
                                <div class="flex gap-3">
                                    <div class="w-10 h-10 rounded-lg bg-white/5 flex items-center justify-center shrink-0"><i data-lucide="map-pin" class="w-5 h-5 text-brand-yellow"></i></div>
                                    <div class="text-sm leading-relaxed text-white/80">
                                        Infiniti Office, Bellezza BSA<br>Lt. 1 Unit 106, Jl. Letjen Soepeno<br>Kebayoran Lama Utara, Kebayoran Lama<br>Jakarta Selatan 12210, DKI Jakarta
                                    </div>
                                </div>
                                <div class="flex gap-3">
                                    <div class="w-10 h-10 rounded-lg bg-white/5 flex items-center justify-center shrink-0"><i data-lucide="briefcase" class="w-5 h-5 text-brand-yellow"></i></div>
                                    <div class="text-sm text-white/80">
                                        <div class="font-semibold text-white">PMDN \u00b7 KBLI 58200</div>
                                        <div class="text-white/60">Software Publishing</div>
                                    </div>
                                </div>
                            </div>

                            <a href="https://www.google.com/maps/search/?api=1&amp;query=Bellezza+BSA+Infiniti+Office+Jakarta" target="_blank" rel="noopener noreferrer" class="mt-8 inline-flex items-center gap-2 bg-brand-yellow text-brand-dark px-5 py-3 rounded-full font-semibold text-sm hover:bg-white transition-all group">
                                <i data-lucide="navigation" class="w-4 h-4"></i>
                                Get Directions
                                <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Contact form -->
                <div class="lg:col-span-3 reveal-right">
                    <div class="bg-white rounded-3xl p-8 sm:p-10 border border-gray-100 shadow-2xl shadow-brand-dark/10">
                        <h2 class="text-2xl sm:text-3xl font-extrabold text-brand-dark mb-2">Send us a message</h2>
                        <p class="text-gray-500 mb-8">We typically reply within 24 hours.</p>
                        <form id="contactForm" action="https://formsubmit.co/{EMAIL}" method="POST" class="space-y-5" autocomplete="on">
                            <input type="hidden" name="_subject" value="New Inquiry from Akanofa Website">
                            <input type="hidden" name="_template" value="table">
                            <input type="hidden" name="_captcha" value="true">
                            <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
                            <div class="grid sm:grid-cols-2 gap-4">
                                <div><label class="block text-sm font-medium text-brand-dark mb-1.5">First Name</label><input type="text" name="First Name" required maxlength="60" autocomplete="given-name" class="w-full px-4 py-3 rounded-xl border border-gray-200 bg-brand-cream focus:bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none transition-all text-brand-dark" placeholder="John"></div>
                                <div><label class="block text-sm font-medium text-brand-dark mb-1.5">Last Name</label><input type="text" name="Last Name" required maxlength="60" autocomplete="family-name" class="w-full px-4 py-3 rounded-xl border border-gray-200 bg-brand-cream focus:bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none transition-all text-brand-dark" placeholder="Doe"></div>
                            </div>
                            <div class="grid sm:grid-cols-2 gap-4">
                                <div><label class="block text-sm font-medium text-brand-dark mb-1.5">Business Email</label><input type="email" name="Email" required maxlength="120" autocomplete="email" class="w-full px-4 py-3 rounded-xl border border-gray-200 bg-brand-cream focus:bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none transition-all text-brand-dark" placeholder="john@company.com"></div>
                                <div><label class="block text-sm font-medium text-brand-dark mb-1.5">Company</label><input type="text" name="Company" maxlength="100" autocomplete="organization" class="w-full px-4 py-3 rounded-xl border border-gray-200 bg-brand-cream focus:bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none transition-all text-brand-dark" placeholder="Your Company"></div>
                            </div>
                            <div><label class="block text-sm font-medium text-brand-dark mb-1.5">How can we help?</label>
                                <select name="Service Interest" required class="w-full px-4 py-3 rounded-xl border border-gray-200 bg-brand-cream focus:bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none transition-all text-brand-dark">
                                    <option value="" disabled selected>Select a service</option>
                                    <option>AI &amp; Machine Learning</option><option>Cloud Solutions</option><option>Mobile Development</option><option>Cybersecurity</option><option>Data Engineering</option><option>DevOps &amp; Automation</option><option>Other</option>
                                </select>
                            </div>
                            <div><label class="block text-sm font-medium text-brand-dark mb-1.5">Project Details</label><textarea rows="4" name="Project Details" required maxlength="2000" class="w-full px-4 py-3 rounded-xl border border-gray-200 bg-brand-cream focus:bg-white focus:border-brand-green focus:ring-2 focus:ring-brand-green/20 outline-none transition-all text-brand-dark resize-none" placeholder="Tell us about your project..."></textarea></div>
                            <button type="submit" class="w-full bg-brand-dark text-white py-4 rounded-xl font-semibold hover:bg-brand-green transition-all duration-300 flex items-center justify-center gap-2 group">
                                Send Message <i data-lucide="send" class="w-5 h-5 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform"></i>
                            </button>
                            <p class="text-xs text-gray-400 text-center">Protected by honeypot + captcha. Your info is never shared.</p>
                        </form>
                        <div id="formSuccess" class="hidden text-center py-16">
                            <div class="w-20 h-20 bg-brand-green/10 rounded-full flex items-center justify-center mx-auto mb-4"><i data-lucide="check-circle" class="w-10 h-10 text-brand-green"></i></div>
                            <h3 class="text-2xl font-bold text-brand-dark mb-2">Message Sent!</h3>
                            <p class="text-gray-500">We'll get back to you within 24 hours.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Map Section -->
    <section class="bg-brand-cream py-20 relative overflow-hidden">
        <div class="absolute inset-0 dot-pattern"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center max-w-2xl mx-auto mb-10 reveal">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">Find Us</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-dark mb-3">Our office in <span class="text-gradient">Jakarta</span></h2>
                <p class="text-gray-500">Drop by for a coffee \u2014 we love meeting people in person.</p>
            </div>
            <div class="reveal rounded-3xl overflow-hidden shadow-2xl shadow-brand-dark/20 border-4 border-white">
                <iframe
                    title="Akanofa office location"
                    class="map-frame w-full"
                    height="450"
                    style="border:0; display:block;"
                    loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade"
                    src="https://www.google.com/maps?q=Bellezza+BSA+Infiniti+Office+Jl+Letjen+Soepeno+Kebayoran+Lama+Utara+Jakarta+Selatan&output=embed">
                </iframe>
            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="bg-white py-20 relative">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12 reveal">
                <span class="inline-block bg-brand-yellow-light text-brand-dark px-4 py-1.5 rounded-full text-sm font-semibold mb-4">FAQ</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-brand-dark">Common questions</h2>
            </div>
            <div class="space-y-3">
                <details class="reveal group bg-brand-cream rounded-2xl p-5 border border-gray-100 hover:border-brand-green/30 transition-all">
                    <summary class="flex items-center justify-between cursor-pointer font-semibold text-brand-dark list-none">How fast will I hear back? <i data-lucide="chevron-down" class="w-5 h-5 text-brand-green group-open:rotate-180 transition-transform"></i></summary>
                    <p class="text-gray-500 mt-3 text-sm leading-relaxed">We respond to all inquiries within 24 hours on business days. WhatsApp is fastest for urgent matters.</p>
                </details>
                <details class="reveal group bg-brand-cream rounded-2xl p-5 border border-gray-100 hover:border-brand-green/30 transition-all" style="transition-delay:.1s">
                    <summary class="flex items-center justify-between cursor-pointer font-semibold text-brand-dark list-none">Do you work with international clients? <i data-lucide="chevron-down" class="w-5 h-5 text-brand-green group-open:rotate-180 transition-transform"></i></summary>
                    <p class="text-gray-500 mt-3 text-sm leading-relaxed">Yes \u2014 we currently serve clients in 15+ countries with fully remote delivery and flexible timezone coverage.</p>
                </details>
                <details class="reveal group bg-brand-cream rounded-2xl p-5 border border-gray-100 hover:border-brand-green/30 transition-all" style="transition-delay:.2s">
                    <summary class="flex items-center justify-between cursor-pointer font-semibold text-brand-dark list-none">What does a typical engagement look like? <i data-lucide="chevron-down" class="w-5 h-5 text-brand-green group-open:rotate-180 transition-transform"></i></summary>
                    <p class="text-gray-500 mt-3 text-sm leading-relaxed">A free discovery call \u2192 scoped proposal \u2192 sprint-based delivery with weekly demos \u2192 launch \u2192 ongoing support.</p>
                </details>
                <details class="reveal group bg-brand-cream rounded-2xl p-5 border border-gray-100 hover:border-brand-green/30 transition-all" style="transition-delay:.3s">
                    <summary class="flex items-center justify-between cursor-pointer font-semibold text-brand-dark list-none">Is my information safe? <i data-lucide="chevron-down" class="w-5 h-5 text-brand-green group-open:rotate-180 transition-transform"></i></summary>
                    <p class="text-gray-500 mt-3 text-sm leading-relaxed">Absolutely. Our website enforces strict CSP, HTTPS, and form spam protection. We never share your information with third parties.</p>
                </details>
            </div>
        </div>
    </section>
"""

# ============================================================
# Page assembler
# ============================================================
def page(filename, title, active, body):
    html = head(title) + nav(active) + body + FOOTER + FLOATING + QUOTE_MODAL + SCRIPTS
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)

if __name__ == "__main__":
    page("index.html", "Akanofa | Intelligent Software, Built for Your Business", "home", INDEX_BODY + PROCESS_SECTION + WHAT_WE_DO_SECTION)
    page("services.html", "Services | Akanofa", "services", SERVICES_BODY)
    page("about.html", "About | Akanofa", "about", ABOUT_BODY)
    page("why-us.html", "Why Akanofa | Akanofa", "why-us", WHY_BODY)
    page("contact.html", "Contact | Akanofa", "contact", CONTACT_BODY)
    print("done")
