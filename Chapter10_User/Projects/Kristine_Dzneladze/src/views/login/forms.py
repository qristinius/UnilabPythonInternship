from wtforms.fields import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, equal_to
from flask_wtf import FlaskForm


class LoginForm(FlaskForm) :
    email = StringField("Enter your mail", validators=[DataRequired(message="You can't log in without mail")])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField()