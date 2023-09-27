from models import *
from helpers import *




engine = create_engine('sqlite:///zombie.db')
session = sessionmaker(bind=engine)
session = Session()


#molly added line 11-20
def display_welcome():
    print(r"""
W    W  AAAAA  L       K   K  I  N   N  GGGG       DDDD   EEEEE  AAAAA  DDDD  
W    W  A   A  L       K  K   I  NN  N  G          D   D  E      A   A  D   D 
W W W   AAAAA  L       K K    I  N N N  G  GG      D   D  EEEE   AAAAA  D   D 
W W W   A   A  L       K  K   I  N  NN  G   G      D   D  E      A   A  D   D 
 W W    A   A  LLLLL   K   K  I  N   N  GGGG       DDDD   EEEEE  A   A  DDDD  
""")
def press_enter():
    input("Press Enter to continue...")

# display menu will show the output of all the logic in the cli
def display_menu(): 
    output_slow(
    '1. Show People\n'
    '2. See Zombie Info\n'
    '3. Start the game\n'
    '4. Add Person')

#molly added line 31-37
def add_character():
    print("Please enter character name (first and last): ")
    person_name = input()
    if person_name:
        person_instance = create_person(person_name)  
        print(f"Added {person_name} to list of characters.")
    press_enter()
        


if __name__ == "__main__":
#molly added line 43
    display_welcome() 
    

    output_slow(
            "Hello there...Welcome to your next adventureee")

    while True:
        display_menu()
   
        choice = input('Enter your choice: ')
        if choice == '1':
           output_slow("Here are a list of people you can choose from:")
           get_all_names()
           person_choice = input('Choose a person from the list by typing in their name or press enter to cancel...')
           if person_choice:
               chosen_person = session.query(Person).filter_by(name=person_choice).first()
               print((f'You have chosen {chosen_person.name} with {chosen_person.health} health'))
               output_slow(f"{chosen_person.name} wakes up confused in their bedroom knowing they need to get to the grocery store. {chosen_person.name} steps out to the street vigilant of any surrounding danger.")
               display_first_scene(chosen_person.id)
           else:
               output_slow("Invalid choice. Please choose a valid person name.")
            
        elif choice == '2':
            output_slow("It looks like there is some info on where all the zombies might be.")
            get_number_of_zombies_per_location()
        elif choice == '3':
            
            break
        elif choice == '4':
            add_character()
        else:
            print('Invalid choice. Please enter a number between 1 and 3.')
            