from flask_restful import Resource
from flask import request

class HeroPowerResource(Resource):
    def get(self, id=None):
        if id is None:
            
            return [
                {"id": 1, "hero_id": 1, "power_id": 2, "strength": "Strong"},
                {"id": 2, "hero_id": 2, "power_id": 3, "strength": "Average"},
            ], 200
        else:
            
            return {"id": id, "hero_id": 1, "power_id": 2, "strength": "Strong"}, 200

    def post(self):
        data = request.get_json()
      
        return {"message": "HeroPower created", "data": data}, 201

    def patch(self, id):
        data = request.get_json()
      
        return {"message": f"HeroPower with id {id} updated", "data": data}, 200

    def delete(self, id):
      
        return {"message": f"HeroPower with id {id} deleted"}, 204
