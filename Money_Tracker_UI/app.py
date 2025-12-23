from flask import Flask,render_template,request,url_for,redirect,session
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date

app=Flask(__name__)
app.secret_key="super-secret-key"

def get_db():
    conn=sqlite3.connect("money_manager.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn=get_db()
    conn.execute("""
                    CREATE TABLE IF NOT EXISTS transactions
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        amount INTEGER,
                        type TEXT,
                        category_id INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users(id),
                        FOREIGN KEY (category_id) REFERENCES categories(id)
                    )
                """)
    conn.execute("""
                    CREATE TABLE IF NOT EXISTS users
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
    conn.execute("""
                    CREATE TABLE IF NOT EXISTS categories
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        user_id INTEGER NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users(id)
                    )
                """)
    conn.commit()
    conn.close()
init_db()

@app.route("/",methods=["GET","POST"])
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    if request.method=="POST":
        amount=request.form.get("amount")
        if not amount or amount<=0:
            return "Amount must be greater than 0 and not null"
        ttype=request.form.get("transaction-type")
        category_id=request.form.get("category_id")
        if not category_id or ttype:
            return "Invalid transaction data"
        selected_date=request.form.get("date")
        if not selected_date:
            selected_date = date.today().isoformat()
        conn=get_db()
        conn.execute("INSERT INTO transactions (user_id,amount,type,category_id,date) VALUES (?,?,?,?,?)",(session["user_id"],amount,ttype,category_id,selected_date))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    
    conn=get_db()
    transactions = conn.execute("""
                                    SELECT 
                                        transactions.id,
                                        transactions.amount,
                                        transactions.type,
                                        transactions.date,
                                        categories.name AS category
                                    FROM transactions
                                    JOIN categories ON transactions.category_id = categories.id
                                    WHERE transactions.user_id = ?
                                    ORDER BY transactions.date DESC
                                """, (session["user_id"],)).fetchall()
    categories=conn.execute("SELECT * FROM categories WHERE user_id=?",(session["user_id"],)).fetchall()
    user=conn.execute("SELECT username FROM users WHERE id=?",(session["user_id"],)).fetchone()
    if not user:
        conn.close()
        session.pop("user_id", None)
        return redirect(url_for("login"))
    income_row = conn.execute(
                                """
                                SELECT SUM(amount) AS total_income
                                FROM transactions
                                WHERE user_id = ? AND type = 'income'
                                """,
                                (session["user_id"],)
                            ).fetchone()
    total_income=income_row["total_income"] or 0
    expense_row = conn.execute(
                                """
                                SELECT SUM(amount) AS total_expense
                                FROM transactions
                                WHERE user_id = ? AND type = 'expense'
                                """,
                                (session["user_id"],)
                            ).fetchone()
    total_expense=expense_row["total_expense"] or 0
    balance=total_income-total_expense
    conn.close()
    return render_template("index.html",transactions=transactions,categories=categories,username=user["username"],income=total_income,expense=total_expense,bal=balance)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        hashed_password=generate_password_hash(password)
        conn=get_db()
        try:
            conn.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists"
        conn.close()
        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        conn=get_db()
        user=conn.execute("SELECT * FROM users WHERE username=?",(username,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"],password):
            session["user_id"]=user["id"]
            return redirect(url_for("home"))
        return "INVALID USERNAME AND PASSWORD"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))

@app.route("/delete/<int:id>")
def delete_trans(id):
    conn=get_db()
    conn.execute("DELETE FROM transactions WHERE id =? AND user_id=?",(id,session["user_id"]))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

@app.route("/categories",methods=["GET","POST"])
def categories():
    if "user_id" not in session:
        return redirect(url_for("login"))
    
    conn=get_db()
    if request.method=="POST":
        name=request.form.get("name")

        conn.execute("INSERT INTO categories (name,user_id) VALUES (?,?)",(name,session["user_id"]))
        conn.commit()

    categories=conn.execute("SELECT * FROM categories WHERE user_id=?",(session["user_id"],)).fetchall()
    conn.close()
    return render_template("categories.html",categories=categories)

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404


if __name__=="__main__":
    app.run(debug=True)