from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize metadata and database
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"
    serialize_rules = ("-hero_powers.hero", "-hero_powers.power.hero_powers")  # 👈 prevent deep nesting

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    super_name = db.Column(db.Text, nullable=False)

    hero_powers = db.relationship("HeroPower", back_populates="hero", cascade="all, delete-orphan")


class Power(db.Model, SerializerMixin):
    __tablename__ = "powers"
    serialize_rules = ("-hero_powers.power", "-hero_powers.hero.hero_powers")  # 👈 avoid deep circular ref

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    hero_powers = db.relationship("HeroPower", back_populates="power", cascade="all, delete-orphan")


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'
    serialize_rules = ("hero.id", "hero.name", "hero.super_name", "power.name", "strength")  
    # 👈 Serialize only specific fields to avoid recursion

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship("Hero", back_populates="hero_powers")
    power = db.relationship("Power", back_populates="hero_powers")
