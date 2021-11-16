from flask import Flask, request, render_template
from database import MySQL

app = Flask(__name__)
db = MySQL('Prices', '#eW2IV0pK&rH9&R65*IO')

@app.route("/get", methods = ["GET"])
def get_product():
    asin = request.args.get('asin', '')
    if not asin:
        return render_template("bad_value.html", value = "asin")

    # time = request.args.get('timestamp','')
    # if not time:
    #     return render_template("bad_value.html", value = "time")

    # key = request.headers.get('authorization_key','')
    # if not key:
    #     return {'error': 'Bad key value'}

    return db.get_price_date(asin) #no time parameter, might need to change so they can get price at specific time

@app.route("/insert", methods = ["POST"])
def product_insert():
    asin = request.form.get('asin', '')
    if asin:
        db.insert_product(asin)
        return "successfully inserted asin"
    else:
        return {'error': 'Asin not valid'}

@app.route("/", methods = ["GET"])
def home_page():
    return render_template("index.html")

@app.route("/table", methods = ["GET"])
def show_table():
    table = db.get_product_table()
    print(table)
    return render_template("table.html", table = table)

@app.route("/prices", methods = ["GET"])
def show_prices():
    table = db.get_price_date()
    print(table)
    return render_template("table.html", table = table)

