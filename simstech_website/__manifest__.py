# -*- coding: utf-8 -*-
{
    'name': 'Simstech Website Theme',
    'version': '19.0.1.0.0',
    'category': 'Website/Theme',
    'summary': 'Professional portfolio website theme for Jacob Sims - Engineering & Technology Consulting',
    'description': """
Simstech Website Theme
======================

A custom Odoo 19 website theme for Jacob Sims' engineering and technology 
consulting portfolio. Features:

* Modern, clean design with professional typography
* Custom brand colors (Signal Blue, Kinetic Orange)
* SEO-optimized templates with structured data (JSON-LD)
* Modular building blocks for flexible page construction
* Responsive design with mobile-first approach
* Accessible and performant

Brand Identity:
- Engineer-first, business-focused consulting
- Myrtle Beach, SC local presence
- Cloud architecture, observability, reliability engineering
- AI integration with LLM observability

Design Language:
- Clean, calm gradients
- Professional signature branding
- Minimal "boxiness" - open layouts
- Subtle motion cues
- Orange accents for energy/action
    """,
    'author': 'Jacob Sims',
    'website': 'https://simstech.cloud',
    'license': 'LGPL-3',
    'depends': [
        'website',
        'website_crm',  # For contact forms
    ],
    'data': [
        # SEO and meta
        'views/seo/seo_data.xml',
        # Views and templates
        'views/layout.xml',
        'views/snippets/snippets.xml',
        'views/snippets/s_hero.xml',
        'views/snippets/s_services.xml',
        'views/snippets/s_problems.xml',
        'views/snippets/s_work.xml',
        'views/snippets/s_approach.xml',
        'views/snippets/s_faq.xml',
        'views/snippets/s_contact.xml',
        'views/snippets/s_footer.xml',
        'views/pages/homepage.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # CSS/SCSS
            'simstech_website/static/src/scss/variables.scss',
            'simstech_website/static/src/scss/theme.scss',
            'simstech_website/static/src/scss/snippets.scss',
            # JS (if needed)
            'simstech_website/static/src/js/animations.js',
        ],
        'website.assets_wysiwyg': [
            # Snippet editor options
            'simstech_website/static/src/snippets/options.js',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

