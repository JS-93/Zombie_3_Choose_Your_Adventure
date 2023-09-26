from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
import time
import random

engine = create_engine('sqlite:///zombie.db')
Session = sessionmaker(bind=engine) 
session = Session() 

def output_slow(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.001)
    print()

def get_random_health():
        return random.randint(1,10)

def get_random_location():
        return random.randint(1,4)
# create a new person function
def create_person(name: str, health: int, location_id: int):
    try:
        new_person = Person(name=name, health=health, location_id=location_id)
        session.add(new_person)
        session.commit()
    except:
        session.rollback() 
        raise Exception("Could not create person.")
    
def remove_person(person_id: int):
    try:
        person = session.query(Person).filter_by(id=person_id).first()
        if not person:
            raise Exception("Person not found.")
        session.delete(person)
        session.commit()
    except:
        session.rollback()
        raise Exception("Could not delete person.")

def update_person_location(person_id, new_location_id):
     try:
        person = session.query(Person).get(person_id)
        if not person:
            print(f'No person found with name {person_id}')
        
        person.location_id = new_location_id
        session.commit()
     except:
        session.rollback()
        raise Exception("Could not update person.")
             
    
def get_all_names():
    people = session.query(Person).all()
    info = [f'Name: {person.name} Health: {person.health}' for person in people]
    return output_slow('\n'.join(info))


def display_first_scene(person):
    while True:
         
         output_slow("1. Walk across the street to the park.\n2. Go explore the abandoned rv camp.\n3. Head to the graveyard where you here cries for help.")
         choice = input("Enter you choice...")
         if choice == "1":
              output_slow("The park has a collapsed playground with a torn swing, it's eerily quiet....There seems to be nothing here.")
         elif choice == "2":
              output_slow("The still silence of the camp is broken by sudden screaming...zombies")
              update_person_location(person, 3)
         else:
            break








