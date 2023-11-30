from flask_wtf import FlaskForm
from wtforms.fields import StringField , SubmitField, TextAreaField, DateTimeLocalField
from wtforms.validators import data_required

class AddProductForm(FlaskForm):
    projectname = StringField("projectname", validators=[data_required(
        message="ჩაწერეთ პროექტის სახელი")])

    name = StringField("name")
    
    email = StringField("email")
    
    coordinates = StringField("coordinates")

    time = DateTimeLocalField("content" , validators=[
                            data_required(message="ჩაწერეთ შეხვედრის დრო")])
    
    content = TextAreaField("content", validators=[
                            data_required(message="განცხადების დამატება")])

    submit = SubmitField("submit")

class AddSearchForm(FlaskForm):
    input = StringField("input")
    submit = SubmitField("submit")
