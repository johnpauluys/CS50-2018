from flask import redirect, session
from functools import wraps
import sqlite3
from datetime import datetime

def create_db():
    """
        Create a new database if it doesn't exist
    """
    # connect to database
    db, cur = db_open()

    # create a users table
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                first_name TEXT NOT NULL,
                middle_name TEXT,
                last_name TEXT NOT NULL,
                birthdate TEXT NOT NULL,
                email TEXT NOT NULL,
                mobile TEXT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL)
                """)
    # close database
    db.close()


def db_open(row_dict=False):
    """
    Connect to db, return connection and cursor too shorten code slightly
    """
    conn = sqlite3.connect('mindmatters.db')
    # if needed for calling function, return a single row as a dict
    conn.row_factory = sqlite3.Row if row_dict else None
    cur = conn.cursor()

    return conn, cur


def db_close(conn):
    """
    Commit and close to shorten database related code slightly
    """
    conn.commit()
    conn.close()


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def time_now(string=False):
    """ Returns either a string or datetime object """
    # when a parameter is passed to function
    # return the desired format (full date and time, just the date or just the time)
    if string:
        if string == "full":
            return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        elif string == "date":
            return datetime.strftime(datetime.now(), "%Y-%m-%d")
        elif string == "time":
            return datetime.strftime(datetime.now(), "%H:%M:%S")
        else:
            raise ValueError(f"time_now(): \"{string}\" is an invalid argument. " \
                + "It has to be either \"full\", \"date\", \"time\" or left empty.")
    # otherwise return a datetime object of current time
    else:
        return datetime.now()
