from flask import Flask,render_template

#app = Flask(__name__,static_url_path="/public")  # the thing is before if u have to visit style.css in browser u only have to do 127.0.0.1:5000/static/style.css but now if u do that u can't access or see it for now u have to do 127.0.0.1:5000/public/style.css
app = Flask(__name__,static_folder="assets") #in this case we are chaging static folder location


@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(debug=True)