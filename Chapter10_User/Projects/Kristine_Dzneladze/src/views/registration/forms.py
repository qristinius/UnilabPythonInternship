from wtforms.fields import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, equal_to
from flask_wtf import FlaskForm


class RegisterForm(FlaskForm):

    username = StringField("Enter username you want to have", validators=[
                           DataRequired(message="username is required")])
    email = EmailField("Enter your email", validators=[DataRequired(
        message="Email required"), Email(message="Please Enter valid email")])
    password = PasswordField("Enter password", validators=[
                             DataRequired(message="Password is required")])
    confirmation = PasswordField("Confrim password", validators=[DataRequired("confirm password required"),
                                                                 equal_to("password", message="Passwords do not match")])
    submit = SubmitField()

