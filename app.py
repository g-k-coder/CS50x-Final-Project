import os
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from cs50 import SQL

from helpers import error, login_required

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///done.db")


@app.after_request
def after_request(response):
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/todo", methods=["GET", "POST"])
@login_required
def todo():

    username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]

    todo = db.execute("SELECT activity FROM ?", username)

    tasks = []

    # Render todo list if existing
    if len(todo):
        for activity in todo:
            tasks.append(activity['activity'])

    # Get input
    input = request.form.get("task")

    if request.method == "GET" or not input:
        return render_template("todo.html", tasks=tasks)

    # Write to database if activity is not on the list
    if not len(db.execute("SELECT activity FROM ? WHERE activity=?", username, input)):
        db.execute("INSERT INTO ? (activity) VALUES (?)", username, input)
        tasks.append(input)

    return redirect('/todo')

# Delete given activity from the users table in the database


@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == 'GET':
        return redirect('/todo')

    task = request.form.get("task")
    user = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]['username']

    # Check if input field is empty
    if not len(task):
        return redirect('/todo')

    db.execute("DELETE FROM ? WHERE activity = ?", user, task)

    return redirect('/todo')


# Render edit.html with default activity value
@app.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
    if request.method == 'GET':
        return redirect('/todo')

    username = db.execute("SELECT username FROM users WHERE id = ?", session['user_id'])[0]['username']

    task = request.form.get("task")

    if not len(task):
        return redirect('/todo')

    session['recent_id'] = db.execute("SELECT id FROM ? WHERE activity = ?", username, task)[0]['id']

    return render_template("edit.html", task=task)

# Edit task and update done.db


@app.route("/alter-edit", methods=["GET", "POST"])
@login_required
def alter():
    if request.method == 'GET':
        return redirect('/todo')

    username = db.execute("SELECT username FROM users WHERE id = ?", session['user_id'])[0]['username']
    task = request.form.get("task")

    if not len(task):
        return redirect('/todo')

    db.execute("UPDATE ? SET activity = ? WHERE id = ?", username, task, session['recent_id'])

    # Reset activity id
    session['recent_id'] = None

    return redirect('/todo')


@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return error("must provide username", 400)
        elif not password:
            return error("must provide password", 400)

        users = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(users) != 1 or not check_password_hash(users[0]["hash"], request.form.get("password")):
            return error("invalid username and/or password", 400)

        session["user_id"] = users[0]["id"]
        return redirect("/todo")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


""" Functions register() and password() were recycled from my submission of the problem set 9/finance. No code has been plagiarized. """


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    # Get passwords and username
    username = request.form.get("username").strip()
    initPass = request.form.get("password").strip()
    confirmPass = request.form.get("confirmation").strip()

    # Search database for the username
    usersDB = db.execute(
        "SELECT username FROM users WHERE username = ?", username)

    # Sequence of conditionals to ensure that everything is in order
    if not username.isalpha():
        return error("username must only contain Latin letters", 400)
    elif not username:
        return error("must provide username", 400)
    elif not initPass:
        return error("must provide password", 400)
    elif not initPass == confirmPass:
        return error("passwords must match", 400)
    elif len(usersDB):
        return error("username already in use", 400)

    # Hash passwords
    hashPass = generate_password_hash(
        initPass, method="pbkdf2:sha256", salt_length=8)

    # Insert user in database
    db.execute("INSERT INTO users(username, hash) VALUES (?,?)",
               username, hashPass)
    db.execute(
        "CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, activity TEXT NOT NULL)", username)

    # Log user in
    user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
    session["user_id"] = user_id[0]["id"]

    return redirect("/todo")


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Change user"s password"""
    if request.method == "GET":
        return render_template("password_change.html")

    username = db.execute(
        "SELECT username, hash FROM users WHERE id = ?", session["user_id"])
    old_hash = username[0]["hash"]
    username = username[0]["username"]

    if not check_password_hash(old_hash, request.form.get("old_password")):
        return error("incorrect current password", 400)

    password = request.form.get("password")
    confirm_password = request.form.get("confirmation")

    if password != confirm_password:
        return error("passwords do not match", 400)

    new_hash = generate_password_hash(
        password, method="pbkdf2:sha256", salt_length=8)

    session.clear()
    db.execute("UPDATE users SET hash = ? WHERE username = ?",
               new_hash, username)

    # Log user in
    user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
    session["user_id"] = user_id[0]["id"]

    db.execute("UPDATE users SET hash = ? WHERE username = ?",
               generate_password_hash(password, method="pbkdf2:sha256", salt_length=8), username)

    return redirect("/todo")
