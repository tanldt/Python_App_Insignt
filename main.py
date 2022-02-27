import time
from applicationinsights.flask.ext import AppInsights
from flask import Flask


# create Flask app
app = Flask(__name__)
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = '8a40515e-a623-4956-9d6e-xxxxxxxx'
appinsights = AppInsights(app)


# force flushing application insights handler after each request
@app.after_request
def after_request(response):
    appinsights.flush()
    return response


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/fail')
def fail():
    a=1+b
    return 'Hello, World!'


@app.route('/sleep')
def sleep():
    time.sleep(2)
    return 'Hello, World + 2s!'

app.run()