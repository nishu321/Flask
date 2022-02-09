import datetime
from time import strftime
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

entries = []

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        entery_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entery_content,formatted_date))

    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1],"%Y-%m-%d").strftime("%b %d")
        )
        for entry in entries
    ]
    
    return render_template("home.html", entries=entries_with_date)
