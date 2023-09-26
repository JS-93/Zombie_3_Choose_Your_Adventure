from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
import time

engine = create_engine('sqlite:///zombie.db')
Session = sessionmaker(bind=engine) 
session = Session() 

def output_slow(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print()

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
    
def get_all_names():
    people = session.query(Person).all()
    info = [f'Name: {person.name} Health: {person.health}' for person in people]
    return output_slow('\n'.join(info))


