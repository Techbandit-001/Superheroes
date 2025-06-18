from flask_restful import Resource
from flask import request
from models import Hero  # Make sure the Hero model is imported
from app import db       # Import your database instance

class HeroesResource(Resource):
    def get(self, id=None):
        if id is None:
            heroes = Hero.query.all()
            return [hero.to_dict() for hero in heroes], 200
        else:
            hero = Hero.query.get(id)
            if hero:
                return hero.to_dict(), 200
            return {"error": "Hero not found"}, 404

    def post(self):
        data = request.get_json()
        try:
            new_hero = Hero(
                name=data.get("name"),
                super_name=data.get("super_name")
            )
            db.session.add(new_hero)
            db.session.commit()
            return new_hero.to_dict(), 201
        except Exception as e:
            return {"error": str(e)}, 400

    def patch(self, id):
        hero = Hero.query.get(id)
        if not hero:
            return {"error": "Hero not found"}, 404

        data = request.get_json()
        if "name" in data:
            hero.name = data["name"]
        if "super_name" in data:
            hero.super_name = data["super_name"]

        db.session.commit()
        return hero.to_dict(), 200

    def delete(self, id):
        hero = Hero.query.get(id)
        if not hero:
            return {"error": "Hero not found"}, 404

        db.session.delete(hero)
        db.session.commit()
        return {"message": "Hero deleted"}, 200
