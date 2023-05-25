import requests
from db import db, BaseModel
from models.mixin_model import MixinModel
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String

class PositionModel(BaseModel, MixinModel):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True) 
    date = Column(DateTime)
    latitude = Column(Float(precision=5))
    longitude = Column(Float(precision=5))
    # Foreign key referencing the 'id' column of the 'cars' table
    car_id = Column(Integer, ForeignKey('cars.id'))
    #Address added to positions
    address = Column(String(300))

    def __init__(self, date, latitude, longitude, car_id):
        self.car_id = car_id
        self.latitude = latitude
        self.longitude = longitude
        # Initialize the date and time of the position
        self.date = date
        self.address = ''

    def json(self):
        self.resolve_address(self.latitude, self.longitude) 
        return {
            'date': self.date.isoformat(),
            'latitude': self.latitude,
            'longitude': self.longitude,
            'address': self.address      
        }

    def resolve_address(self, latitude, longitude):
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.address = data.get('display_name', '')
        else:
            self.address = ''