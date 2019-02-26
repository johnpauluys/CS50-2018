from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

import sqlite3
from datetime import datetime, timedelta
from time import sleep

from helpers import create_db, db_open, db_close, login_required, time_now
from headache import report_headache, update_headache

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up/create database file
create_db()

# Configure app routes
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():

    # set sql ccommand
    sql_cmd = f"SELECT * FROM {session['user_table']}"
    # connect to db
    db, cur = db_open(row_dict=True)

    # check for unresolved headaches, there should always just be one
    cur.execute(sql_cmd + " WHERE duration IS 'unresolved'")
    # get rows
    unresolved = cur.fetchone()

    # if there is an unresolved headache, let user update/resolve it
    if unresolved:
        # close database connection before leaving page
        db.close()
        return render_template("update_headache.html", rows=unresolved)

    # get column names, not sure if this is overkill, but the idea of dynamism appeals to me.
    cols = [ k[0] for k in cur.description ]

    # fetch all rows
    cur.execute(sql_cmd + " WHERE duration IS NOT 'unresolved'")
    rows = cur.fetchall()
    db.close()

    return render_template('index.html', cols=cols, rows=rows)

@app.route('/headache', methods=['GET', 'POST'])
@login_required
def headache():
    if request.method == 'POST':
        if '_report_headache' in request.form:
            # if report a headache button was pressed
            return render_template('report_headache.html')

        if '_submit_headache' in request.form:
            # if a new headache has been submitted
            report_headache(session, request.form)
            return redirect("/")

        if '_update_headache' in request.form:
            # if an existing headache has been updated
            update_headache(session, request.form)
            return redirect("/")
    else:
        return render_template('report_headache.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Log user in """

    if request.method == 'POST':

        db, cur = db_open(row_dict=True)

        cur.execute("SELECT * FROM users WHERE username = :username", request.form)
        user_data = cur.fetchone()

        db.close()

        if user_data:
            # check entered password against saved one.
            if check_password_hash(user_data['password'], request.form.get("password")):
                # if password matches clear session
                session.clear()
                session['user_id'] = user_data['id']
                session['user_table'] = f"u_{user_data['id']}"
                session['user_name'] = f"{user_data['first_name']} {user_data['last_name']}"
                return redirect('/')
            else:
                # if password checking failed, let user know
                error_msg = "invalid password entered"
                return render_template('login.html', error_msg=error_msg, username=request.form['username'])
        else:
            # if username does not exist in db, let user know
            error_msg = f"username '{request.form['username']}' does not exist"
            return render_template('login.html', error_msg=error_msg)

    else:
        # if a user is already logged in, load homepage
        if 'user_id' in session:
            return redirect('/')
        # otherwise load login page
        else:
            return render_template('/login.html')

@app.route('/logout')
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # Prepare data from form to add to database
        user_data = {}
        for data in request.form:
            if data.endswith('_name'):
                user_data[data] = request.form[data].title()
            elif data == 'password':
                # generate password hash
                user_data[data] = generate_password_hash(request.form[data])
            elif data == 'confirmation':
                continue
            else:
                user_data[data] = request.form[data]


        db, cur = db_open()
        # insert a new user into users table
        cur.execute("""INSERT INTO users(
            first_name, middle_name, last_name, birthdate, email, mobile, username, password)
            VALUES(:first_name, :middle_name, :last_name, :birthdate, :email, :mobile, :username, :password)""", user_data)

        # create a reports table for new user
        cur.execute("""CREATE TABLE {}(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            duration TEXT NOT NULL DEFAULT "unresolved",
            location TEXT NOT NULL,
            type TEXT NOT NULL,
            intensity TEXT NOT NULL,
            additional_symptoms TEXT DEFAULT NULL,
            medication TEXT DEFAULT NULL,
            medication_effect TEXT DEFAULT NULL,
            routine_disruption TEXT DEFAULT NULL,
            hours_sleep TEXT DEFAULT NULL,
            food_before TEXT DEFAULT NULL,
            activities_before TEXT DEFAULT NULL,
            stressful_events TEXT DEFAULT NULL,
            comments TEXT DEFAULT NULL)""".format("u_" + str(cur.lastrowid)))

        # log user in by setting session user id
        user_id = cur.lastrowid
        session['user_id'] = user_id
        session['user_table'] = f"u_{user_id}"
        session['user_name'] = f"{user_data['first_name']} {user_data['last_name']}"
        db_close(db)


        return redirect('/')

    else:
        if 'user_id' in session:
            return redirect('/')
        else:
            return render_template('register.html')

@app.route('/checkusername/<username>', methods=["GET"])
# notice no trailing slash, try it with in the browser
def check_username(username):

    db, cur = db_open()
    cur.execute("SELECT username FROM users WHERE username = :username", {"username": username})
    result = cur.fetchall()
    db.close()
    if len(result) != 0:
        return "taken"
    else:
        return "free"

@app.route('/checkemail/<email>', methods=["GET"])
# notice no trailing slash, try it with in the browser
def check_email(email):

    db, cur = db_open()
    cur.execute("SELECT email FROM users WHERE email = :email", {"email": email})
    result = cur.fetchall()
    db.close()
    if len(result) != 0:
        return "taken"
    else:
        return "free"

@app.route('/settings', methods=['GET'])
def settings():
    return render_template('settings.html')