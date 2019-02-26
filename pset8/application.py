import os
import re
from flask import Flask, jsonify, render_template, request

from cs50 import SQL
from helpers import lookup

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mashup.db")


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Render map"""
    return render_template("index.html")


@app.route("/articles")
def articles():
    """Look up articles for geo"""

    # Ensure parameters are present
    if not request.args.get("geo"):
        raise RuntimeError("missing geo")

    # Lookup articles
    articles = lookup(request.args.get("geo"))

    # Output articles as JSON
    return jsonify(articles[:5])


@app.route("/search")
def search():
    """Search for places that match query"""

    # Ensure parameteres are present
    if not request.args.get("q"):
        raise RuntimeError("missing q")

    # Clean up and simplify search query
    query = ""
    for c in request.args.get("q"):
        if c.isalnum() or c in ['-', '.']:
            query += c
        else:
            query += ' '

    # Split search query into single words
    query = query.split()

    # Compile regex string formats
    ll = re.compile(r'^-?\d{1,3}.\d*$')  # lats & longs
    pc = re.compile(r'^\d{1,5}$')        # postal codes
    cd = re.compile(r'^\D{2}$')          # country/state codes

    # Create SQL command string
    sql_cmd = "SELECT * FROM places WHERE"

    for i in range(len(query)):
        # Check if string is postal code
        if pc.search(query[i]):
            sql_cmd += " postal_code LIKE '" + query[i] + "%'" \

        # Check if string is lat or long
        elif ll.search(query[i]):
            sql_cmd += " (longitude LIKE '" + query[i] + "%'" \
                       " OR latitude LIKE '" + query[i] + "%')"
        # Check if string is a country/state code
        elif cd.search(query[i]):
            sql_cmd += " (country_code = '" + query[i].upper() + "' OR " \
                       " admin_code1 = '" + query[i].upper() + "')"

        # Check is string is anything other than the above
        else:
            sql_cmd += " (place_name LIKE '%" + query[i] + "%'" \
                       " OR admin_name1 LIKE '%" + query[i] + "%')"

        # Add AND to end of string, before adding more commands
        if i != len(query) - 1:
            sql_cmd += " AND"

    # Execute SQL command
    results = db.execute(sql_cmd)

    # Return jsonified results
    return jsonify(results)


@app.route("/update")
def update():
    """Find up to 10 places within view"""

    # Ensure parameters are present
    if not request.args.get("sw"):
        raise RuntimeError("missing sw")
    if not request.args.get("ne"):
        raise RuntimeError("missing ne")

    # Ensure parameters are in lat,lng format
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("sw")):
        raise RuntimeError("invalid sw")
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("ne")):
        raise RuntimeError("invalid ne")

    # Explode southwest corner into two variables
    sw_lat, sw_lng = map(float, request.args.get("sw").split(","))

    # Explode northeast corner into two variables
    ne_lat, ne_lng = map(float, request.args.get("ne").split(","))

    # Find 10 cities within view, pseudorandomly chosen if more within view
    if sw_lng <= ne_lng:

        # Doesn't cross the antimeridian
        rows = db.execute("""SELECT * FROM places
                          WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude AND longitude <= :ne_lng)
                          GROUP BY country_code, place_name, admin_code1
                          ORDER BY RANDOM()
                          LIMIT 10""",
                          sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    else:

        # Crosses the antimeridian
        rows = db.execute("""SELECT * FROM places
                          WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude OR longitude <= :ne_lng)
                          GROUP BY country_code, place_name, admin_code1
                          ORDER BY RANDOM()
                          LIMIT 10""",
                          sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    # Output places as JSON
    return jsonify(rows)
