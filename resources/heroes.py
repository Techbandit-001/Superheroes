from flask_restful import Resource
from models import Hero

class HeroesResource(Resource):
    def get(self, id=None):
        if id is None:
            heroes = Hero.query.all()
            return [hero.to_dict() for hero in heroes], 200
        else:
           hero = Hero.query.filter_by(id=id).first()
           if hero:
               return hero.to_dict(), 200
        return {"message": "Hero not found"}, 404