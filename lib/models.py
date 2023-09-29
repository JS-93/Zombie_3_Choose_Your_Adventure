from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    health = Column(Integer())
    location_id = Column(Integer(), ForeignKey('locations.id'))


    location = relationship('Location', back_populates='people')
    def __repr__(self):
        return f'Person {self.id}:'\
        + f'{self.name}'\
        + f'{self.health}'\
        + f'{self.location_id}'


class Zombie(Base):
    __tablename__ = "zombies"

    id = Column(Integer(), primary_key=True)
    description = Column(String())
    health = Column(Integer())
    location_id = Column(Integer(), ForeignKey('locations.id'))

    location = relationship('Location', back_populates='zombies')

    def __repr__(self):
        return f'Zombie {self.id}:'\
        + f'{self.description}'\
        + f'{self.health}'\
        + f'{self.location_id}'

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    people = relationship('Person', back_populates='location')
    zombies = relationship('Zombie', back_populates='location')

    def __repr__(self):
        return f'Location {self.id}:'\
        + f'{self.name}'\
        + f'{self.people}'\
        + f'{self.zombies}'






