# Simstech Brand Guide

**Jacob Sims — Engineering & Technology Consulting**  
*Myrtle Beach, SC*

---

## Brand Identity

### Positioning
- **Engineer-first, business-focused** consulting
- Practical systems that last, not buzzwords
- Builder mentality — advisory + hands-on delivery
- Local presence (Myrtle Beach, SC) with remote capability

### Tagline
> "Engineer first. I build systems that last."

### Voice & Tone
- **Calm & confident** — not salesy or hype-driven
- **Direct** — clear language, no jargon soup
- **Empathetic** — acknowledges real-world complexity
- **Practical** — focuses on outcomes, not theory

---

## Color Palette

### Primary Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Ink** | `#0B0F14` | Primary text, headings |
| **Charcoal** | `#111827` | Dark sections, footer |
| **Steel** | `#1F2937` | Cards, borders, secondary backgrounds |
| **Cloud** | `#F8FAFC` | Page backgrounds, light sections |
| **Fog** | `#6B7280` | Secondary text, descriptions |
| **Runway** | `#E5E7EB` | Borders, dividers, subtle lines |

### Accent Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Signal Blue** | `#2563EB` | Primary CTAs, links, active states |
| **Kinetic Orange** | `#F97316` | Highlights, energy accents, attention |

### Functional Colors

| Name | Hex | Usage |
|------|-----|-------|
| **Success** | `#10B981` | Positive states, confirmations |
| **Warning** | `#F59E0B` | Caution states |
| **Error** | `#EF4444` | Error states, destructive actions |

### Gradient Usage

**Hero Background:**
```scss
background:
  radial-gradient(1200px 600px at 80% -20%, rgba(#F97316, 0.18), transparent 40%),
  radial-gradient(800px 400px at 0% 0%, rgba(#2563EB, 0.18), transparent 45%),
  linear-gradient(180deg, #F8FAFC 0%, #F1F5F9 100%);
```

---

## Typography

### Font Family
**Inter** — Clean, modern, highly readable sans-serif

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Font Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | 400 | Body text |
| Medium | 500 | Subtle emphasis |
| Semibold | 600 | Buttons, labels |
| Bold | 700 | Headings |

### Font Sizes

| Element | Size | Line Height |
|---------|------|-------------|
| H1 (Hero) | 3.5rem (56px) | 1.25 |
| H2 (Section) | 2rem (32px) | 1.25 |
| H3 (Subsection) | 1.5rem (24px) | 1.25 |
| H4 (Card Title) | 1.25rem (20px) | 1.25 |
| Body | 1rem (16px) | 1.6 |
| Small | 0.875rem (14px) | 1.6 |
| XS | 0.75rem (12px) | 1.6 |

### Letter Spacing
- Headings: `-0.025em` (tight)
- Body: Normal

---

## Spacing System

### Section Padding
- Desktop: `7rem` (112px) top/bottom
- Mobile: `4rem` (64px) top/bottom

### Container
- Max width: `80rem` (1280px)
- Horizontal padding: `1.5rem` (24px)

### Border Radius

| Size | Value | Usage |
|------|-------|-------|
| SM | 0.5rem (8px) | Small elements |
| Base | 0.75rem (12px) | Default |
| LG | 1rem (16px) | Buttons, cards |
| XL | 1.5rem (24px) | Large cards |
| 2XL | 2rem (32px) | Hero elements |

---

## Components

### Buttons

**Primary (Signal Blue)**
- Background: `#2563EB`
- Text: White
- Padding: `0.75rem 2.25rem`
- Border radius: 1rem
- Hover: Slight lift (-1px) + shadow

**Secondary (Outlined)**
- Background: White
- Border: 1px solid `#E5E7EB`
- Text: Ink (`#0B0F14`)
- Hover: Slight lift + shadow

**Large Variant**
- Padding: `1rem 2.25rem`
- Border radius: 1.5rem

### Cards
- Background: White
- Border: 1px solid `#E5E7EB`
- Border radius: 1.5rem
- Padding: 1.5rem
- Hover: Lift (-2px) + shadow

### Pills/Tags
- Padding: `0.25rem 0.75rem`
- Border radius: Full (9999px)
- Border: 1px solid `#E5E7EB`
- Font size: 0.75rem

---

## Motion & Animation

### Transitions
- Fast: 150ms ease
- Base: 180ms ease
- Slow: 300ms ease

### Hover Effects
- **Rise**: `transform: translateY(-2px)` + shadow increase
- **Subtle rise**: `transform: translateY(-1px)`

### Page Load
- **Fade up**: Opacity 0→1, translateY(8px)→0 over 600ms

---

## Shadows

| Name | Value | Usage |
|------|-------|-------|
| SM | `0 1px 2px rgba(0,0,0,0.05)` | Subtle depth |
| Base | `0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.1)` | Default |
| MD | `0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.1)` | Hover states |
| LG | `0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.1)` | Elevated elements |

---

## Logo & Branding

### Logo File
`/static/src/img/jacob-sims-logo.png`

### Alt Text
"Jacob Sims – Engineering Systems Reliability"

### Favicon
Standard Odoo favicon with brand colors (optional customization)

---

## Service Area & Geography

### Primary Location
Myrtle Beach, SC

### Service Area
- **South Carolina Coast**: Charleston, Mount Pleasant, Myrtle Beach, Conway, Georgetown
- **North Carolina Coast**: Wilmington, Southport, Calabash
- **Remote**: Nationwide

### Geographic Keywords
- "Technology consulting Myrtle Beach"
- "Cloud consultant South Carolina"
- "Engineering consulting Grand Strand"
- "IT consultant Charleston to Wilmington"

---

## SEO Keywords

### Primary Keywords
- Technology consulting
- Engineering consulting
- Cloud architecture consulting
- Reliability engineering
- Observability consulting

### Secondary Keywords
- AI integration consulting
- LLM observability
- SaaS selection consulting
- Tool evaluation
- Infrastructure automation

### Industry Keywords
- Healthcare IT consulting
- Aviation systems engineering
- Hospitality technology
- Marketing technology (MarTech)
- Big data and analytics
- Network engineering
- Campus network design

### Local Keywords
- Myrtle Beach technology consultant
- South Carolina engineering consultant
- Grand Strand IT consulting
- Coastal Carolina tech consulting

---

## Content Guidelines

### Headings Style
- Use sentence case
- Be direct and benefit-focused
- Avoid jargon

### Body Copy
- Short paragraphs (2-3 sentences)
- Active voice
- Concrete examples over abstract claims

### CTAs
- Primary: "Start a conversation"
- Secondary: "See my work", "Learn more"
- Avoid: "Contact us", "Get started today!"

---

## File Structure

```
simstech_website/
├── __manifest__.py
├── BRAND_GUIDE.md          # This file
├── static/
│   └── src/
│       ├── scss/
│       │   ├── variables.scss   # Brand variables
│       │   ├── theme.scss       # Core styles
│       │   └── snippets.scss    # Snippet-specific styles
│       ├── js/
│       │   └── animations.js    # Motion effects
│       └── img/
│           ├── jacob-sims-logo.png
│           └── snippets_thumbs/
└── views/
    ├── layout.xml           # Global layout overrides
    ├── snippets/            # Building blocks
    └── pages/
        └── homepage.xml     # Main landing page
```

