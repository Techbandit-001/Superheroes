from flask_restful import Resource

class PowersResource(Resource):
    def get(self, id = None):
        if id == None:
            return []
        else:
            return {}
        
    
    def post(self):
        return {"message": "Powers created"}

    def patch(self, id):
        return {"message": "Powers updated"}

    def delete(self, id):
        return {"message": "Powers deleted"}