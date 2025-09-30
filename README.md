
# 🧾 Income Tax Calculator (India – Old Regime)

A simple and cleanly structured Income Tax Calculator for Indian taxpayers under the **Old Regime (as per Income Tax Act, 1961)**.  
This project includes both a **console-based version** and a **web version using Flask**, allowing users to calculate taxes interactively or via a browser.

---

## 📁 Project Structure

```
income-tax-calculator/
├── console_version/
│   └── tax_calculator.py
├── flask_version/
│   ├── main.py
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── templates/
│       ├── tax_form.html
│       ├── tax_result.html
│       ├── 404.html
│       └── 500.html
└── README.md
```

---

## 🧮 Console Version

- Built using **pure Python** (no external libraries)
- Interactive CLI prompts to enter income details
- Simple terminal-based tax output

### ▶️ Run the Console Version
```bash
cd console_version
python tax_calculator.py
```

---

## 🌐 Flask Web App Version

- Built using **Flask**
- Input form via browser; output displayed as an HTML page
- Handles all major income tax components: Basic exemption, slabs, surcharge, cess, etc.

### ▶️ Setup & Run (with Poetry)
```bash
cd flask_version
poetry install
poetry run python main.py
```

Or, if not using Poetry:
```bash
cd flask_version
pip install -r requirements.txt
python main.py
```

Then open your browser and visit:  
**http://127.0.0.1:5000/**

---

## 🧰 Requirements

- Python 3.8 or higher
- Flask (for web version)
- [Poetry](https://python-poetry.org/) (for dependency management)

---

## 🔗 Live Demo

🌐 [Try it on Replit](https://replit.com/join/idtzrvdtnm-satyamjhaa81)

---

## 👨‍💻 Author

**Satyam Jha**  
Aspiring Data Analyst | Python & SQL Learner  
📧 satyamjhaa81@gmail.com

---

## 📄 License

This project is open source. Feel free to use, modify, and share it for educational or personal purposes.
