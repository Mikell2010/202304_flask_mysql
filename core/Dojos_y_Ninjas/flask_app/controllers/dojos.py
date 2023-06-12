from flask import render_template, request, redirect
from flask_app import app

# Models
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    dojos = Dojo.read_all()
    return render_template("index.html", all_dojos=dojos)


@app.route("/dojos/create/", methods=['GET','POST'])
def dojo_create():
    """Crear un dojo."""
    Dojo.create(request.form)
    return redirect('/dojos')


@app.route("/dojos/<int:id>/detail/")
def dojo_detail(id):
    """Detalle de un dojo."""
    data = {
        'id':id
    }
    return render_template('dojo_detail.html', dojo=Dojo.get_one_with_ninjas(data))
