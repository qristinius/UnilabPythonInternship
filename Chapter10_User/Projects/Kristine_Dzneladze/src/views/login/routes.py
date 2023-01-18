from flask import Blueprint, render_template , flash 
from src.views.login.forms import LoginForm

login_blueprint = Blueprint("login", __name__, template_folder="templates")

@login_blueprint.route("/login" , methods=["GET", "POST"])
def login():
    login_form =  LoginForm ()
    if login_form.validate_on_submit():
        user_name = login_form.username.data
        user_mail = login_form.email.data
        user_password = login_form.password.data
    else:
        print(login_form.errors)
    return render_template("login/login.html" , loginform = login_form)


