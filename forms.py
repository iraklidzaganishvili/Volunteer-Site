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
    submitS = SubmitField("submit")

class AddRegForm(FlaskForm):
    email = StringField("email", validators=[
                            data_required(message="ჩაწერეთ ელ-ფოსტა")])
    name =  StringField("email", validators=[
                            data_required(message="ჩაწერეთ სახელი")])
    surname =  StringField("email", validators=[
                            data_required(message="ჩაწერეთ გვარი")])
    password = StringField("password", validators=[
                            data_required(message="ჩაწერეთ პაროლი")])
    submit = SubmitField("submit")

class AddLoginForm(FlaskForm):

    email = StringField("email", validators=[
                            data_required(message="ჩაწერეთ ელ-ფოსტა")])
    password = StringField("password", validators=[
                            data_required(message="ჩაწერეთ პაროლი")])
    submit = SubmitField("submit")

class AddXForm(FlaskForm):

    info = StringField("info")

    submitX = SubmitField("submit")