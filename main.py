from flask import Flask, render_template

app = Flask(__name__)

##-- IN POWERSHELL --##
#- $env:FLASK_APP = "server"
#- flask run

#- $env:FLASK_ENV="developer"  to turn on debug mode on.

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

#this is a note