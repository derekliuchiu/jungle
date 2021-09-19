from flask import Flask
from flask import request
from database import MySQL

app = Flask(__name__)
db = MySQL('prices', '#eW2IV0pK&rH9&R65*IO')

@app.route("/get", methods = ["GET"])
def hello_world():
    asin = request.args.get('asin', '')
    if not asin:
        return {'error':'Bad asin value'}
    time = request.args.get('timestamp','')
    if not time:
        return {'error': 'Bad time value'}
    key = request.headers.get('authorization_key','')
    if not key:
        return {'error': 'Bad key value'}

    return db.get_price_date(asin, time)

@app.route("/insert", methods = ["POST"])
def product_insert():
    asin = request.form.get('asin', '')
    if asin:
        db.insert_product(asin)
        return "successfully inserted asin"
    else:
        return {'error': 'Asin not valid'}
