import os

from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")
# Create tables needed for app to function
db.execute("CREATE TABLE IF NOT EXISTS 'users' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," +
           "'username' TEXT NOT NULL, 'hash' TEXT NOT NULL, 'cash' NUMERIC NOT NULL DEFAULT 10000.00)")
db.execute("CREATE TABLE IF NOT EXISTS 'transactions' ('trans_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," +
           "'date' DATETIME NOT NULL, 'cust_id' INTEGER NOT NULL,'shares' INTEGER NOT NULL," +
           "'stock' TEXT NOT NULL,'price' REAL NOT NULL)")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # get user cash amount
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                      user_id=session['user_id'])[0]['cash']

    # get user shares
    shares = db.execute("SELECT stock, SUM(shares) FROM transactions WHERE cust_id = :user_id GROUP BY stock",
                        user_id=session['user_id'])

    # calculate total value (balance + value of sum of shares)
    total = 0

    for t in shares:
        if t["SUM(shares)"]:
            stock = lookup(t['stock'])
            t['company'], t['price'], t['value'] = stock['name'], usd(stock['price']), usd(stock['price'] * t['SUM(shares)'])
            total += t['SUM(shares)'] * stock['price']

    transactions = [t for t in shares if t["SUM(shares)"] > 0]
    total += cash

    return render_template('index.html', cash=usd(cash), total=usd(total), transactions=transactions)


@app.route("/action", methods=["POST"])
@login_required
def action():
    """Instant buy/sell of stock"""
    return render_template("action.html", action=request.form.get("action"),
                           price=request.form.get("price"), symbol=request.form.get("symbol"))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Check if user entered a valid number
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology('Invalid number of shares given', 400)
        if shares <= 0:
            return apology('Negative number entered', 400)
        # Check whether user entered a valid stock symbol
        if lookup(request.form.get("symbol")):
            # Lookup price of chosen stock
            price = (lookup(request.form.get("symbol")))['price']
        else:
            return apology('Stock symbol "{}" invalid'.format(request.form.get("symbol")), 400)

        # Check whether user has enough cash to buy amount of desired stock
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])[0]['cash']

        # Check whether user has enough cash in account
        if shares * price <= cash:
            # subtract total amount from user's account
            db.execute("UPDATE users SET cash = :money WHERE id = :user_id",
                       money=cash - (shares * price), user_id=session["user_id"])
            # store new transaction into transactions table
            db.execute("INSERT INTO transactions (date, cust_id, shares, stock, price) " +
                       "VALUES (:date, :user_id, :shares, :stock, :price)",
                       date=datetime.strftime(datetime.now(), "%x %X"),
                       user_id=session["user_id"], shares=shares,
                       stock=request.form.get('symbol').upper(), price=price)
            # Return to index page
            return redirect("/")
        else:
            return apology("You can't afford this, SUCKER!")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # get user cash amount
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                      user_id=session['user_id'])[0]['cash']

    data = db.execute("SELECT date, shares, stock, price FROM transactions WHERE cust_id = :user_id ORDER BY stock",
                      user_id=session['user_id'])

    total = 0

    for t in data:
        # Retrieve stock info and prepare data
        stock = lookup(t['stock'])
        t['date'], t['time'] = t['date'].split()[0], t['date'].split()[1]
        t['company'], t['value'] = stock['name'], t['price'] * t['shares']
        total += t['value']
        t['value'], t['usdprice'] = usd(t['value']), usd(t['price'])

    total += cash

    return render_template('history.html', cash=usd(cash), total=usd(total), transactions=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Get request stock info from API
        quote = lookup(request.form.get("symbol"))
        if quote:
            # Load stock info page
            quote['price'] = usd(quote['price'])
            return render_template("quoted.html", quote=quote)
        else:
            # Apologize if user made a mistake, because the customer is always right :(
            return apology('"{}" stocks don\'t exist'.format(request.form.get("symbol")), 400)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Load search form
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure username doesn't exist
        elif len(db.execute("SELECT * FROM users WHERE username = :username",
                            username=request.form.get("username"))) != 0:
            return apology("username already exists", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirmation password was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # Ensure confirmation password matches password
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match", 400)

        # Add new user and hashed password to database
        db.execute("INSERT INTO users(username, hash) VALUES(:username, :hash)",
                   username=request.form.get("username"),
                   hash=generate_password_hash(request.form.get("password")))

        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "GET":
        shares = db.execute("SELECT stock, SUM(shares) FROM transactions WHERE cust_id = :user_id GROUP BY stock",
                            user_id=session['user_id'])

        if shares:
            return render_template("sell.html", shares=shares)
        else:
            return apology("You don't own any shares to sell")
    else:
        if not request.form.get("shares"):
            return apology("Please enter amount of shares")
        elif request.form.get("symbol") == "choose stock":
            return apology("Please select stock symbol")
        else:
            owned = db.execute("SELECT SUM(shares) FROM transactions WHERE cust_id = :user_id AND stock = :symbol",
                               symbol=request.form.get('symbol'), user_id=session['user_id'])[0]['SUM(shares)']
            if owned < int(request.form.get("shares")):
                return apology("You don't own that many shares")

        # Lookup price of selected stock
        price = lookup(request.form.get("symbol"))["price"]

        # Get user's current balance
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])[0]["cash"]

        # add total amount of shares to user's account
        db.execute("UPDATE users SET cash = :money WHERE id = :user_id",
                   money=cash + (int(request.form.get("shares")) * price), user_id=session["user_id"])

        # store new transaction into transactions table
        db.execute("INSERT INTO transactions (date, cust_id, shares, stock, price) " +
                   "VALUES (:date, :user_id, :shares, :stock, :price)",
                   date=datetime.strftime(datetime.now(), "%x %X"),
                   user_id=session["user_id"], shares=-(int(request.form.get("shares"))),
                   stock=request.form.get("symbol"), price=price)

        # Return to index page
        return redirect("/")


@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    """Change user settings"""

    user_info = db.execute("SELECT * from users WHERE id = :user_id",
                           user_id=session['user_id'])

    if request.method == "GET":
        return render_template("settings.html", username=user_info[0]['username'], hash=user_info[0]['hash'], cash=user_info[0]['cash'])

    else:
        # check whether username field is empty/changed
        if request.form.get('username') and request.form.get('username') != user_info[0]['username']:

            db.execute("UPDATE users SET username = :username WHERE id = :user_id",
                       username=request.form.get('username'), user_id=session['user_id'])

        if request.form.get('oldpwd') or request.form.get('password'):
            # check user given old_pwd against password in db
            if generate_password_hash(request.form.get('oldpwd')) != user_info[0]['hash']:
                # check whether new password is the same as the confirmation password
                if request.form.get('password') == request.form.get('confirmation') and request.form.get('password') != "":

                    db.execute("UPDATE users SET hash = :hash WHERE id = :user_id",
                               hash=generate_password_hash(request.form.get('password')), user_id=session['user_id'])
                else:
                    return apology("new and confirmation passwords don't match")
            else:
                return apology("old password incorrect")

        return redirect("/")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
