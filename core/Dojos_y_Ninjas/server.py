"""Server."""

# App config
from flask_app import app

# Controllers
from flask_app.controllers import dojos, ninjas


if __name__== "__main__":
    app.run(debug=True)
