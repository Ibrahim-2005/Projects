from flask import Flask,render_template,request,url_for,redirect,session
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)


def get_db():
    conn=sqlite3.connect("money_manager.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn=get_db()
    conn.execute("""
                    CREATE TABLE IF NOT EXISTS transactions
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount INTEGER,
                        type TEXT
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
    conn.commit()
    conn.close()
init_db()

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        amount=request.form.get("amount")
        ttype=request.form.get("transaction-type")
        conn=get_db()
        conn.execute("INSERT INTO transactions (amount,type) VALUES (?,?)",(amount,ttype))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    
    conn=get_db()
    transactions=conn.execute("SELECT * FROM transactions").fetchall()
    conn.close()
    return render_template("index.html",transactions=transactions)

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
        redirect(url_for("home"))
    return render_template("register.html")

@app.route("/delete/<int:id>")
def delete_trans(id):
    conn=get_db()
    conn.execute("DELETE FROM transactions WHERE id =?",(id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True)