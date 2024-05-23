from flask import Flask, render_template

app = Flask(__name__)

##-- IN POWERSHELL --##
#- $env:FLASK_APP = "server"
#- flask run

#- $env:FLASK_ENV="developer"  to turn on debug mode on.

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index.html")
def home_link():
    return render_template('index.html')

@app.route("/works.html")
def works_link():
    return render_template('works.html')

@app.route("/about.html")
def about_me_link():
    return render_template('about.html')

@app.route("/contact.html")
def contact_link():
    return render_template('contact.html')