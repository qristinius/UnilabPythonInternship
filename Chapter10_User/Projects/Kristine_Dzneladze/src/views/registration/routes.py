from flask import Blueprint, render_template , flash 
from src.views.registration.forms import RegisterForm
from src.models.registration import User

registration_blueprint = Blueprint("registration", __name__, template_folder="templates")

@registration_blueprint.route("/registration" , methods=["GET", "POST"])
def registration():
    register_form =  RegisterForm ()
    if register_form.validate_on_submit():
        user_name = register_form.username.data
        user_mail = register_form.email.data
        user_password = register_form.password.data

        user = User( username = user_name, email = user_mail, password = user_password)
        user.create()
        user.save()
    else:
        print(register_form.errors)
    return render_template("registration/registration.html" , registerform = register_form)


