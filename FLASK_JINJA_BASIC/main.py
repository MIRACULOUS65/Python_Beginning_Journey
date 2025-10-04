from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "john":45,
        "a":39,
        "b":56
    }
    return render_template("index.html",marks=marks) 

app.run(debug=True)