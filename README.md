# Simstech Website Theme for Odoo 19

A custom Odoo 19 website module for Jacob Sims' engineering and technology consulting portfolio at [simstech.cloud](https://simstech.cloud).

## Features

### Design Language
- **Modern, clean aesthetic** - Calm gradients, professional typography
- **Brand colors** - Signal Blue (#2563EB) + Kinetic Orange (#F97316)
- **Responsive** - Mobile-first with smooth breakpoints
- **Accessible** - Proper semantic HTML, ARIA labels, touch-friendly targets

### SEO Optimized
- **JSON-LD structured data** - ProfessionalService, Person, FAQPage schemas
- **Open Graph meta tags** - Social sharing optimization
- **Semantic HTML** - Proper heading hierarchy, landmark regions
- **Local SEO** - Myrtle Beach, SC geographic targeting

### Custom Building Blocks
The module provides drag-and-drop building blocks in the Odoo website editor:

| Snippet | Description |
|---------|-------------|
| **Hero** | Main landing section with logo, headline, CTAs, social proof |
| **Services** | 2-column grid listing core service offerings |
| **Problems** | Recognition triggers - problems visitors identify with |
| **Work** | Industry experience cards (Healthcare, Aviation, etc.) |
| **Approach** | Methodology cards + "what happens next" process |
| **FAQ** | Accordion-style FAQs with Schema.org markup |
| **Contact** | Dark CTA section with form integration |
| **Divider** | Gradient line separator |

### Brand Voice
- Engineer-first, business-focused
- Clear, direct communication
- Professional but approachable
- Builder mentality - not buzzwords

## Installation

### Prerequisites
- Odoo 19 Community or Enterprise
- `website` module installed
- `website_crm` module (for contact forms)

### Install via UI
1. Go to **Apps** → **Update Apps List**
2. Search for "Simstech Website"
3. Click **Install**

### Install via CLI
```bash
./odoo-bin -d your_database -i simstech_website
```

### Deploy with Docker/Kubernetes
Add to your Odoo addons path:
```yaml
volumes:
  - ./simstech-odoo-website:/mnt/extra-addons/simstech_website
```

## Module Structure

```
simstech_website/
├── __init__.py
├── __manifest__.py
├── static/
│   ├── src/
│   │   ├── scss/
│   │   │   ├── variables.scss    # Brand colors, typography, spacing
│   │   │   ├── theme.scss        # Core theme styles
│   │   │   └── snippets.scss     # Snippet-specific styles
│   │   ├── js/
│   │   │   └── animations.js     # Smooth scroll, fade-in effects
│   │   ├── snippets/
│   │   │   └── options.js        # Snippet editor options
│   │   └── img/
│   │       ├── jacob-sims-logo.png
│   │       ├── jacob-sims-signature.png
│   │       └── snippets/         # Snippet thumbnails
│   └── description/
│       ├── banner.png
│       └── icon.png
└── views/
    ├── layout.xml                # Layout overrides, navbar, footer
    ├── snippets/
    │   ├── snippets.xml          # Snippet registration
    │   ├── s_hero.xml
    │   ├── s_services.xml
    │   ├── s_problems.xml
    │   ├── s_work.xml
    │   ├── s_approach.xml
    │   ├── s_faq.xml
    │   └── s_contact.xml
    └── pages/
        └── homepage.xml          # Default homepage with SEO schemas
```

## Customization

### Colors
Edit `static/src/scss/variables.scss`:
```scss
$simstech-signal: #2563EB;    // Primary blue
$simstech-accent: #F97316;    // Orange accent
$simstech-ink: #0B0F14;       // Dark text
$simstech-cloud: #F8FAFC;     // Light background
```

### Content
All snippet text uses `o_default_snippet_text` class, making it editable directly in the Odoo website builder.

### Adding New Snippets
1. Create template in `views/snippets/s_yoursnippet.xml`
2. Add styles in `static/src/scss/snippets.scss`
3. Register in `views/snippets/snippets.xml`
4. Add to `__manifest__.py` data list

## SEO Configuration

### Structured Data
The homepage includes JSON-LD for:
- **ProfessionalService** - Business details, service areas
- **Person** - Personal branding
- **FAQPage** - FAQ content for rich snippets

### Meta Tags
Configure in Odoo:
1. **Website** → **Configuration** → **Settings**
2. Set default meta title, description
3. Add social media accounts

### Local SEO
- Geographic targeting: Myrtle Beach, SC
- Service area: South Carolina, United States
- Industry keywords in schema

## Development

### Local Testing
```bash
# Run Odoo with hot-reload
./odoo-bin -d test_db -i simstech_website --dev=all
```

### SCSS Compilation
Odoo compiles SCSS automatically. Clear assets cache after changes:
```
Settings → Technical → Assets Bundles → Clear Bundles
```

## License

LGPL-3.0

## Author

**Jacob Sims**  
Engineering & Technology Consulting  
Myrtle Beach, SC

- Website: [simstech.cloud](https://simstech.cloud)
- GitHub: [@jacobsims214](https://github.com/jacobsims214)

