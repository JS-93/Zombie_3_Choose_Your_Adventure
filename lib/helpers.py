from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from termcolor import colored
import time
import random

engine = create_engine('sqlite:///zombie.db')
Session = sessionmaker(bind=engine) 
session = Session() 
# outputs cli text slow
def output_slow(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
    print()
# outputs cli text slower
def output_slower(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()
# gets random health for person in range of 1-20
def get_random_health():
        return random.randint(1,20)
# creates a location given a string name
def create_location(name: str):
    try:
        new_location = Location(name=name)
        session.add(new_location)
        session.commit()
        return new_location
    except:
        session.rollback()
        raise Exception("Could not create a new location.")
# removes a location given a location_id  
def remove_location(location_id: int):
    try:
        location=session.query(Location).filter_by(id=location_id).first()
        if not location:
            raise Exception("Location not found.")
        session.delete(location)
        session.commit()
    except:
        session.rollback()
        raise Exception("Could not delete location")
# finds a location given an id and returns the name
def find_location_by_id(location_id: int):
    location = session.query(Location).filter_by(id=location_id).first()
    if location:
        return location.name
    else:
        raise ValueError(f"No location found with id {location_id}")

# finds zombies by id and returns the description
def find_zombie_by_id(zombie_id: int):
    zombie = session.query(Zombie).filter_by(id=zombie_id).first()
    if zombie:
        return zombie.description 
    else:
        raise ValueError(f"No zombie found with id {zombie_id}")
# finds person by id and returns the name and health
def find_person_by_id(person_id: int):
    person = session.query(Person).filter_by(id=person_id).first()
    if person:
        output_slow(f"{person.name} with {person.health} health")
    else:
        raise ValueError(f"No person found with id {person_id}")



# removes a person given an id
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


# creates a person
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
    output_slow("Please enter character name: ")
    person_name = input()
    if person_name:
        create_person(person_name)  
        output_slow(f"Added {colored(person_name, 'green')} to list of characters.")
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
        return person
     except:
        session.rollback()
        raise Exception("Could not update person.")
             
# retrieves all the names of the people in a top to bottom string format
def get_all_names():
    people = session.query(Person).all()
    info = [colored(f'\nName: {person.name} | Health: {person.health}\n', 'green') for person in people]
    return output_slow('\n'.join(info))

def get_all_names_list():
    return session.query(Person).all()
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
            output_slow(f'\n{colored(person_name, "red")} has been taken! Game over...\n')
            display_ending()
            return main_game()
            
            
        elif zombie_count > 0 and person.health > zombie_count:
            person.health -= zombie_count
            if location_id == 3:
                output_slow(colored(f"{person.name}'s health will go down by {zombie_count} since there are {zombie_count} zombies here.", 'red'))
                output_slow(colored(f'{person_name} is injured and left with {person.health} health. {person.name} runs away back to the street.', 'red'))
            elif location_id == 2:
                output_slow(colored(f"{person.name}'s health will go down by {zombie_count} since there are {zombie_count} zombies here.", 'red'))
                output_slow(colored(f'{person_name} is injured and left with {person.health} health. {person.name} throws the broken branch to the side to distract the zombies.', 'red'))
            elif location_id == 7:
                output_slow(colored(f"{person.name}'s health will go down by {zombie_count} since there are {zombie_count} zombies here.", 'red'))
                output_slow(colored(f'{person_name} is injured and left with {person.health} health. {person.name} quickly closes the door of the gun room.', 'red'))
            elif location_id == 5:
                output_slow(colored(f"{person.name}'s health will go down by {zombie_count} since there are {zombie_count} zombies here.", 'red'))
                output_slow(colored(f'{person_name} is injured and left with {person.health} health. {person.name} jumps over the fence safely with the zombies close behind.', 'red'))
            elif location_id == 4:
                output_slow(colored(f"{person.name}'s health will go down by {zombie_count} since there are {zombie_count} zombies here.", 'red'))
                output_slow(colored(f"{person_name} is injured and left with {person.health} health. {person.name} runs back into the ofice and closes the door.", 'red'))
            elif location_id == 9:
                output_slow(colored(f"{person.name}'s health will go down by {zombie_count} since there are {zombie_count} zombies here.", 'red'))
                output_slow(colored(f"It looks like {person.name} has some visitors! Running at the speed of light {person.name} gets to the parking lot of the grocery store, but is left with {person.health} health.", 'red'))
        elif zombie_count == 0:
            output_slow(f'{person_name} is safe for now...No zombies in sight.')

        session.commit()
    except:
        session.rollback()
        raise Exception("Could not affect person's health with zombies.")
    # adds zombies to database in locations specified
def add_zombies():
    locations= [2,3,4,5,6,7,9]
    zombies = []
    try:
        
        number_of_zombies = int(input("Enter the number of zombies you want to add: "))
        for _ in range(number_of_zombies):
            location_id = random.choice(locations)
            health = random.randint(1,30)
            description = f"Zombie with health {health}"

            zombie = (Zombie(description = description, health = health, location_id = location_id))
            zombies.append(zombie)
        session.add_all(zombies)
        session.commit()
        output_slow(f"Added {number_of_zombies} zombies to the database. Good luck...")
    except:
        output_slow("Number of zombies must be a positive integer")
        # removes zombies from database
def remove_zombies():
    try:
        number_of_zombies = int(input("Enter the number of zombies you want to remove: "))

        if number_of_zombies < 0 or not int:
            output_slow("Number of zombies must be positive integer.")
            return
        zombies = session.query(Zombie).all()

        if len(zombies) < number_of_zombies:
            output_slow(f'There are only {len(zombies)} zombies. You need to have at least 1 zombie!')
            number_of_zombies = len(zombies)
    
        zombies_to_remove = random.sample(zombies, number_of_zombies)

        try:
            for zombie in zombies_to_remove:
                session.delete(zombie)
            session.commit()
            output_slow(f"Removed {number_of_zombies} zombies from the database.")
        except:
            session.rollback()
            raise Exception("Could not remove zombies from the database.")
    except:
        output_slow("Please enter a valid number of zombies.")

# retrieves zombie with the most health
def get_zombie_with_most_health():
    try:
        boss_zombie = session.query(Zombie).order_by(Zombie.health.desc()).first()
        if boss_zombie:
            return boss_zombie
        else:
            return None
    except:
        raise Exception("Could not get zombie.")
    # updates the zombie with the most health to a different description
def update_zombie_with_most_health():
    try:
        boss_zombie = session.query(Zombie).order_by(Zombie.health.desc()).first()
        if boss_zombie:
            boss_zombie.description = "DISGUSTING AND GIGANTIC ZOMBIE"
            return boss_zombie.description
        else:
            return None
    except:
        raise Exception("Could not get zombie.")
# updates the health of the person by 1
def update_health(person_id):
    try:
        person = session.query(Person).get(person_id)
        if not person:
            print("No person found with the id.")
        person.health += 1
        session.commit()
        output_slow(colored(f"Chuck thanked {person.name} for being a close friend all these years. He tosses {person.name} a beer and {person.name} feels better. {person.name}'s health is now {person.health}!", 'green'))
    except:
        session.rollback()
        raise Exception("Could not update health.")
    # updates the health of the person by 5
def semi_update_health(person_id):
    try:
        person = session.query(Person).get(person_id)
        if not person:
            print("No person found with the id.")
        person.health += 5
        session.commit()
        output_slow(colored(f"{person.name} finds a protein bar and energy drink! In a holding cell?! Crazy. {person.name}'s health is now {person.health}", 'green'))
    except:
        session.rollback()
        raise Exception("Could not update health.")
    # updates the health of the person by 10
def super_update_health(person_id):
    try:
        person = session.query(Person).get(person_id)
        if not person:
            print("No person found with the id.")
        person.health += 10
        session.commit()
        output_slow(colored(f"SCORE! It looks like someone is looking out for {person.name}. While searching the desk, much needed supplements were found-{person.name}'s health increased by 10!", 'green'))
    except:
        session.rollback()
        raise Exception("Could not update health.")
    # updates the health of the person by 50
def dog_update_health(person_id):
    try:
        person = session.query(Person).get(person_id)
        if not person:
            print("No person found with the id.")
        person.health += 50
        session.commit()
        output_slow(colored(f"Having a dog close by increases {person.name}'s health by 50!!! It is now {person.health}!", 'green'))
    except:
        session.rollback()
        raise Exception("Could not update health")
# shows the list of zombies in each location
def get_number_of_zombies_per_location():
    locations = session.query(Location).all()
    info = []
    for location in locations:
        zombie_count = session.query(Zombie).filter_by(location_id=location.id).count()
        info.append(colored(f'\nLocation: {location.name} | Number of Zombies: {zombie_count}\n', 'red'))
    return output_slow('\n'.join(info))

# everything below is logic for cli

def display_menu(): 
    output_slow(
    '1. Start\n'
    '2. Zombie Locations\n'
    '3. Add Person\n4. Add Zombies\n5. Remove Zombies')

def display_welcome():
    output_slow(colored(r"""
W    W  AAAAA  L       K   K  I  N   N  GGGG       DDDD   EEEEE  AAAAA  DDDD
W    W  A   A  L       K  K   I  NN  N  G          D   D  E      A   A  D   D 
W W W   AAAAA  L       K K    I  N N N  G  GG      D   D  EEEE   AAAAA  D   D 
W W W   A   A  L       K  K   I  N  NN  G   G      D   D  E      A   A  D   D 
 W W    A   A  LLLLL   K   K  I  N   N  GGGG       DDDD   EEEEE  A   A  DDDD
""", 'red'))

def display_ending():
    output_slow(colored(r""" ▄· ▄▌      ▄• ▄▌    ▄▄▌        .▄▄ · ▄▄▄▄▄    ▄▄ 
▐█▪██▌▪     █▪██▌    ██•  ▪     ▐█ ▀. •██      ██▌
▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ██▪   ▄█▀▄ ▄▀▀▀█▄ ▐█.▪    ▐█·
 ▐█▀·.▐█▌.▐▌▐█▄█▌    ▐█▌▐▌▐█▌.▐▌▐█▄▪▐█ ▐█▌·    .▀ 
  ▀ •  ▀█▄▀▪ ▀▀▀     .▀▀▀  ▀█▄▀▪ ▀▀▀▀  ▀▀▀      ▀ """, 'red') + "\n\n")
    
def display_congrats():
    output_slow(colored(r""" ▄· ▄▌      ▄• ▄▌    ▄▄▌ ▐ ▄▌       ▐ ▄     ▄▄ ▄▄ ▄▄ 
▐█▪██▌▪     █▪██▌    ██· █▌▐█▪     •█▌▐█    ██▌██▌██▌
▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ██▪▐█▐▐▌ ▄█▀▄ ▐█▐▐▌    ▐█·▐█·▐█·
 ▐█▀·.▐█▌.▐▌▐█▄█▌    ▐█▌██▐█▌▐█▌.▐▌██▐█▌    .▀ .▀ .▀ 
  ▀ •  ▀█▄▀▪ ▀▀▀      ▀▀▀▀ ▀▪ ▀█▄▀▪▀▀ █▪     ▀  ▀  ▀  """, 'green') + "\n\nDo you want to play again?\n\n")

def main_game():
    
    
    
    while True:
        display_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
           output_slow("Here are a list of people you can choose from:")
           get_all_names()
           person_choice = input('Choose a person from the list by typing in their name or press enter to cancel...')
           try:
                if person_choice:
                    chosen_person = session.query(Person).filter_by(name=person_choice).first()
                    print((f'You have chosen {chosen_person.name} with {chosen_person.health} health!'))
                    output_slower("\n...Starting...\n")
                    output_slow(f"{chosen_person.name} wakes up confused in their bedroom knowing they need to get to the grocery store. {chosen_person.name} steps out to the street vigilant of any surrounding danger.")
                    display_first_scene(chosen_person)
           except:
               output_slow("Invalid choice. Please choose a valid person name.")
               
            
        elif choice == '2':
            output_slow("It looks like there is some info on where all the zombies might be.")
            get_number_of_zombies_per_location()

        elif choice == '3':
            add_character()
        elif choice == '4':
            add_zombies()
        elif choice == '5':
            remove_zombies()
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 5.')





def display_first_scene(person):
   
    while True:
         
         output_slow("1. Walk across the street to the park.\n2. Go explore the abandoned rv camp.\n3. Head to the graveyard where you hear cries for help.\n4. Get health")
         choice = input("Enter your choice...")
         if choice == "1":
              output_slow("The park has a collapsed playground with a torn swing, it's eerily quiet....There seems to be nothing here.")
         elif choice == "2":
              output_slow(colored("The still silence of the camp is broken by sudden screaming...ZOMBIES!", 'red'))
              update_person_location(person.id, 3)
              zombie_attack(person.id, 3)
         elif choice == "3":
             display_second_scene(person)
         elif choice == "4":
             output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
         else:
            output_slow('Invalid choice. Please enter a number between 1 and 4.')


def display_second_scene(person):
    
    chuck_has_helped = False
    output_slow(f"The gates of the graveyard reveal themselves and {person.name} is hesitant to move toward them. Maybe it's best to continue down the street toward the town square.")
    while True:
        output_slow("1. Explore who's been yelling for help in the graveyard.\n2. Go around the graveyard toward the abandoned gravel road.\n3. Head toward the town square where you can hear the distant song of 'Joy to the World' being played.\n4. Climb the tree over the gate to avoid making sounds.\n5. Get health")
        choice = input("Enter your choice...")           
        if choice == "1":
            if chuck_has_helped:
                output_slow("Chuck is no longer here, he left a note saying he hopes the grocery store is as safe as everyone says it is.")
            else:
                output_slow(f"It's Chuck - a long time close friend, he says he came from the town square where he last saw a zombie.")
                update_health(person.id)
                chuck_has_helped = True
        elif choice == "2":
            abandoned_road_scene(person)
            chuck_has_helped = False
        elif choice == "3":
            town_square(person)
            chuck_has_helped = False
        elif choice == "4":
            output_slow(colored(f"The gates were already open, but {person.name} had the right idea. Unfortunately, {person.name} broke a branch on the way over and caught the attention of some unwanted company...", 'red'))
            update_person_location(person.id, 2)
            zombie_attack(person.id, 2)
        elif choice == "5":
            output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 4.')

supplements_found = False
dog_here = True
eaten = False

def abandoned_road_scene(person):
    output_slow(f"The gravel road leads to out of town, but {person.name} remembers a backway to the grocery store, but they have to cross the high school football field.")
    while True:
         output_slow("1. Keep going down the road to the high school.\n2. Turn back to the graveyard.\n3. Get health ")
         choice = input("Enter your choice...")
         if choice == "1":
            output_slow("The abandoned road seems quiet, but the distant sounds of zombies are closing in.")
            high_school_scene(person)
         elif choice == "2":
             output_slow(f"{person.name} heads back to the graveyard. With the zombies closing in it looks like the only option is to...\n1. Head to the town square...")
             choice = input("Enter the last choice...")
             if choice == "1":
                 town_square(person)
             else:
                 output_slow('SMH. Just enter 1...')
         elif choice == "3":
             output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
         else:
             output_slow('Invalid choice. Please enter a number between 1 and 3.')
             
            
             
def high_school_scene(person):
    output_slow(f"The remnants of a forgotten game are strewn about the field in a haphazard fasion. Like the gunners of a kicking team, {person.name} sees the zombies running quickly toward them foaming at the mouth. The grocery store's lights are close.")
    while True:
        output_slow(f"1. Test out your running skills and make a run for the fence behind the grocery store.\n2. Panic and attempt to hide behind the bleachers.\n3. Continue down the road to the drug store.\n4. Get health")
        choice = input("Enter your choice...")
        if choice == "1":
            update_person_location(person.id, 5)
            zombie_attack(person.id, 5)
            grocery_store_parking_lot(person)
        elif choice == "2":
            remove_person(person.id)
            output_slow(colored("Maybe running isn't such a bad idea after all. Sorry, you didn't make it..", 'red'))
            display_ending()
            main_game()
        elif choice == "3":
            output_slow("The back of the drug store comes up out of the darkness with broken windows and empty pill bottles littered around the dumpster.")
            drug_store_scene(person)
        elif choice == "4":
            output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 4.')


def drug_store_scene(person):
    output_slow(f"{person.name} creeps toward the back door of the drug store next to the post office and debates whether to make a run to the grocery store or wait it out awhile in the drug store.")
    while True:
        output_slow("1. Head into the drug store.\n2. Go around the building into the town square.\n3. Stop and gather your thoughts.\n4. Get health")
        choice = input("Enter your choice...")
        if choice == "1":
            inside_drug_store(person)
        elif choice == "2":
            town_square(person)
        elif choice == "3":
            remove_person(person.id)
            output_slow(colored("Everyone is up for a little introspection now and then...maybe now isn't the best time?", 'red'))
            display_ending()
            main_game()
        elif choice == "4":
            output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 4.')
            


def inside_drug_store(person):
    global supplements_found
    output_slow(f"{person.name} finds the drug store door unlocked and edges their way inside. They look around the back office room.")
    while True:
        output_slow("1. Sit down on the office chair and wait.\n2. Search the main store for some drugs.\n3. Head back outside to the town square.\n4. Get health")
        choice = input("Enter your choice...")
        if choice == "1":
            if supplements_found:
                output_slow(f"{person.name} has already raided the stash. There is nothing left here.")
            else:
                super_update_health(person.id)
                supplements_found = True
        elif choice == "2":
            output_slow(colored(f"Creeping through the store, {person.name} slips on an old dollar bill--the zombies of the store wake up!", 'red'))
            update_person_location(person.id, 4)
            zombie_attack(person.id, 4)
            
        elif choice == "3":
            town_square(person)
        elif choice == "4":
            output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 4.')
            

def town_square(person):
    output_slow(f"The song 'Joy to the World is on blast and repeat-{person.name} thinks of better times. Looking around, {person.name} looks around at the empty plaza and decides what to do next.")
    while True:
        output_slow(f"1. Head toward the police station across the street to see if you can get help.\n2. Head to the post office next to the drug store.\n3. Make a dash for the grocery store.\n4. Get health")
        choice = input("Enter your choice...")
        if choice == "1":
            police_station(person)
        elif choice == "2":
            post_office(person)
        elif choice == "3":
            update_person_location(person.id, 9)
            zombie_attack(person.id, 9)
            grocery_store_parking_lot(person)
        elif choice == "4":
            output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 4.')

def police_station(person):
    global eaten
    output_slow(f"{person.name} flies across the plaza and dives head first through a broken windown of the police station. {person.name} looks at their options.")
    while True:
        output_slow(f"1. Head to the holding cell where the static of a walky talky makes {person.name} reluctant to explore.\n2. Head to the gun room, there might be something to protect {person.name} with.\n3. Go back outside to see if you're safe.\n4. Get health")
        choice = input("Enter your choice...")
        if choice == "1":
            if eaten:
                output_slow(f"Bummer. There is no more food or drink for {person.name}")
            else:
                semi_update_health(person.id)
                eaten = True
        elif choice == "2":
            output_slow(colored("The gun room is full of zombies? Very counterintuitive.", 'red'))
            update_person_location(person.id, 7)
            zombie_attack(person.id, 7)
            
        elif choice == "3":
            output_slow(f"{person.name} heads back outside of the police station. With the zombies closing in it looks like the only option is to...\n1. Head to the post office...")
            choice = input("Enter the last choice...")
            if choice == "1":
               post_office(person)
            else:
                output_slow("Just press 1 and enter...")
        elif choice == "4":
            output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 4.')

def post_office(person):
    global dog_here
    output_slow(f"{person.name} creeps up to the old post office door and quickly gets inside. Old letters are are scattered across the floor with Amazon packages.")
    while True:
        output_slow(f"1. Check inside the Amazon packages to see if you can find anything useful.\n2. Go into the back room where where the lights flicker and a bad feeling looms.\n3. Exit the post office and go around the back.\n4. Stop to read a helpful note about how to stop the zombies.\n5. Get health")
        choice = input("Enter your choice...")
        if choice == "1":
            output_slow("Bathroom products, electronics, self-help books, nothing of use at this moment")
            
        elif choice == "2":
            if not dog_here:
                output_slow("The room where the dog was trapped doesn't look too nice.")
            else:
                output_slow("A thankful German Shepard appears, it must've been locked in the room all this time!")
                interact_with_dog(person)
                dog_here = False
            
                
        elif choice == "3":
            drug_store_scene(person)
            
        elif choice == "4":
            output_slow(colored(f"Looks like there is no stopping these things through the power of reading, unfortunately {person.name} has been taken while studying the note!", 'red'))
            remove_person(person.id)
            display_ending()
            main_game()
        elif choice == "5":
            output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 5.')

def interact_with_dog(person):
    global dog_here
    output_slow(f"{person.name} wonders what to do with the dog, hoping it won't be too loud and get them caught. What to do with the dog?")
    while True:
        output_slow("1. Give the dog a pet and treat.\n2. Ignore the dog and continue on in the town square.\n3. Teach the dog how to shake.\n4. Get health")
        choice = input("Enter your choice...")
        if choice == "1":
            if person.health > 30:
                output_slow("The dog is thankful for the treat and wags its tail.")
            else:
                output_slow(f"The dog seems to be attached to {person.name} and follows them everywhere. Time to head back to the town square.")
                dog_update_health(person.id)
                dog_here = False
                town_square(person)
        elif choice == "2":
            output_slow("The dog is probably too loud, it's time to go back to the town square.")
            dog_here = False
            town_square(person)
        elif choice == "3":
            output_slow(colored(f"No time for getting to know the pet on a time crunch, {person.name} has been taken! The dog gets away.", 'red'))
            remove_person(person.id)
            main_game()
        elif choice == "4":
            output_slow(colored(f"{person.name} | Health: {person.health}", 'green'))
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 4.')


def grocery_store_parking_lot(person):
    output_slow(f"Hiding behind a car and looking at the beautiful and welcoming lights of the grocery store, {person.name} hears the most ungodly growl behind them.")
    update_zombie_with_most_health()
    boss_zombie = get_zombie_with_most_health()
    output_slow(colored(f"A {boss_zombie.description} reveals itself and {person.name} is terriied. They better hope their health is more than {boss_zombie.health} or they are done for.", 'red'))
    while True:
        output_slow("1. Fight the beast.\n2. Get in a feedle position and hope it goes away.\n3. Get health ")
        choice = input("Choose wisely...")
        if choice == "1":
            if person.health > boss_zombie.health:
                output_slow(colored(f"In a miraculous turn of events, {person.name} gets away from the foul beast and reaches the grocery store safely barricaded.", 'green'))
                display_congrats()
                main_game()
            else:
                remove_person(person.id)
                output_slow(colored("While the courage is admired, it won't go far with that thing. Try again next time!", 'red'))
                display_ending()
                main_game()
                
        elif choice == "2":
                output_slow(colored("A FEEDLE position?! Do you think it's a bear?! No time to play possum shmossum. Try again next time!", 'red'))
                remove_person(person.id)
                display_ending()
                main_game()
        elif choice == "3":
                output_slow("Make a decision.....it's waiting for you...")
        else:
            output_slow('Invalid choice. Please enter a number between 1 and 2.')
    
    



            



          
        
            


            
                
                







