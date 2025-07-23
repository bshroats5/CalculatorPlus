# Calculator Plus - Demo Deployment Guide

This guide shows you how to set up online demo links for your Calculator Plus app.

## Option 1: Streamlit Cloud (Recommended for Python apps)

### Steps:
1. **Create a GitHub repository:**
   - Go to GitHub.com and create a new repository
   - Upload these files: `streamlit_demo.py` and `requirements.txt`

2. **Deploy on Streamlit Cloud:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and set main file path to `streamlit_demo.py`
   - Click "Deploy"

3. **Your demo will be available at:**
   `https://[your-app-name].streamlit.app`

### Benefits:
- Free hosting
- Automatic deployments from GitHub
- Python-based (matches your original app)
- Built-in sharing features

---

## Option 2: GitHub Pages (For HTML version)

### Steps:
1. **Create a GitHub repository:**
   - Upload the `index.html` file
   - Go to repository Settings → Pages
   - Select "Deploy from a branch" → "main"
   - Select "/ (root)" folder

2. **Your demo will be available at:**
   `https://[your-username].github.io/[repository-name]`

### Benefits:
- Completely free
- Works on any device with a browser
- No server required
- Fast loading

---

## Option 3: Local Demo Server

### For Streamlit version:
```bash
# Install Streamlit
pip install streamlit

# Run the demo
streamlit run streamlit_demo.py
```

### For HTML version:
```bash
# Python simple server
python -m http.server 8000

# Then open: http://localhost:8000
```

---

## Option 4: Other Free Hosting Platforms

### Vercel (for HTML):
1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Deploy automatically

### Netlify (for HTML):
1. Go to [netlify.com](https://netlify.com)
2. Drag and drop your `index.html` file
3. Get instant demo link

### Heroku (for Streamlit):
1. Create `Procfile`: `web: streamlit run streamlit_demo.py --server.port=$PORT --server.address=0.0.0.0`
2. Deploy to Heroku

---

## Demo Features Comparison

| Feature | Original Desktop App | Streamlit Demo | HTML Demo |
|---------|---------------------|----------------|-----------|
| Basic calculations | ✅ | ✅ | ✅ |
| Advanced functions | ✅ | ✅ | ✅ |
| Note-taking | ✅ (local files) | ✅ (session) | ✅ (browser) |
| History | ✅ | ✅ | ✅ |
| File export | ✅ | ✅ (JSON) | ✅ (JSON) |
| Cross-platform | Windows/Mac/Linux | Any browser | Any browser |

---

## Quick Start Instructions

### Fastest Option (HTML Demo):
1. Upload `index.html` to any web server
2. Share the URL - that's it!

### Best Option (Streamlit):
1. Create GitHub repo with `streamlit_demo.py` and `requirements.txt`
2. Deploy on Streamlit Cloud
3. Share your Streamlit app URL

---

## Tips for Demo Success

1. **Add screenshots** to your GitHub README
2. **Include instructions** on how to use the calculator
3. **Mention key features** like note-taking and history
4. **Test on mobile** - both demos are mobile-friendly
5. **Share the demo link** on social media, portfolio, or resume

---

## Example Demo URLs

Once deployed, your demos might look like:
- Streamlit: `https://calculator-plus-demo.streamlit.app`
- GitHub Pages: `https://yourusername.github.io/calculator-plus`
- Vercel: `https://calculator-plus.vercel.app`

Choose the option that best fits your needs and technical comfort level!
