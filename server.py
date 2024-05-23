from flask import Flask, render_template

app = Flask(__name__)

##-- IN POWERSHELL --##
#- $env:FLASK_APP = "server"
#- flask run

#- $env:FLASK_ENV="developer"  to turn on debug mode on.

@app.route("/")
def hello_world():
    return "<p>This is Bryan's Server!</p>"