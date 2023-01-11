from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>App is live</p>"

@app.route("/grab-data", method=['GET'])
def grab_data():

    return 