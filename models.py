from ext import db, app, login_manager
from flask_login import UserMixin

class Page(db.Model):

    __tablename__ = "pages"
    
    id = db.Column(db.Integer, primary_key=True)
    projectname = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)
    coordinates = db.Column(db.String)
    time = db.Column(db.String)
    content = db.Column(db.String)

class User (db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    usename = db.Column(db.String)
    password = db.Column(db.String)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()