from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, WeatherRecord, Category, City

engine = create_engine('sqlite:///weather.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

berlin = City(id=10382, name='Berlin')
moscow = City(id=27612, name='Moscow')

session.add(berlin)
session.add(moscow)

session.commit()
