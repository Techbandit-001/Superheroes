from random import choice as rc
from app import app
from models import db, Hero, Power, HeroPower

if __name__ == '__main__':
    with app.app_context():
        print("Clearing database...")
        HeroPower.query.delete()
        Power.query.delete()
        Hero.query.delete()

        print("Seeding powers...")
        powers = [
            Power(name="Super Strength", description="Gives the wielder super-human strength."),
            Power(name="Flight", description="Allows the wielder to fly at supersonic speed."),
            Power(name="Super Human Senses", description="Enhances senses to super-human levels."),
            Power(name="Elasticity", description="Can stretch the human body to extreme lengths."),
        ]
        db.session.add_all(powers)
        db.session.commit()

        print("Seeding heroes...")
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra"),
        ]
        db.session.add_all(heroes)
        db.session.commit()

        print("Assigning powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        hero_powers = []

        for hero in heroes:
            assigned_powers = [rc(powers) for _ in range(rc([1, 2]))]
            for power in set(assigned_powers):  # Avoid duplicates
                hero_powers.append(
                    HeroPower(hero=hero, power=power, strength=rc(strengths))
                )

        db.session.add_all(hero_powers)
        db.session.commit()

        print("✅ Done seeding!")
