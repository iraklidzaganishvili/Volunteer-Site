from flask import render_template, redirect
from forms import AddProductForm, AddSearchForm, AddLoginForm, AddRegForm, AddXForm
from ext import app, db, login_manager
from models import Page, User
from flask_login import login_user, logout_user, current_user
import json

@app.route("/", methods=["POST", "GET"])
def index():

    search = AddSearchForm()
    x = AddXForm()
    if search.submitS.data and search.validate_on_submit():
        filt = Page.query.filter(Page.projectname.ilike(
            f"%{search.input.data}%")).all()
        return render_template("index.html", pages=filt, search=search, x=x)

    pages = Page.query.all()
    if x.submitX.data and x.validate_on_submit():
        filt = Page.query.filter(Page.id == x.info.data).first()
        db.session.delete(filt)
        db.session.commit()
        return redirect("/")

    return render_template("index.html", pages=pages, search=search, x=x)


@app.route("/add", methods=["POST", "GET"])
def add():

    form = AddProductForm()
    if form.validate_on_submit():
        new_page = Page(name=form.name.data, email=form.email.data, content=form.content.data,
                        coordinates=form.coordinates.data, projectname=form.projectname.data, time=str(form.time.data)[:-3], comming = 1)
        db.session.add(new_page)
        db.session.commit()
        return redirect("/")

    return render_template("/add.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    error = False
    form = AddLoginForm()
    if form.validate_on_submit():
        filt = User.query.filter(User.email == form.email.data).first()
        if (filt):
            if (filt.password != form.password.data):
                error = "არასწორი ელ-ფოსტა ან პაროლი"
            else:
                login_user(filt)
                return redirect ("/")
        else:
            error = "არასწორი ელ-ფოსტა ან პაროლი"
    return render_template("/login.html", form=form, error=error)


@app.route("/register", methods=["POST", "GET"])
def register():
    form = AddRegForm()
    error = False
    if form.validate_on_submit():
        filt = User.query.filter(User.email == form.email.data).first()
        if (filt):
            error = "ეს ელ-ფოსტა უკვე დარეგისტრირებულია"
            print ("error")
        else:
            new_user = User(email = form.email.data, password = form.password.data, name = form.name.data, surname = form.surname.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect ("/")

    return render_template("/register.html", form=form, error=error)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/page-<int:page_id>", methods=["POST", "GET"])
def view_page(page_id):
    page = Page.query.get(page_id)
    x = AddXForm()
    curr_page = Page.query.filter(Page.id == page_id).first()
    
    if not page:
        return render_template("404.html")
    
    if x.validate_on_submit():

        commingTo = []
        
        if current_user.commingTo:
            if page_id not in json.loads(current_user.commingTo):

                commingTo = json.loads(current_user.commingTo)
                commingTo.append(page_id)
                current_user.commingTo = json.dumps(commingTo)

                curr_page.comming += 1
                
                db.session.commit()

            else:

                commingTo = json.loads(current_user.commingTo)
                commingTo.remove(page_id)
                current_user.commingTo = json.dumps(commingTo)

                curr_page.comming -= 1

                db.session.commit()

        else:

            current_user.commingTo = json.dumps([page_id])

            curr_page.comming += 1

            db.session.commit()

        return redirect(f"/page-{page_id}#map")
    
    if current_user.commingTo == "null":

        current_user.commingTo = ""
        db.session.commit()

    if current_user.commingTo and page_id in json.loads(current_user.commingTo): comming = "მოვდივარ"
    else: comming = "წამოხვალ?"
    
    return render_template("custom_page.html", page=page, x=x, comming=comming, comming_num=curr_page.comming)
