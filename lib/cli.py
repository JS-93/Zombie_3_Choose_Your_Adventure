from models import *
from helpers import *
import random

engine = create_engine('sqlite:///zombie.db')
session = sessionmaker(bind=engine)
session = Session()




# display menu will show the output of all the logic in the cli
def display_menu(): 
    output_slow(
    '1. Show People\n'
    '2. Create Your Own Character\n'
    '3. Start at the game with random person')

def display_first_scene():
    output_slow(
        '1. '
    )

if __name__ == "__main__":
    def get_random_health():
        return random.randint(1,10)

    def get_random_location():
        return random.randint(1,4)

    output_slow("Hello there...Welcome to your next adventureee")
    while True:
        display_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
           get_all_names()
           person_choice = input('Choose a person from the list by typing in their name or press enter to cancel...')
           if person_choice:
               chosen_person = session.query(Person).filter_by(name=person_choice).first()
               print((f'You have chosen {chosen_person.name} with {chosen_person.health} health'))
           else:
               print("Invalid choice. Please choose a valid person name.")
            
        elif choice == '2':
            person_name = input('Please type in a name: ')
            if isinstance(person_name, str):
                 print(f'Hello {person_name}!')
                 create_person(name = person_name, health = get_random_health(), location_id = get_random_location())
            else:
                print("Please enter a name with only letters!")
                
            
        elif choice == '3':
            break  # Exit the loop and end the program
        else:
            print('Invalid choice. Please enter a number between 1 and 3.')



# def affect_health(location_name, person_id):
#     zombies_amount = len(zombie for zombie in Location if location.name is location_name)
#     if zombies_amount > person.health and person.id is person_id:
#         person.delete()
#     else:
#         print("There are no zombies here")
    
