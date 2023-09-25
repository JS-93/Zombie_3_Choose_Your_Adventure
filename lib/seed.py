from models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine




if __name__ == "__main__":

    engine = create_engine('sqlite:///zombie.db')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    

    house = Location(name="house")
    graveyard = Location(name="graveyard")
    rv_camp = Location(name="rv camp")
    grocery_store = Location(name="grocery store")

    session.add_all([house, graveyard, rv_camp, grocery_store])


    jane = Person(name="Jane Doe", health=10, location=house)
    john = Person(name="Johnny Simmons", health=7, location=house)

    session.add_all([jane, john])

    big_zombie = Zombie(description="Big and brute", health=40, location=graveyard)
    small_zombie = Zombie(description="Small", health=8, location=grocery_store)
    medium_zombie =Zombie(description="medium", health=19, location=rv_camp)

    session.add_all([big_zombie, small_zombie, medium_zombie])

    session.commit()
    session.close()

    print("Database updated")




