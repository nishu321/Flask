from flask import Flask, render_template, url_for
from helper import users 
from form import Counter

app = Flask(__name__)
app.config["SERCET_KEY"] = "17c03ca41147650a9458dd14c8613265"

@app.route("/")
def index():
    return render_template("index.html",users=users)

if __name__ == "__main__":
    app.run(debug=True)