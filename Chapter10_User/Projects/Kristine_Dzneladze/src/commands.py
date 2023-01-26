from flask.cli import with_appcontext
import click
from src.extensions import db
from src.data import books
from src.models.books import Book
from src.models.registration import User , UserEssay, UserRole, Role

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating db")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating db")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("populating db")
    #users
    admin_user = User(username = "admin", password = "mypass", email = "adminmail@gmail.com" )
    admin_user.create()
    admin_user.save()
    
    #roles
    roles = ["user", "moderator", "admin"]
    for role in roles:
        user_role = Role(name = role)
        user_role.create()
    user_role.save()

    admin_role = Role.query.filter_by(name = "admin").first()
    click.echo(admin_role)

    admin_user_role  = UserRole(user_id = admin_user.id, role_id = admin_role.id)
    click.echo(admin_user_role)
    admin_user_role.create()
    admin_user_role.save()

    #books db
    for item in books:
        book_parametres = Book(bookname = item[0], author = item[1], genre = item[2], img_link = item[3])
        book_parametres.create()
    book_parametres.save()
    click.echo("Finished populating db")


