🧾 README.md

# 📝 Flask NotePad App

A simple CRUD NotePad web app built with **Flask** and **SQLAlchemy**.  
You can create, read, update, and delete notes — all stored locally in a SQLite database.

---

## 🚀 Features
- Create new notes
- View full note content
- Edit and delete notes
- Simple and clean UI
- Uses SQLAlchemy ORM for database management

---

## 🛠️ Tech Stack
- **Python 3**
- **Flask**
- **SQLAlchemy**


---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ArjhayDeChavez/NotePad.git
   cd NotePad

2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Android/Termux use: source venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


4. Run the app

flask run



Then open your browser to http://127.0.0.1:5000.


---

🧩 Folder Structure

NotePad/
│
├── app.py
├── models.py
├── routes.py
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── read.html
│   ├── edit.html
│   └── create.html
├── requirements.txt
└── README.md


