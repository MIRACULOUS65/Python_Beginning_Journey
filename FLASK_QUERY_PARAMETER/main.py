from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    name=12
    token=67000
    return render_template("index.html",name=name,token=token)

app.run(debug=True)