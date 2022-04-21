from os import environ
from flask import Flask
import bot2

app = Flask(__name__)

@app.route("/")
def home():
    bot2.main()
    return "Tweeting a picture..."

app.run(host= '0.0.0.0', port=environ.get('PORT'))