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
    comming = db.Column(db.Integer)


class User (db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    commingTo = db.Column(db.String)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        db.session.add(User(email="admin", password="1234",
                       name="irakli", surname="dzaganishvili"))
        db.session.add(User(email="zuko@gmail.com", password="1",
                       name="zuko", surname="zikaze"))
        db.session.add(Page(projectname="ნაგვის აკრეფა ლისთან", name="ზურაბი ალექსიშვილი", email="zurabiko@gmail.com",
                       coordinates="41.746233, 44.738844", time="2023-11-29 11:00", content="ვიკრიბებით ნაგვის გასასუფთავებლად", comming=1))
        db.session.add(Page(projectname="ტანსაცმლის გაცვლა/გაცემა", name="დემეტრე ზივიანი", email="demetriko@gmail.com",
                            coordinates="40.741233, 44.728844", time="2023-12-01 14:00", content="მოიტანეთ ტანსაცმელი რომელიც არ გჭირდებათ და გავცვალოთ. დარჩენილი ტანსაცმელი უსახლკაროოებს და ობლებს მიეცემა", comming=1))
        db.session.add(Page(projectname="ტანსაცმლის გაცვლა/გაცემა", name="დემეტრე ზივიანი", email="demetriko@gmail.com",
                            coordinates="40.741233, 44.728844", time="2023-12-01 14:00", content="მოიტანეთ ტანსაცმელი რომელიც არ გჭირდებათ და გავცვალოთ. დარჩენილი ტანსაცმელი უსახლკაროოებს და ობლებს მიეცემა", comming=1))
        db.session.add(Page(projectname="ტანსაცმლის გაცვლა/გაცემა", name="დემეტრე ზივიანი", email="demetriko@gmail.com",
                            coordinates="40.741233, 44.728844", time="2023-12-01 14:00", content="მოიტანეთ ტანსაცმელი რომელიც არ გჭირდებათ და გავცვალოთ. დარჩენილი ტანსაცმელი უსახლკაროოებს და ობლებს მიეცემა", comming=1))
        db.session.commit()
