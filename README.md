# Internship Task 1 – Django HTML + CSS + Dynamic Data

## 📌 Project Overview
This is a simple Django project created as part of Internship Task 1.  
It demonstrates:
- Serving HTML (`task.html`) with **dynamic data** from Django views
- Using a **CSS file** for styling
- Creating routes (`/` and `/task/`) for easy navigation

---

## 📂 Project Structure
Task1/
│-- manage.py
│-- Task1/ # Main Django project settings
│-- task/ # Django app
│ │-- templates/
│ │ ├── index.html
│ │ └── task.html
│ │
│ │-- static/
│ │ └── style.css
│ │
│ ├── views.py
│ ├── urls.py
│
└── README.md

## 🚀 How to Run This Project

1️⃣ **Clone the Repository**

git clone https://github.com/nirdeshtiwari432/task.git
cd task
2️⃣ Create a Virtual Environment


python -m venv env
3️⃣ Activate the Virtual Environment

Windows (cmd)

env\Scripts\activate
Mac/Linux

source env/bin/activate
4️⃣ Install Django

pip install django
5️⃣ Run the Development Server

python manage.py runserver
Visit:

Home Page → http://127.0.0.1:8000/

Task Page → http://127.0.0.1:8000/task/

📝 Features
Dynamic Data Rendering → Titles & tasks passed from views.py to HTML

Static File Usage → CSS linked via {% static %}

Reusable Layout → Simple HTML/CSS structure for easy editing

📧 Author
Nirdesh Tiwari
