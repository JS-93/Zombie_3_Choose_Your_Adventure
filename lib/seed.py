from models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import random




if __name__ == "__main__":

    engine = create_engine('sqlite:///zombie.db')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    

    house = Location(name="House")
    graveyard = Location(name="Graveyard")
    rv_camp = Location(name="RV Camp")
    town_square = Location(name="Town Square")
    drug_store = Location(name = "Drug Store")
    high_school = Location(name = "High School")
    post_office = Location(name="Post Office")
    police_station = Location(name="Police Station")
    grocery_store = Location(name="Grocery Store")

    session.add_all([house, graveyard, rv_camp, drug_store, high_school, post_office, police_station, grocery_store, town_square])


    jane = Person(name="Jane Doe", health=10, location=house)
    john = Person(name="Johnny Smith", health=7, location=house)

    session.add_all([jane, john])

    zombies = []
    locations = [graveyard, rv_camp, town_square, drug_store, high_school, post_office, police_station]
    for _ in range(50):
        health = random.randint(1, 30)
        location = random.choice(locations)
        description = f"Zombie with health {health}"
        zombie = Zombie(description = description, health = health, location = location)
        zombies.append(zombie)
    
    session.add_all(zombies)

    session.commit()
    session.close()

    print("Database updated")




