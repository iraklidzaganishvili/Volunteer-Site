from flask import render_template, redirect
from forms import AddProductForm, AddSearchForm
from ext import app, db
from models import Page, User


@app.route("/", methods=["POST", "GET"])
def index():

    search = AddSearchForm()
    if search.validate_on_submit():
        filt = Page.query.filter(Page.projectname.ilike(f"%{search.input.data}%")).all()
        return render_template("index.html", pages=filt, search=search)

    pages = Page.query.all()
    return render_template("index.html", pages=pages, search=search)


@app.route("/add.html", methods=["POST", "GET"])
def add():

    form = AddProductForm()
    if form.validate_on_submit():
        new_page = Page(name=form.name.data, email=form.email.data, content=form.content.data,
                        coordinates=form.coordinates.data, projectname=form.projectname.data, time=str(form.time.data)[:-3])
        db.session.add(new_page)
        db.session.commit()
        return redirect("/")

    return render_template("/add.html", form=form)


@app.route("/page-<int:page_id>")
def view_page(page_id):
    page = Page.query.get(page_id)
    if not page:
        return render_template("404.html")
    return render_template("custom_page.html", page=page)
