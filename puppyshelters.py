import sys
import datetime
from sqlalchemy import Date, String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	"""docstring for Shelter"""

	__tablename__ = "shelter"

	name = Column(String(80), nullable=False)
	address = Column(String(150), nullable=False)
	city = Column(String(60))
	state = Column(String(50))
	zipCode = Column(Integer)
	website = Column(String(120))
	id = Column(Integer, primary_key=True)


class Puppy(Base):
	"""docstring for Puppy"""

	__tablename__ = "puppy"

	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	dateOfBirth = Column(Date)
	gender = Column(String(10), nullable=False)
	weight = Column(String(30))
	picture = Column(String)
	shelter_id = Column(Integer, ForeignKey("shelter.id"))

	shelter = relationship(Shelter)

engine = create_engine("sqlite:///puppies.db")
Base.metadata.create_all(engine)