from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    health = Column(Integer())
    location_id = Column(Integer(), ForeignKey('locations.id'))
    weapon_id = Column(Integer(), ForeignKey('weapons.id'))

    weapon = relationship('Weapon', back_populates='person')
    location = relationship('Location', back_populates='people')


class Zombie(Base):
    __tablename__ = "zombies"

    id = Column(Integer(), primary_key=True)
    description = Column(String())
    health = Column(Integer())
    location_id = Column(Integer(), ForeignKey('locations.id'))

    location = relationship('Location', back_populates='zombies')

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    people = relationship('Person', back_populates='location')
    zombies = relationship('Zombie', back_populates='location')
    weapons = relationship('Weapon', back_populates='location')

class Weapon(Base):
    __tablename__ = "weapons"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    damage = Column(Integer())

    person_id = Column(Integer(), ForeignKey('people.id'))
    location_id = Column(Integer(), ForeignKey('locations.id'))

    person = relationship('Person', back_populates='weapon')
    location = relationship('Location', back_populates='weapons')
