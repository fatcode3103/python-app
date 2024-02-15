from myApp.app.connectDB import db
from myApp.app.entities.role import Role

class User(db.Model):
  __tablename__ = "user"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), unique=True, nullable=False)
  age = db.Column(db.String(15), unique=False, nullable=False)
  roleId = db.Column(db.Integer, db.ForeignKey(Role.id))