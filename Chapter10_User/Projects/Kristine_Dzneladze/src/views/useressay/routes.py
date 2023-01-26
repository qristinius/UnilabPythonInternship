from flask import Blueprint, render_template, flash
from flask_login import login_required
from os import path, getcwd , sep , pardir
from src.views.useressay.forms import EssayForm
from werkzeug.utils import secure_filename
from src.models.registration import UserEssay
from src.views.useressay.name_generator import random_name
from src.extensions import db 

useressay_blueprint = Blueprint("essay", __name__, template_folder="templates")

@useressay_blueprint.route("/essay", methods=["GET", "POST"])
@login_required
def essay_form():
    form = EssayForm()
    if form.validate_on_submit():
        

        user_firstname = form.firstname.data
        user_lastname = form.lastname.data
        user_mail = form.email.data
        user_experience = form.writer_experience.data
        user_writer_field = form.writer_field.data
        user_essay_secription = form.essay_description.data


        filename = secure_filename(form.essay_file.data.filename)
        file_type = filename.split(".")[1]

        while True:
            new_filename = random_name() + "." + file_type

            if not UserEssay.query.filter_by(uploaded_file = new_filename).first() :


                location = path.realpath(path.join(
                getcwd(), path.dirname(__file__) + sep + pardir+ sep + pardir))
                print(location)
                file_path = path.join(location, "uploaded_files", new_filename)
                form.essay_file.data.save(file_path)
                flash("Succesfully uploaded")


                someone = UserEssay(firstname=user_firstname, lastname=user_lastname, email=user_mail,
                                    writer_experience=user_experience, writer_field=user_writer_field, essay_description=user_essay_secription, uploaded_file = new_filename)
                someone.create()
                someone.save()
                break

    else:
        print(form.errors)
    return render_template("useressay/essay_form.html",  user_essay=form)

