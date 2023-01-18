from src.extensions import db
from src.models.base import BaseModel

class User(BaseModel):
    __tablename__ = "Registered users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password  = db.Column(db.String)
    email = db.Column(db.String)





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
