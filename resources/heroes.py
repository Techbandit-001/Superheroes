from flask_restful import Resource

class HeroesResource(Resource):
    def get(self, id = None):
        if id == None:
            return []
        else:
            return {}
        
    def post(self):
        return {"message": "Heroes created"}

    def patch(self, id):
        return {"message": "Heroes updated"}

    def delete(self, id):
        return {"message": "Heroes deleted"}