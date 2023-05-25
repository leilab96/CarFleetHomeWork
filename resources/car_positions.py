from flask import request
from flask_restful import Resource, reqparse
from models.car import CarModel
from models.position import PositionModel
from datetime import datetime

class CarPosition(Resource):
    # Parse the latitude and longitude values from the request body
    parser = reqparse.RequestParser()
    parser.add_argument('latitude', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('longitude', type=float, required=True, help='This field cannot be left blank')

    def post(self, plate):
        
        data = CarPosition.parser.parse_args()
        latitude = data['latitude']
        longitude = data['longitude']
        # Find the car by its license plate
        car = CarModel.find_by_attribute(license_plate=plate)

        if not car:
            # Return an error message if the car is not found
            return {'message': 'Car not found.'}, 404
        # Create and save the position to the database with adding also the datetime
        car_position = PositionModel(date=datetime.now(), latitude=latitude, longitude=longitude, car_id=car.id)
        car_position.save_to_db()

        return {'message': 'Position saved successfully'}, 201
    
    # get method to list positions based on plate number
    def get(self, plate):
        car = CarModel.find_by_attribute(license_plate=plate)
         # Return an error message if the car is not found
        if not car:
            return {'message': 'Car not found.'}, 404

        positions = PositionModel.query.filter_by(car_id=car.id).all()
        positions_json = [position.json() for position in positions]

        return {'positions': positions_json}, 200