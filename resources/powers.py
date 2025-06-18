from flask_restful import Resource
from flask import request
from models import Power  # Make sure Power model is imported

class PowersResource(Resource):
    def get(self, id=None):
        if id is None:
            powers = Power.query.all()
            return [power.to_dict() for power in powers], 200
        else:
            power = Power.query.get(id)
            if power:
                return power.to_dict(), 200
            return {"error": "Power not found"}, 404

    def post(self):
        data = request.get_json()
        try:
            new_power = Power(name=data.get("name"), description=data.get("description"))
            from app import db
            db.session.add(new_power)
            db.session.commit()
            return new_power.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 400

    def patch(self, id):
        power = Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404

        data = request.get_json()
        if "name" in data:
            power.name = data["name"]
        if "description" in data:
            power.description = data["description"]

        from app import db
        db.session.commit()
        return power.to_dict(), 200

    def delete(self, id):
        power = Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404

        from app import db
        db.session.delete(power)
        db.session.commit()
        return {"message": "Power deleted"}, 200
