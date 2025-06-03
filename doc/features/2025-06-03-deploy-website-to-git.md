# Deploy Filmz2 Website to GitHub Pages

## Overview

This document describes the deployment process for the Filmz2 website, which involves automatically building the Pelican static site and deploying it to GitHub Pages whenever changes are pushed to the source repository.

### Goals
- Deploy the Pelican-generated site to GitHub Pages
- Make the site available at https://filmz2.app
- Host the generated HTML in the repository `tillg/filmz2.app`
- Automate deployment using GitHub Actions
- Follow the pattern established by https://github.com/tillg/grtnr.com_src

## Architecture

### Repository Structure
- **Source Repository**: `tillg/filmz2.app_src` (this repo)
  - Contains Pelican source files, content, and theme
  - Triggers automatic builds on push
- **Target Repository**: `tillg/filmz2.app`
  - Contains only the generated static HTML files
  - Serves the website via GitHub Pages

### Deployment Flow
1. Developer pushes changes to `filmz2.app_src`
2. GitHub Action triggers on push
3. Action builds the site using Pelican
4. Generated files are pushed to `filmz2.app` repository
5. GitHub Pages serves the updated site

## Step-by-Step Setup Guide

### 1. Create Target Repository

1. Go to GitHub and create a new repository named `filmz2.app`
2. Make it public (required for GitHub Pages with custom domain)
3. Do NOT initialize with README, .gitignore, or license
4. Leave it completely empty

### 2. Configure GitHub Pages in Target Repository

1. Go to Settings → Pages in the `filmz2.app` repository
2. Source: Deploy from a branch
3. Branch: `main` (or `master`)
4. Folder: `/ (root)`
5. Save the settings

### 3. Set Up Custom Domain

#### In GitHub:
1. In the `filmz2.app` repository settings
2. Go to Pages section
3. Under "Custom domain", enter: `filmz2.app`
4. Check "Enforce HTTPS"
5. Save

#### DNS Configuration:
Add the following DNS records for your domain:

**For apex domain (filmz2.app):**
```
Type: A
Name: @
Value: 185.199.108.153
       185.199.109.153
       185.199.110.153
       185.199.111.153
```

**For www subdomain (optional):**
```
Type: CNAME
Name: www
Value: tillg.github.io
```

### 4. Create GitHub Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Note: `Filmz2 Website Deployment`
4. Expiration: Choose appropriate (90 days or no expiration)
5. Select scopes:
   - `repo` (all)
   - `workflow`
6. Generate token and **save it securely**

### 5. Add Token to Source Repository Secrets

1. In `filmz2.app_src` repository, go to Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `DEPLOY_TOKEN`
4. Value: Paste the personal access token
5. Add secret

### 6. Create GitHub Actions Workflow

Create `.github/workflows/deploy.yml` in the source repository:

```yaml
name: Deploy Website

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout source
      uses: actions/checkout@v4
      
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        
    - name: Install dependencies
      run: |
        cd src
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        
    - name: Build website
      run: |
        cd src
        pelican content -s publishconf.py
        
    - name: Deploy to target repository
      env:
        DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
      run: |
        # Configure git
        git config --global user.email "github-actions[bot]@users.noreply.github.com"
        git config --global user.name "github-actions[bot]"
        
        # Clone target repository
        git clone https://${DEPLOY_TOKEN}@github.com/tillg/filmz2.app.git target
        
        # Clear old content (except CNAME and .git)
        cd target
        find . -maxdepth 1 ! -name '.git' ! -name 'CNAME' ! -name '.' -exec rm -rf {} +
        
        # Copy new content
        cp -r ../src/output/* .
        
        # Commit and push if there are changes
        git add -A
        if git diff --staged --quiet; then
          echo "No changes to deploy"
        else
          git commit -m "Deploy website - $(date +'%Y-%m-%d %H:%M:%S')"
          git push origin main
        fi
```

### 7. Update publishconf.py

Ensure your `src/publishconf.py` has the correct production URL:

```python
SITEURL = 'https://filmz2.app'
RELATIVE_URLS = False
```

### 8. Ensure CNAME File

The CNAME file is already in `src/content/extra/CNAME` and will be copied during build.

## Testing the Deployment

1. Make a small change to any content file
2. Commit and push to the `main` branch
3. Go to Actions tab in the source repository
4. Watch the workflow execute
5. Check the target repository for new commits
6. Visit https://filmz2.app to see your changes

## Troubleshooting

### Common Issues:

1. **Permission Denied**: Ensure the personal access token has correct permissions
2. **CNAME Missing**: Make sure CNAME file is in `content/extra/` and `EXTRA_PATH_METADATA` is configured
3. **404 Error**: Check GitHub Pages is enabled and pointing to correct branch
4. **DNS Not Resolving**: DNS changes can take up to 48 hours to propagate

### Checking Deployment Status:

1. GitHub Actions: Check workflow runs in Actions tab
2. GitHub Pages: Check deployment status in target repo Settings → Pages
3. DNS: Use `dig filmz2.app` or `nslookup filmz2.app` to verify DNS

## Maintenance

### Token Renewal
If using expiring tokens, set a reminder to renew before expiration.

### Monitoring
- Set up GitHub notifications for failed workflows
- Periodically check that the site is accessible
- Monitor GitHub Pages status: https://www.githubstatus.com/

## Security Considerations

1. Never commit the personal access token
2. Use repository secrets for sensitive data
3. Limit token permissions to minimum required
4. Consider using GitHub App tokens for production environments

## Alternative Deployment Options

### GitHub Deploy Keys
Instead of personal access tokens, you can use deploy keys:
1. Generate SSH key pair
2. Add public key to target repo as deploy key with write access
3. Add private key to source repo secrets
4. Modify workflow to use SSH for git operations

### Third-Party Services
- Netlify
- Vercel
- Cloudflare Pages

These offer additional features like preview deployments and enhanced analytics.