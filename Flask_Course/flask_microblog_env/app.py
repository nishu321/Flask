import datetime
from time import strftime
from flask import Flask, render_template, request, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://Nishu:Nishu321@microblogapp.qgmqc.mongodb.net/test")
app.db = client.microblog

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        entery_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        app.db.entries.insert_one({"content": entery_content, "date": formatted_date})

    entries_with_date = [
        (
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"],"%Y-%m-%d").strftime("%b %d")
        )
        for entry in app.db.entries.find()
    ]
    
    return render_template("home.html", entries=entries_with_date)