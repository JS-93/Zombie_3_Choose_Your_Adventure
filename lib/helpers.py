from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///zombie.db')
Session = sessionmaker(bind=engine) 
session = Session() 

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
    names = session.query(Person.name).all()
    for name in names:
        print(name)

