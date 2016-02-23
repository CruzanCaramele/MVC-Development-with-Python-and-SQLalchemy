import random
import datetime
from random import randint
from sqlalchemy import asc, desc, Date, create_engine
from sqlalchemy.orm import sessionmaker
from puppyshelters import Base, Shelter, Puppy

engine = create_engine("sqlite:///puppies.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def all_names():
	#Query all of the puppies and return the results in ascending alphabetical order
	puppies = session.query(Puppy).order_by(Puppy.name).all()
	for puppy in puppies:
		print puppy.name

def six_months():
	# Query all of the puppies that are less than 6 months old organized by the youngest first
	puppies_six_months = session.query(Puppy).filter(Puppy.dateOfBirth >= "2015-06-01").order_by(asc(Puppy.dateOfBirth))
	for puppies in puppies_six_months:
		print puppies.dateOfBirth

def weight_order():
	# Query all puppies by ascending weight
	puppyWeights = session.query(Puppy).order_by(asc(Puppy.weight)).all()
	for puppyWeight in puppyWeights:
		print puppyWeight.weight

def all_puppies():
	#Query all puppies grouped by the shelter in which they are staying
	puppyHomes = session.query(Puppy).order_by(Puppy.shelter_id)
	for puppyHome in puppyHomes:
		print puppyHome.name + ' : ' + puppyHome.shelter.name


def check_into_shelter(shelter_id):
	#check a puppy into a shelter
	shelter = session.query(Shelter).filter_by(id=shelter_id).one()

	puppy_name = raw_input("Puppy's Name: ")
	#birthday   = datetime.date(raw_input("Date of Birth: "))
	gender     = raw_input("Gender: ")
	weight     = raw_input("Weight: ")

	newPuppy = Puppy(name=puppy_name, gender=gender,weight=weight)

	session.add(newPuppy)
	session.commit()


shelter_id = random.randint(1,4)
check_into_shelter(shelter_id)

