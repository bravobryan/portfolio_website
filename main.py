from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.csv', 'a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f"\n{email},{subject},{message}")

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == "POST":
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect('/thankyou.html')
#     else:
#         return "Something went wrong, try again!"


##-- IN POWERSHELL --##
#- $env:FLASK_APP = "main"
#- flask run --debug

##-- Code for BASH --##
# git init
# git remote add origin {REMOTE_URL}
# git pull origin master
# git branch --set-upstream-to=origin/master master
# git pull
