from ext import db, app

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectname = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)
    coordinates = db.Column(db.String)
    time = db.Column(db.String)
    content = db.Column(db.String)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()