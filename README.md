**Summary**


Walking Dead is a CLI application choose your own adventure game. A user can view the list of people & health, add a person, add zombies, remove zombies and view zombie health & location. Once a user has chosen a character, the user can follow the prompts to navigate to the end of the game, unless they are killed by zombies, then the game is over. 

**Requirements**


1. Python 3.x 
2. SQLAlchemy
3. Termcolor



**Installing**


To start the program, CD into the Zombie_3_choose_your_adventure directory:

1. In the above directory run: 

pipenv install<br>
pipenv shell<br>
cd lib

2. In the lib directory:

python seed.py<br>
python cli.py<br>


**Usage**


Once the program starts, the user will be able to read the instructions that provide tips to making it to the end of the game. After reading the game instructions, the user will see the main menu with the following choices:

1. Show People
2. Zombie Locations
3. Add Person
4. Add Zombies
5. Remove Zombies

Once you select a person by typing in their full name, you will start at the first scene and get random health from 1-50 assigned to you. After the first scene, you'll navigate through a series of locations and options to try to make it to the end of the game. 

If you run into zombies, your health will be impacted. You will also run into friends who will help you to the end. Good luck!



**Application Structure**



cli.py:
Main file containing the CLI


helpers.py:
A set of helper functions to retrieve and update information from the database.


models.py:
contains the SQLAlchemy models for the Zombies, locations and people


seed.py:
contains data seeding for the database


**Support**
If you encounter issues, please feel free to directly reach out to us via email.
