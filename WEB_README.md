# Calculator Plus - Web Demo

🧮 **Live Demo**: [Your Streamlit App URL]

A powerful web-based calculator with note-taking functionality, converted from the original Python desktop application.

## Features

- ✅ Basic arithmetic operations (+, -, ×, ÷)
- ✅ Advanced mathematical functions (sin, cos, tan, sqrt, log, exp)
- ✅ Parentheses and order of operations
- ✅ Pi (π) constant
- ✅ Power operations (^)
- ✅ Note-taking for each calculation
- ✅ Calculation history with timestamps
- ✅ Download history as JSON
- ✅ Mobile-friendly responsive design

## Demo Versions

This repository contains multiple versions of the calculator:

### Web Demo (Streamlit)
- **File**: `streamlit_demo.py` or `main.py`
- **Platform**: Streamlit Cloud
- **Features**: Full calculator functionality in web browser

### Static Web Demo (HTML/JS)
- **File**: `index.html`
- **Platform**: Any web server (GitHub Pages, Vercel, Netlify)
- **Features**: Pure HTML/JavaScript, no server required

### Desktop Application
- **File**: `calculator-plus-app.py`
- **Platform**: Windows/Mac/Linux with Python + tkinter
- **Features**: Original desktop GUI version

## Deployment Instructions

### For Streamlit Cloud:
1. Use `streamlit_demo.py` or `main.py` as your main file
2. Ensure `requirements.txt` is in the repository
3. Deploy to [share.streamlit.io](https://share.streamlit.io)

### For GitHub Pages:
1. Upload `index.html` to your repository
2. Enable GitHub Pages in repository settings
3. Access via `https://username.github.io/repository-name`

## Local Development

### Run Streamlit Demo:
```bash
pip install streamlit
streamlit run streamlit_demo.py
```

### Run HTML Demo:
```bash
python -m http.server 8000
# Open http://localhost:8000
```

### Run Desktop App:
```bash
python calculator-plus-app.py
```

## Technologies Used

- **Frontend**: Streamlit (Python) / HTML + CSS + JavaScript
- **Math Operations**: Python math library / JavaScript Math object
- **Data Storage**: Session state / Browser localStorage
- **Export**: JSON format

## Project Structure

```
CalculatorPlus/
├── streamlit_demo.py      # Streamlit web app
├── main.py               # Entry point for deployment
├── index.html            # Static HTML demo
├── calculator-plus-app.py # Original desktop app
├── requirements.txt      # Python dependencies
├── .streamlit/config.toml # Streamlit configuration
└── README.md             # This file
```

---

**Note**: When deploying to Streamlit Cloud, make sure to use `streamlit_demo.py` or `main.py` as your main file path, NOT `calculator-plus-app.py` (which is the desktop version).
