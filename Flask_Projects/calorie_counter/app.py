from flask import Flask, render_template, url_for
from helper import users,user_keys,user_names
from form import Counter


app = Flask(__name__)
app.config["SERCET_KEY"] = "17c03ca41147650a9458dd14c8613265"

@app.route("/")
def index():
    return render_template("index.html",user_names=user_names)

@app.route("/user_info/<int:id>")
def user_info(id):
    return render_template("user_info.html",users=users[id],user_keys=user_keys)

@app.route("/add_user")
def add_user():
    return render_template("add_user.html")

    
if __name__ == "__main__":
    app.run(debug=True)