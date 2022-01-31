from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/fancy")
def fancy_hello():
    return """
    <html>
    <body>
    <h1>Greetings!</h1>
    <p>Hello, world</p>
    </body>
    """

if __name__ == "__main__":
    app.run(debug=True)