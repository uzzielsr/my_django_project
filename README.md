# 🐍 Django + Playwright UI Test Demo

This project demonstrates a basic Django app with functional UI tests using Playwright and pytest.

## 🚀 Tech Stack

- Python 3.13
- Django 5.2.3
- Playwright
- pytest

## 📁 Project Structure

```
my_django_project/
├── blog/
├── mysite/
├── ui_tests/
├── templates/
└── manage.py
```

## ▶️ How to Run

```bash
# Setup
python -m venv env
source env/bin/activate  # On macOS/Linux
# .\env\Scripts\activate  # On Windows (use this instead)
pip install -r requirements.txt
playwright install

# Run Django app
python manage.py migrate
python manage.py runserver

# Run UI Test
pytest -s ui_tests/test_home.py
```

## 🔌 How to Deactivate the Virtual Environment

To exit the Python virtual environment, simply run:

```bash
deactivate
```

## 🧪 Test Covers

- Page opens in Chromium
- Asserts greeting message
- Takes screenshot: `screenshots/test_homepage.png`

---

Created by Uzziel Sierra