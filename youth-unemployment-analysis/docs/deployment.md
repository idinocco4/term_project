# Deployment Guide: Running as GitHub Webpage

This guide explains how to deploy the Global Youth Unemployment Analysis as a working webpage on GitHub.

## 🚀 Quick Start Options

### Option 1: Static HTML Dashboard (Recommended for GitHub Pages)
The static HTML dashboard (`index.html`) works immediately on GitHub Pages.

1. **Upload to GitHub**: Push this repository to GitHub
2. **Enable GitHub Pages**: Go to Settings → Pages → Source: Deploy from a branch → Branch: main
3. **Access your site**: `https://yourusername.github.io/youth-unemployment-analysis/`

### Option 2: Streamlit Web App (Interactive)
For a fully interactive experience, deploy the Streamlit app.

#### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

#### Deploy to Streamlit Cloud
1. Create account at [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub repository
3. Deploy the app (main file: `app.py`)

## 📋 Detailed Deployment Steps

### GitHub Pages Setup (Static Website)

1. **Create GitHub Repository**
   ```bash
   # Initialize git if not already done
   git init
   git add .
   git commit -m "Initial commit: Youth unemployment analysis dashboard"
   git branch -M main
   git remote add origin https://github.com/yourusername/youth-unemployment-analysis.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click "Settings" tab
   - Scroll down to "Pages" section
   - Under "Source", select "Deploy from a branch"
   - Select "main" branch and "/ (root)" folder
   - Click "Save"

3. **Access Your Website**
   - Wait 2-3 minutes for deployment
   - Visit: `https://yourusername.github.io/youth-unemployment-analysis/`
   - The `index.html` file will be served as your homepage

### Streamlit Cloud Deployment (Interactive App)

1. **Prepare Your App**
   - Ensure `app.py` exists and works locally
   - Update any hardcoded paths to work with Streamlit Cloud

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository: `yourusername/youth-unemployment-analysis`
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Access Your App**
   - Streamlit will provide a URL like: `https://youth-unemployment-analysis.streamlit.app`

## 🔧 Configuration Files

### GitHub Pages Configuration
- `_config.yml`: Jekyll configuration for GitHub Pages
- `.github/workflows/deploy.yml`: Automated deployment workflow

### Streamlit Configuration
- `app.py`: Main Streamlit application
- `requirements.txt`: Python dependencies including Streamlit

## 🌐 Website Features

### Static HTML Dashboard (`index.html`)
- ✅ Works immediately on GitHub Pages
- ✅ No server required
- ✅ Fast loading
- ✅ Mobile responsive
- ⚠️ Limited interactivity (static charts)

### Streamlit Web App (`app.py`)
- ✅ Fully interactive
- ✅ Dynamic data exploration
- ✅ Real-time updates
- ✅ Advanced filtering
- ⚠️ Requires hosting service (not GitHub Pages)

## 📊 Data Requirements

### For Static HTML Version
- Sample data is embedded in JavaScript
- For live data, modify the `sampleData` object in `index.html`
- Or load data dynamically with JavaScript

### For Streamlit Version
- Requires `data/youth_unemployment_cleaned.csv`
- Ensure data file is included in repository
- Streamlit Cloud has file size limits (max 200MB)

## 🔍 Troubleshooting

### GitHub Pages Issues
- **404 Error**: Wait 5-10 minutes after enabling Pages
- **Blank Page**: Check that `index.html` is in the root directory
- **Styles Not Loading**: Ensure CSS is inline or paths are correct

### Streamlit Issues
- **Import Errors**: Check `requirements.txt` matches your local environment
- **Data Not Loading**: Ensure CSV file path is correct
- **Memory Errors**: Reduce data size or optimize loading

### Common Issues
- **Repository Name**: Update `baseurl` in `_config.yml` to match your repo name
- **Branch Name**: Ensure you're pushing to the correct branch (main/master)
- **File Permissions**: Ensure all files are committed and pushed

## 🎨 Customization

### Styling
- **HTML Version**: Modify CSS in `<style>` tags
- **Streamlit Version**: Add custom CSS with `st.markdown()` and `<style>` tags

### Data Updates
- **HTML Version**: Update the `sampleData` JavaScript object
- **Streamlit Version**: Replace the CSV file or modify data loading logic

### New Features
- **HTML Version**: Add new JavaScript functions and HTML elements
- **Streamlit Version**: Extend the `app.py` file with new components

## 📞 Support

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Check the main README.md for project details
- **Streamlit Docs**: Visit [docs.streamlit.io](https://docs.streamlit.io) for Streamlit help

## 🚀 Alternative Hosting Options

If GitHub Pages doesn't meet your needs:

- **Netlify**: Drag-and-drop deployment, great for static sites
- **Vercel**: Similar to Netlify, good for static content
- **Heroku**: Supports Streamlit apps, more configuration required
- **AWS/GCP/Azure**: Enterprise-grade hosting solutions

---

*Ready to deploy? Push your code to GitHub and enable Pages! 🎉*
