from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "topics"
	article_num =Column(Integer,primary_key=True)
	name=Column(String)
	topic=Column(String)
	rating=Column(Integer)


	def __repr__(self):
		return("article name: {}\n"
				"article topic:{}\n"
				"article rating{}\n").format(
					self.name,
					self.topic,
					self.rating)
		print("If you want to learn about" , self.topic , "you should look at the Wikipedia article called" , self.name
		"we gave this artical a rating of " , self.rating ,"out of 10")


x = Knowledge(name="what happens when you're angry",topic="psychology",rating=9)
y = Knowledge(name= "rainbow",topic= "weather",rating=9)

