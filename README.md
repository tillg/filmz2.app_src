# Filmz2 App Website

This is the official website for Filmz2, an iOS app for tracking movies and TV series. Built with [Pelican](https://getpelican.com/), a Python-based static site generator.

## Project Structure

```
.
├── src/              # Website source code
│   ├── content/      # Markdown content files
│   ├── theme/        # Custom theme files
│   └── ...           # Build configuration
└── doc/              # Project documentation
```

## Overview

The website serves as a landing page for the Filmz2 iOS app, featuring:
- App description and key features
- Privacy policy
- Support documentation
- Download links (App Store)

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tillg/filmz2.app_src.git
cd filmz2.app_src/src
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Local Development

### Build the Site

Using invoke:
```bash
invoke build
```

Using make:
```bash
make html
```

### Serve Locally

Start a local server with auto-reload:
```bash
invoke livereload
```

Or serve without auto-reload:
```bash
invoke serve
# or
make serve
```

The site will be available at `http://localhost:8000`

### Other Commands

Clean output directory:
```bash
invoke clean
# or
make clean
```

Build for production:
```bash
invoke preview
# or
make publish
```

## Detailed Structure

### Source Directory (`/src`)
```
src/
├── content/           # Markdown content files
│   ├── pages/        # Static pages (home, features, privacy, support)
│   ├── images/       # Images for content
│   └── extra/        # Extra files (CNAME, favicon, etc.)
├── theme/            # Custom theme
│   ├── templates/    # HTML templates
│   └── static/       # CSS, JS, images
├── output/           # Generated site (git-ignored)
├── pelicanconf.py    # Development configuration
├── publishconf.py    # Production configuration
├── tasks.py          # Invoke task definitions
└── Makefile          # Make commands
```

### Documentation Directory (`/doc`)
Project documentation, feature descriptions, and development notes will be stored here.

## Configuration

Main settings are in `pelicanconf.py`:
- Site name and description
- Menu items
- Social links
- Theme settings

Production settings in `publishconf.py`:
- Production URL
- Feed generation
- Analytics (if needed)

## Adding Content

1. Create new pages in `content/pages/` as Markdown files
2. Include metadata at the top:
```markdown
Title: Page Title
Slug: page-url

# Page Content Here
```

3. Rebuild the site to see changes

## Deployment

The site is configured to deploy to `filmz2.app`. Update the CNAME file in `content/extra/` if using a different domain.

For GitHub Pages deployment:
1. Build the site with production settings
2. Push the `output/` directory to your GitHub Pages branch

## License

This website is part of the Filmz2 project. See the main project repository for license information.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For questions about the website, please open an issue in this repository.
For app support, contact: support@filmz2.app