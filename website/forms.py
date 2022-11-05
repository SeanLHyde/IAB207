
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

# class CommentsForm(FlaskForm):
#     textArea=StringField("Comments", validators=[InputRequired])
#     submit = SubmitField("Post comment")