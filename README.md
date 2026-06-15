# TODO-APP

A simple TODO application built with Django. This is a **server-rendered web app** (using Django templates, HTML, CSS/SCSS, and JavaScript for the frontend) — **not an API**. There are no REST/JSON endpoints exposed; all pages are rendered directly by Django views.

## Features

- User account management (registration/login via the `account` app)
- Create, view, and manage TODO tasks (`todo` app)
- Server-rendered HTML pages using Django templates
- Static assets (CSS/SCSS, JS) for styling and interactivity

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, SCSS, JavaScript (rendered server-side via Django templates)
- **Database:** SQLite (`db.sqlite3`)

## Project Structure
TODO-APP/
├── account/        # User account app
├── doing/          # Tasks app 
├── staticfiles/     # Static assets (CSS, JS)
├── templates/       # HTML templates
├── todo/            # Main app
├── manage.py
├── requirements.txt
└── db.sqlite3

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
git clone https://github.com/alit83/TODO-APP.git
cd TODO-APP
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the App

```bash
python manage.py migrate
python manage.py runserver
```

Then open your browser at `http://127.0.0.1:8000/`.

## Screenshots
<img width="1349" height="871" alt="Screenshot 2026-06-15 224709" src="https://github.com/user-attachments/assets/b63ad3a9-70cf-406c-99c3-fc24cfd53842" />

> _Add a screenshot of the app below to showcase the UI._

![App Screenshot](path/to/your/screenshot.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
