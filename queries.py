from sqlalchemy import create_engine
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