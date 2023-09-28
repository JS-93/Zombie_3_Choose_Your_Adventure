from models import *
from helpers import *


engine = create_engine('sqlite:///zombie.db')
session = sessionmaker(bind=engine)
session = Session()













if __name__ == "__main__":
    main_game()

                



