from flask import Flask
from flask import request
from database import MySQL

app = Flask(__name__)
db = MySQL('prices', '#eW2IV0pK&rH9&R65*IO')

@app.route("/swag")
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