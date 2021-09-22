from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

ride_types = [
    {"label": "WIN Scooter", "value": "WIN"},
    {"label": "Limosine", "value": "LIMO"},
    {"label": "Compact SUV", "value": "CSUV"},
    {"label": "SUV", "value": "SUV"},
    {"label": "Sedan", "value": "SEDAN"},
    ]

class RideType(Resource):
    def get(self, value = None):
        if value is None:
            return ride_types

        for item in ride_types:
            if item['value'] == value.upper():
                return item
        return f"{value} - does not exists!"

    def put(self, todo_id):
        # TODO need to implement add new/ update ride type
        print(request.form['data'])
        return "Data Added Successfully!"
api.add_resource(RideType, '/<string:value>', '/')

if __name__ == '__main__':
    app.run(debug=True)