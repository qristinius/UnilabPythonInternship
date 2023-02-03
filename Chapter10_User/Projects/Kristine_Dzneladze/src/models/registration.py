from src.extensions import db
from src.models.base import BaseModel
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel , UserMixin):
    __tablename__ = "registered_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique  = True, nullable = False)
    _password  = db.Column("password",db.String, unique =  True, nullable = False)
    email = db.Column(db.String)

    roles = db.relationship("Role", secondary  = "User_roles")

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    def _check_password(self,password):
        return check_password_hash(self.password, password)

    def has_role(self, role):
        return role in [userrole.name for userrole in self.roles]


    password = db.synonym("_password", descriptor = property(_get_password, _set_password))

class UserRole(BaseModel):
    __tablename__ = "User_roles"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

class Role(BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique  = True)




class UserEssay(BaseModel):

    __tablename__ = "User essays"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname  = db.Column(db.String)
    email = db.Column(db.String)
    writer_experience = db.Column(db.String)
    writer_field = db.Column(db.String)
    essay_description = db.Column(db.String)
    uploaded_file = db.Column(db.String)
