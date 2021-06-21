from flask_wtf import FlaskForm
from wtforms import StringField,RadioField,IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class Counter(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired()]
    )

    age = IntegerField(
        "Age",
        validators=[DataRequired(),Length(min=2, max=3,message="Please enter validate age.")]
    )

    weight = IntegerField(
        "Weight",
        validators=[DataRequired()]
    )

    sex = RadioField(
        "Sex",
        choices=[("Male","Male"),("Female","Female")]
    )

    goal = RadioField(
        "Goal",
        choices=[("Lose","Lose"),("Maintaine","Maintaine"),("Gain","Gain")]
    )

    fat = IntegerField(
        "Fat",
        validators=[DataRequired(),NumberRange(min=20,max=35,message="Please enter a number between 20 - 35")]
    )

    protein = IntegerField(
        "Protein",
        validators=[DataRequired(),NumberRange(min=10,max=35,message="Please enter a number between 10 - 35")]
    )

    carbs = IntegerField(
        "Carbs",
        validators=[DataRequired(),NumberRange(min=45,max=65,message="Please enter a number between 45- 65")]
    )

