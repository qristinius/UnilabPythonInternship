from wtforms.fields import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, equal_to
from flask_wtf import FlaskForm


class LoginForm(FlaskForm) :
    username = StringField("Enter your username", validators=[DataRequired(message="You can't log in without username")])
    email  = EmailField("Enter your email", validators=[DataRequired(
        message="Email required"), Email(message="Please Enter valid email")])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField()