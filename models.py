import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class WeatherRecord(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)

    category_id = Column(String, ForeignKey('categories.id'))
    category = relationship('Category', backref=backref('weather', uselist=True))

    country_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship('City', backref=backref('weather', uselist=True))

    value = Column(Integer)

    def __repr__(self):
        return "'%s'" % self.year


class Category(Base):
    __tablename__ = 'categories'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


engine = create_engine('sqlite:///weather.db')

Base.metadata.create_all(engine)
