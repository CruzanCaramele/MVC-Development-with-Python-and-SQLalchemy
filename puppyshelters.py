import sys
import datetime
from sqlalchemy import Table, Date, String, Column, Integer, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


association_table = Table("association", Base.metadata,
					Column("puppy_id", Integer, ForeignKey("puppy.id")),
					Column("adopters_id", Integer, ForeignKey("adopters.id")),
					)

class Shelter(Base):
	"""docstring for Shelter"""

	__tablename__ = "shelter"

	name = Column(String(80), nullable=False)
	address = Column(String(150), nullable=False)
	city = Column(String(60))
	state = Column(String(50))
	zipCode = Column(Integer)
	website = Column(String(120))
	maximum_capacity = Column(Integer)
	current_occupancy = Column(Integer)
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

	shelter = relationship("Shelter")
	puppyprofile = relationship("PuppyProfile", uselist=False, back_populates="puppy")

	adopters = relationship("adopters", secondary=association_table, back_populates="puppy")


class PuppyProfile(Base):
	"""docstring for PuppyProfile"""

	__tablename__ = "puppyprofile"

	photoUrl = Column(String(120))
	description = Column(String(220))
	specialNeeds = Column(String(200))
	puppy_id = Column(Integer, ForeignKey("puppy.id"))

	puppy = relationship("Puppy", back_populates="puppyprofile")
	id = Column(Integer, primary_key=True)


class adopters(Base):
	"""docstring for adopters"""

	__tablename__ = "adopters"

	name = Column(String(100))
	id   = Column(Integer, primary_key=True)
	phone = Column(String(10))

	puppy = relationship("Puppy", secondary=association_table, back_populates="adopters")
		
		

engine = create_engine("sqlite:///puppies.db")
Base.metadata.create_all(engine)