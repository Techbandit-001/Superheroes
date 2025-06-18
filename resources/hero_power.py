from flask_restful import Resource, reqparse

# Define the parser for POST
parser = reqparse.RequestParser()
parser.add_argument('hero_id', type=int, required=True, help='Hero ID is required')
parser.add_argument('power_id', type=int, required=True, help='Power ID is required')
parser.add_argument('strength', type=str, required=True, help='Strength is required')

class HeroPowerResource(Resource):
    def post(self):
        args = parser.parse_args()
        # Here you'd normally create a HeroPower record in the database
        return {
            "message": "HeroPower created successfully",
            "data": {
                "hero_id": args["hero_id"],
                "power_id": args["power_id"],
                "strength": args["strength"]
            }
        }, 201
