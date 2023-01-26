from flask import Blueprint, render_template , redirect, url_for, request
from flask_login import current_user
from src.views.login.forms import LoginForm
from flask_login import login_user, logout_user
from sqlalchemy import or_, MetaData
from src.models.registration import User, Role, UserRole
login_blueprint = Blueprint("login", __name__, template_folder="templates")

@login_blueprint.route("/login" , methods=["GET", "POST"])
def login():
    login_form =  LoginForm ()
    meta = MetaData()
    if login_form.validate_on_submit():
        user = User.query.filter_by( email = login_form.email.data).first()
        next = request.args.get("next")
        if user and user._check_password(login_form.password.data):
            print(next)
            login_user(user)
            if next:
                return redirect(url_for("essay.essay_form"))
            else:
                return redirect(url_for("main.home"))
    else:
        print(login_form.errors)
    return render_template("login/login.html" , loginform = login_form)


@login_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

