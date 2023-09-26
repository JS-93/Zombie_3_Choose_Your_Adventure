from models import *
from helpers import *




def display_menu():
    output_slow(
    '1. Show People\n'
    '2. Create Your Own Character\n'
    '3. Start at random')

if __name__ == "__main__":
    output_slow("Hello there...Welcome to your next adventureee")
    while True:
        display_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
           print(get_all_names())
           person_choice = input('Choose a person from the list or press enter...')
           if person_choice:
               chosen_person = session.query(Person).filter_by(name=person_choice).first()
               print((f'You have chosen {chosen_person.name} with {chosen_person.health} health'))
           else:
               print("Invalid choice. Please choose a valid person name.")
            
        elif choice == '2':
            pass
        elif choice == '3':
            break  # Exit the loop and end the program
        else:
            print('Invalid choice. Please enter a number between 1 and 3.')

