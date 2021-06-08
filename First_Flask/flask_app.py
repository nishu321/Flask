from flask import Flask,render_template

app = Flask(__name__)

info = {
    "name": "Nishu Mehta",
    "age": "27",
    "job": "Software-developer"
}

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",title="Home",greeting=True)

@app.route("/about")
def about():
    return render_template("about.html",title="About",info=info)

if __name__ == "__main__":
    app.run(debug=True)