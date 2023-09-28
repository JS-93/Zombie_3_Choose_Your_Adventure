from models import *
from helpers import *


engine = create_engine('sqlite:///zombie.db')
session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":
    output_slower("\nWelcome to the Walking Dead Choose Your Own Adventure game:\n")
    output_slower("\nRemember to look at zombie locations to see where they all are so you can strategize your decisions on where to go next.\n")
    output_slower("\nStart by adding your name, press enter, enter 'Show People', and type in exactly how your name looks.\n")
    output_slower("\nAfter you press enter, your character will be taken directly into the game where you start with random health from 1-20.\n")
    output_slower("\nYour character wakes up in their house, but they need to get to the grocery store...\n")
    display_welcome()
    main_game()

                



