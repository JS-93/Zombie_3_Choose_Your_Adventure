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
        return random.randint(1,20)

def create_person(person_name):  # Define a function to create a person instance
    new_person = Person(  # person class and what we are returning 
        name=person_name,
        health=get_random_health(),
        location_id = 1,
    )
    session.add(new_person)
    session.commit()
    return new_person

def add_character():
    print("Please enter character name (first and last): ")
    person_name = input()
    if person_name:
        person_instance = create_person(person_name)  
        print(f"Added {person_name} to list of characters.")
    press_enter()

def press_enter():
    input("Press Enter to continue...")
# deletes the person from the table
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
# updates the location of the person given a new location_id
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
             
# retrieves all the names of the people in a top to bottom string format
def get_all_names():
    people = session.query(Person).all()
    info = [f'Name: {person.name} Health: {person.health}' for person in people]
    return output_slow('\n'.join(info))
# zombie attack to have amount of zombies in a location affect a person's health
def zombie_attack(person_id, location_id):
    try:
        person = session.query(Person).get(person_id)
        if not person:
            print("No person found with the id.")
            return
        if person.location_id != location_id:
            print(f"{person.name} is not in the location with id {location_id}.")
            return 
        
        zombie_count = session.query(Zombie).filter_by(location_id = location_id).count()
        person_name = person.name

        if zombie_count >= person.health and zombie_count > 0:
            remove_person(person.id)
            output_slow(f'{person_name} has been taken! Game over...')
            
        elif zombie_count > 0 and person.health > zombie_count:
            person.health -= zombie_count
            output_slow(f'{person_name} is injured- left with {person.health} health. {person.name} runs away back to the street.')
        elif zombie_count == 0:
            output_slow(f'{person_name} is safe for now...No zombies in sight.')

        session.commit()
    except:
        session.rollback()
        raise Exception("Could not affect person's health with zombies.")
def update_health(person_id):
    try:
        person = session.query(Person).get(person_id)
        if not person:
            print("No person found with the id.")
        person.health += 1
        session.commit()
        output_slow(f"Chuck thanked {person.name} for being a close friend all these years. He tosses {person.name} a beer and {person.name} feels better. {person.name}'s health is now {person.health}")
    except:
        session.rollback()
        raise Exception("Could not update health.")
# shows the list of zombies in each location
def get_number_of_zombies_per_location():
    locations = session.query(Location).all()
    info = []
    for location in locations:
        zombie_count = session.query(Zombie).filter_by(location_id=location.id).count()
        info.append(f'Location: {location.name} | Number of Zombies: {zombie_count}')
    return output_slow('\n'.join(info))

def create_location(name: str):
    try:
        new_location = Location(name=name)
        session.add(new_location)
        session.commit()
        return new_location
    except:
        session.rollback()
        raise Exception("Could not create a new location.")





def display_first_scene(person):
    while True:
         
         output_slow("1. Walk across the street to the park.\n2. Go explore the abandoned rv camp.\n3. Head to the graveyard where you hear cries for help.")
         choice = input("Enter your choice...")
         if choice == "1":
              output_slow("The park has a collapsed playground with a torn swing, it's eerily quiet....There seems to be nothing here.")
         elif choice == "2":
              output_slow("The still silence of the camp is broken by sudden screaming...zombies")
              update_person_location(person, 3)
              zombie_attack(person, 3)
         elif choice == "3":
             display_second_scene(person)
         else:
            break
chuck_has_helped = False

def display_second_scene(person):
    global chuck_has_helped
    while True:
        output_slow("1. Explore who's been yelling for help in the graveyard.\n2. Go around the graveyard toward the abandoned gravel road.\n3. Head toward the town square where you can hear the distant song of 'Joy to the World' being played.")
        choice = input("Enter your choice...")           
        if choice == "1":
            if chuck_has_helped:
                output_slow("Chuck is no longer here, he left a note saying he hopes the grocery store is as safe as everyone says it is.")
            else:
                output_slow(f"It's Chuck - a long time close friend, he says he came from the town square where he last saw a zombie.")
                update_health(person)
                chuck_has_helped = True
        elif choice == "2":
            person_id = person
            person = session.query(Person).filter_by(id = person_id).first()
            abandoned_road_scene(person)
        elif choice == "3":
            pass 
        # town square scene above

def abandoned_road_scene(person):
    output_slow(f"The gravel road leads to out of town, but {person.name} remembers a backway to the grocery store, but they have to cross the high school football field.")
    while True:
         output_slow("1. Keep going down the road to the high school.\n2. Turn back to the graveyard. ")
         choice = input("Enter your choice...")
         if choice == "1":
            output_slow("The abandoned road seems quiet and is ripe")
         elif choice == "2":
             output_slow(f"{person.name} heads back to the graveyard. With the zombies closing in it looks like the only option is to...\n1. Head to the town square...")
             choice = input("Enter the last choice...")
             if choice == "1":
                 pass
            #  town square scene above
             





          
        
            


            
                







