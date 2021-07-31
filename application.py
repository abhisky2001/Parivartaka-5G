import os
import re
import requests
import urllib.parse
from cs50 import SQL
from functools import wraps
from tempfile import mkdtemp
from flask_session import Session
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///buyer.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True
FOLDER = os.path.join('static')
app.config['UPLOAD_FOLDER'] =FOLDER
file = os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')
file2 = os.path.join(app.config['UPLOAD_FOLDER'], 'Name.png')
file3 = os.path.join(app.config['UPLOAD_FOLDER'], 'bg1.jpg')
file4 = os.path.join(app.config['UPLOAD_FOLDER'], 'btbg.jpg')
file5 = os.path.join(app.config['UPLOAD_FOLDER'], 'nfcbg.png')
file6 = os.path.join(app.config['UPLOAD_FOLDER'], 'bg2.JPEG')
file7 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.ico')
file8 = os.path.join(app.config['UPLOAD_FOLDER'], '5g1.jpg')
file9 = os.path.join(app.config['UPLOAD_FOLDER'], 'portable.png')
file10 = os.path.join(app.config['UPLOAD_FOLDER'], 'pbank.png')
file11 = os.path.join(app.config['UPLOAD_FOLDER'], 'power.png')
file12 = os.path.join(app.config['UPLOAD_FOLDER'], 'app.jpg')
file13 = os.path.join(app.config['UPLOAD_FOLDER'], 'track.png')
file14 = os.path.join(app.config['UPLOAD_FOLDER'], 'thin.png')
file15 = os.path.join(app.config['UPLOAD_FOLDER'], 'sim.png')
file16 = os.path.join(app.config['UPLOAD_FOLDER'], 'spec.png')
file17 = os.path.join(app.config['UPLOAD_FOLDER'], 'black.png')
file18 = os.path.join(app.config['UPLOAD_FOLDER'], 'white.png')
file19 = os.path.join(app.config['UPLOAD_FOLDER'], 'error.jpg')
file20 = os.path.join(app.config['UPLOAD_FOLDER'], 'order.jpg')

@app.route("/")
def homepage():
    return render_template("layout.html", Logo = file, Name = file2, bg1 = file3,
                            btbg = file4, nfc = file5, col = file6, ico = file7)

@app.route("/features")
def features():
    return render_template("features.html",Logo = file, Name = file2, bg1 = file3,
                            btbg = file4, nfc = file5, col = file6, ico = file7, cell = file8,
                            portable = file9, thin = file14, pbank = file10, power = file11,
                            track = file13, app = file12, sim = file15)

@app.route("/specs")
def specs():
    return render_template("specs.html",Logo = file, Name = file2, bg1 = file3,
                            btbg = file4, nfc = file5, col = file6, ico = file7, spec = file16)

@app.route("/pricing")
def pricing():
    return render_template("pricing.html", Logo = file, Name = file2, bg1 = file3,
                            btbg = file4, nfc = file5, col = file6, ico = file7, black = file17,
                            white = file18, spec = file16)


@app.route("/orders", methods=["GET", "POST"])
def orders():
    """View Ordered Items"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html",spec = file19)

        # Ensure email was submitted
        elif not request.form.get("email"):
            return render_template("error.html",spec = file19)

        # Retrieve orders of the user
        rows = db.execute("SELECT username, email, Product, qty, time FROM users WHERE username = :username", username=request.form.get("username"))
        return render_template("history.html", rows=rows, Logo = file, Name = file2, bg1 = file3,
                            btbg = file4, nfc = file5, col = file6, ico = file7, spec = file16)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", Logo = file, Name = file2, bg1 = file3,
                            btbg = file4, nfc = file5, col = file6, ico = file7, spec = file16)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Place Order for Black Color Device"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html",spec = file19)

        # Ensure email was submitted
        elif not request.form.get("email"):
            return render_template("error.html",spec = file19)

        # Ensure quantity was submitted
        elif not request.form.get("qty"):
            return render_template("error.html",spec = file19)

        # Insert into Database
        db.execute("INSERT INTO users (username, email, Product, qty) VALUES (:username, :email, :Product, :qty)",
                    username = request.form.get("username"),
                    email = request.form.get("email"),
                    Product = "Black and Red",
                    qty = request.form.get("qty"))

        # Redirect user to home page
        return render_template("order.html", order = file20)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html", Logo = file, Name = file2, bg1 = file3,
                            btbg = file4, nfc = file5, col = file6, ico = file7, spec = file16)

@app.route("/registerw", methods=["GET", "POST"])
def registerw():
    """Place Order for White Color Device"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("error.html",spec = file19)

        # Ensure email was submitted
        elif not request.form.get("email"):
            return render_template("error.html",spec = file19)

        elif not request.form.get("qty"):
            return render_template("error.html",spec = file19)

        db.execute("INSERT INTO users (username, email, Product, qty) VALUES (:username, :email, :Product, :qty)",
                    username = request.form.get("username"),
                    email = request.form.get("email"),
                    Product = "White Frost",
                    qty = request.form.get("qty"))

        # Redirect user to home page
        return render_template("order.html", order = file20)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("registerw.html", Logo = file, Name = file2, bg1 = file3,
                            btbg = file4, nfc = file5, col = file6, ico = file7, spec = file16)

