from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('first_page.html')

@app.route("/jinja")
def jinja():
    return render_template(
        'jinja.html',
        name="John Doe",
        template_name='Jinja')

@app.route("/jinja_expressions")
def jinja_expressions():
    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    # addition and subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation
    first_name = "Caption"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_one":animal_one,
        "animal_two":animal_two,
        "orange_amount":orange_amount,
        "apple_amount":apple_amount,
        "donate_amount":donate_amount,
        "first_name":first_name,
        "last_name":last_name
    }

    return render_template(
        'jinja_expressions.html',**kwargs)


class GalileanMoons():
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/jinja_data_structures")
def jinja_data_strucures():
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    car = {
        "brand":"Honda",
        "model":"Civic",
        "year":2016,
    }

    moons = GalileanMoons("IO", "Europa", "Ganymede", "Callisto")

    return render_template(
        'jinja_data_structures.html',
        movies=movies,
        car=car,
        moons=moons)

@app.route("/jinja_conditional")
def jinja_conditional():
    return render_template(
        'jinja_conditional.html',
        company="Microsoft")

@app.route("/jinja_loops")
def jinja_loops():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    return render_template('jinja_loops.html',planets=planets)

@app.route("/jinja_variables")
def jinja_variables():
    return render_template("jinja_variables.html", todos=["Get Milk", "Learn programming"])

todos = [
    ("Get milk", False),
    ("Learn Programing", True)
]

@app.route("/jinja_macros")
def jinja_macros():
    return render_template("jinja_macros.html", todos=todos)


#create custome tests
def square(value):
    return (value ** 0.5).is_integer()

app.jinja_env.tests["square"] = square

def hello_world(value):
    return f"Hello World,{value}"

#injecting varriable to all templates
@app.context_processor
def greeting():
    return {"greeting":"Hello World"}

#allowing all templates to access function
app.jinja_env.globals['hello_world'] = hello_world

@app.route("/jinja_test")
def jinja_test():
    return render_template("jinja_test.html")

if __name__ == "__main__":
    app.run(debug=True)