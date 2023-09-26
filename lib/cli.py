from models import *
from helpers import *


engine = create_engine('sqlite:///zombie.db')
session = sessionmaker(bind=engine)
session = Session()




# display menu will show the output of all the logic in the cli
def display_menu(): 
    output_slow(
    '1. Show People\n'
    '2. See Zombie Info\n'
    '3. Start the game')



if __name__ == "__main__":
    

    output_slow("Hello there...Welcome to your next adventureee")
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
        else:
            print('Invalid choice. Please enter a number between 1 and 3.')
            

                



# def affect_health(location_name, person_id):
#     zombies_amount = len(zombie for zombie in Location if location.name is location_name)
#     if zombies_amount > person.health and person.id is person_id:
#         person.delete()
#     else:
#         print("There are no zombies here")
    
# person_name = input('Please type in a name: ')
#             if isinstance(person_name, str):
#                  print(f'Hello {person_name}!')
#                  created_person = create_person(name = person_name, health = get_random_health(), location_id = 1)
#                  output_slow(f"{created_person.name} wakes up unaware of their surroundings. They need to get to the grocery store where everyone is so they step outside. The zombies are out there waiting... ")
#                  display_first_scene(created_person)
#             else:
#                 print("Please enter a name with only letters!")
