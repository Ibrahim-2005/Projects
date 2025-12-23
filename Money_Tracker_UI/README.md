# Money Manager — Flask Web Application

A full-stack **expense & income tracking web application** built using Flask, designed with user authentication, relational database modeling, and deployment best practices.

---

### 🔗 Live Demo:      👉 https://money-tracker-zcps.onrender.com   


---

### 📌 Features

* 🔐 User Authentication

    * Register, Login, Logout

    *  Secure password hashing

    * Session-based access control

* 👤 User-Specific Data

    * Each user sees only their own data

    * Protected routes to prevent data leakage

* 🗂️ Custom Categories

    * Users can create their own categories

    * Categories linked to transactions using foreign keys

* 💸 Transaction Management

    * Add income and expense transactions

    * Manual date selection with automatic fallback

    * Categorized transaction tracking

* 📊 Dashboard Summary

    * Total Income

    * Total Expense

    * Balance calculation

* 🛡️ Validation & Edge Case Handling

    * Prevents invalid or empty inputs

    * Handles stale sessions safely

    * Graceful error handling

* 🚀 Production Deployment

    * Deployed using Gunicorn

    * Hosted on Render

    * Environment variables used for secrets

---

### 🧠 Tech Stack

* Backend: Python, Flask

* Frontend: HTML, Jinja2 Templates

* Database: SQLite

* Authentication: Werkzeug Password Hashing

* Deployment: Gunicorn + Render

* Version Control: Git & GitHub

---

### 🗃️ Database Design (High Level)

* users

    * id, username, password, created_at

* categories

    * id, user_id, name

* transactions

    * id, user_id, category_id, amount, type, date

> Relational integrity is enforced using foreign keys, ensuring clean and secure data modeling.
---

# ⚙️ Local Setup Instructions

1. `git clone` "https://github.com/Ibrahim-2005/Projects.git"

2. `cd` Money_Tracker_UI

3. `pip install -r requirements.txt`

4. `python app.py`

### Open browser and visit:

http://127.0.0.1:5000



# 👤 Author

>Mohamed Ibrahim



---

## ⭐ If you like this project, give it a star on GitHub!
