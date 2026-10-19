
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
testing = True
def create_app():
    app = Flask(__name__)

    from app.routes import routes
    app.register_blueprint(routes)
    if testing :
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:TASREEE3%40s@localhost:3306/tasree3"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.models.models import Source, Tip

    with app.app_context():
        db.create_all()

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

