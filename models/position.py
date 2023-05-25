from db import db, BaseModel
from models.mixin_model import MixinModel
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey

class PositionModel(BaseModel, MixinModel):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True) 
    date = Column(DateTime)
    latitude = Column(Float(precision=5))
    longitude = Column(Float(precision=5))
    # Foreign key referencing the 'id' column of the 'cars' table
    car_id = Column(Integer, ForeignKey('cars.id'))

    def __init__(self, date, latitude, longitude, car_id):
        self.car_id = car_id
        self.latitude = latitude
        self.longitude = longitude
        # Initialize the date and time of the position
        self.date = date

    def json(self):
        return {
            'date': self.date.isoformat(),
            'latitude': self.latitude,
            'longitude': self.longitude      
        }
