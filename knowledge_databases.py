from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,topic,rating):
	artical_object = Knowledge(
		name = name,
		topic=topic,
		rating=rating)
	session.add(artical_object)
	session.commit()


add_article("health" , "psychology" , 9)
add_article("body" , "biology" , 10)

def query_all_articles():
	articals = session.query(
		Knowledge).all()
	return articals

print(query_all_articles())
	

def query_article_by_topic():
	articals = session.query(
		Knowledge).filter_by(
		topic=their_topic)
	return articals

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
