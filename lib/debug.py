from ipdb import set_trace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *
from helpers import *

if __name__ == "__main__":

    engine = create_engine('sqlite:///zombie.db')
    session = sessionmaker(bind=engine)()
    
set_trace()

