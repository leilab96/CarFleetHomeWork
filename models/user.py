from models.mixin_model import MixinModel
from db import db, BaseModel
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String



class UserModel(BaseModel, MixinModel):
  __tablename__ = 'users'
  # id = db.Column(db.Integer, primary_key=True)
  id = mapped_column(Integer, primary_key=True)
  # username = db.Column(db.String(80))
  username = mapped_column(String(80))
  # password = db.Column(db.String(80))
  password = mapped_column(String(800))

  email = mapped_column(String(80))

  def __init__(self, username, password):
    self.username = username
    self.password = password
    

  def json(self):
    return {'name': self.username, 'id': self.id}

  @classmethod
  def get_all(cls):
    return cls.query.all()
