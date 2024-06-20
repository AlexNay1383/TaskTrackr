from flask import Flask, redirect, url_for, session, render_template, request, flash
from datetime import timedelta

from login_funcs import *
from crypt_funcs import secure_hash
from classes import User
from mongodb import *

app = Flask(__name__)
with open("keys/secret_key.txt") as k:
    app.secret_key = k.read()
app.permanent_session_lifetime = timedelta(days=3)

@app.route("/")
def main_page():
    return redirect(url_for("login"))


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        phash = secure_hash(request.form["password"])

        if get_user({"email": email}) is None:
            flash("Wrong email or password")
            return redirect(url_for("login"))

        if get_user({"email": email})["password_hash"] != phash:
            flash("Wrong email or password")
            return redirect(url_for("login"))

        session.permanent = True
        session["email"] = email
        session["phash"] = phash
        return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        phash = secure_hash(request.form["password"])
        phashc = secure_hash(request.form["confirm-password"])

        if not is_valid_email(email):
            flash("Invalid email")
            return redirect(url_for('signup'))

        if get_user({"email": "FUCK U"}) is not None:
            flash("Email already taken")
            return redirect(url_for("signup"))
        
        if phash != phashc:
            flash("Passwords don't match")
            return redirect(url_for("signup"))
        
        strenght = strenght_password(request.form["password"])
        if strenght != "Strong":
            flash(strenght)
            return redirect(url_for("signup"))

        newuser = User(request.form["username"], email, phash)

        add_user(newuser)

        session["email"] = email
        session["phash"] = phash

        return redirect(url_for("home"))
    else:
        return render_template("signup.html")


@app.route("/home/")
def home():
    if "email" and "phash" in session:
        if get_user({"email": session["email"]}):
            return render_template("home2.html")
    return redirect(url_for("login"))

@app.route("/logout/")
def logout():
    if "email" and "phash" in session:
        session.pop("email")
        session.pop("phash")
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)