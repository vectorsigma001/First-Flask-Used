from flask import Flask,render_template,request,flash
app=Flask(__name__)
app.secret_key="vector"

@app.route("/")
def index():
    return "Hello who is this"

@app.route("/hello")
def index1():
    flash("What's Your name")
    return render_template("index.html")

#interaction with server
@app.route("/greet",methods=["POST","GET"])
def greet():
    flash("Hi "+str(request.form['name_input'])+", great to see you")
    return render_template("index.html")      #name of your input
    