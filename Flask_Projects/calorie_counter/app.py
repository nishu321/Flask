from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config["SERCET_KEY"] = "17c03ca41147650a9458dd14c8613265"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)