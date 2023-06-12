
# Flask
from flask import render_template, request, redirect, url_for, flash

# Flask app
from flask_app import app

# Models
from flask_app.models.ninja import Ninja 
from flask_app.models.dojo import Dojo


@app.route("/ninjas")
def ninja():
    """Lista de ninjas."""

    return render_template('ninja.html', dojos= Dojo.read_all())


@app.route("/ninjas/create/", methods=['GET','POST'])
def ninja_create():
    """Crear un ninja."""
    ninja.Ninja.create(request.form)
    return redirect('/')