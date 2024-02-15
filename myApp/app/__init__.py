from flask import Flask
from myApp.app.routes.users import users_bp
from myApp.app.connectDB import db

def create_app():
  app = Flask(__name__)

  app.config["SQLALCHEMY_DATABASE_URL"] = "mysql+mysqlconnector://root:Root123@@localhost/demo_python_connect_db"

  db.app = app
  db.init_app(app)

  app.register_blueprint(users_bp)

  return app