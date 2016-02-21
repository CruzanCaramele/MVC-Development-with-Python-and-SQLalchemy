from sqlalchemy import asc, desc, Date, create_engine
from sqlalchemy.orm import sessionmaker
from puppyshelters import Base, Shelter, Puppy

engine = create_engine("sqlite:///puppies.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#Query all of the puppies and return the results in ascending alphabetical order
puppies = session.query(Puppy).order_by(Puppy.name).all()
for puppy in puppies:
	print puppy.name


# Query all of the puppies that are less than 6 months old organized by the youngest first
puppies_six_months = session.query(Puppy).filter(Puppy.dateOfBirth >= "2015-06-01").order_by(asc(Puppy.dateOfBirth))
for puppies in puppies_six_months:
	print puppies.dateOfBirth


# Query all puppies by ascending weight
puppyWeights = session.query(Puppy).order_by(asc(Puppy.weight)).all()
for puppyWeight in puppyWeights:
	print puppyWeight.weight


#Query all puppies grouped by the shelter in which they are staying
puppyHomes = session.query(Puppy).order_by(Puppy.shelter_id)
for puppyHome in puppyHomes:
	print puppyHome.name + ' : ' + puppyHome.shelter.name