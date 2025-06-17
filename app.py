from flask import Flask, request
from flask_restful import Resource, Api
from flask_migrate import Migrate

from models import db
from resources.heroes import HeroesResource
from resources.powers import PowersResource
from resources.hero_power import HeroPowerResource

app = Flask(__name__)

# configuring our flask app through the config object
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
# allow sqlalchemy to display generate sql on the terminal
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)

api = Api(app)

migrate = Migrate(app, db)

@app.route("/", methods=["GET"])
def index():
    return {"message": "Welcome to my first flask"}

@app.post("/hero_powers")
def create_category():
    data = request.get_json()
    # Assume category creation logic here
    return {"message": "Category created", "data": data}, 201

@app.get("/heroes")
def get_categories():
    return [], 200  # List of categories

@app.get("/powers")
def get_powers():
    return [], 200  # List of categories

@app.get("/heroes/<int:id>")
def get_single_category(id):
    # Retrieve category by ID (mock response)
    return {"id": id, "name": "Sample Category"}, 200

@app.get("/powers/<int:id>")
def single_category(id):
    # Retrieve category by ID (mock response)
    return {"id": id, "name": "Sample Category"}, 200

@app.patch("/powers/<int:id>")
def update_category(id):
    data = request.get_json()
    # Assume update logic here
    return {"message": f"Category {id} updated", "updated_data": data}, 200

@app.delete("/categories/<int:id>")
def delete_category(id):
    # Assume delete logic here
    return {"message": f"Category {id} deleted"}, 200

api.add_resource(HeroesResource, "/heroes", "/heroes/<id>")
api.add_resource(PowersResource, "/powers", "/powers/<id>")
api.add_resource(HeroPowerResource, "/hero_powers", "/hero_powers/<int:id>")

# if __name__ == "__main__":
#     app.run(debug=True)
