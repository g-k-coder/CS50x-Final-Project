from flask import redirect, render_template, session
from functools import wraps

""" Feedback upon receiving bad request """


def error(feedback_message, code):
    def format_message(feedback_message):
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"), ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            feedback_message = feedback_message.replace(old, new)
        return feedback_message
    return render_template("error.html", top=code, bottom=format_message(feedback_message)), code


""" Helper function to ensure that user is logged in. """
""" https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator """


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

