
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo, email_validator

#creates the login information
class LoginForm(FlaskForm):
    email=StringField("Email", validators=[InputRequired('Enter your email')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#  # this is the registration form
class RegisterForm(FlaskForm):
    name=StringField("Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password1=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    password2 = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

#Create new destination
class EventForm(FlaskForm):
    eventname=StringField("Event Name", validators=[InputRequired()])
    description=TextAreaField("Description", validators=[InputRequired()])
    location=StringField("Event Location", validators=[InputRequired()])
    date=StringField("Date", validators=[InputRequired()])
    ticketamount=StringField("Number of tickets", validators=[InputRequired()])
    ticketprice=StringField("Price per ticket", validators=[InputRequired()])
    creatorname=StringField("Creator Name", validators=[InputRequired()])
    image=StringField("Cover Image", validators=[InputRequired()])
    submit = SubmitField("Create")

class CommentsForm(FlaskForm):
    comment=StringField("Comments", validators=[InputRequired()])
    submit = SubmitField("Post comment")
