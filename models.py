import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)

    category_id = Column(String, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='weather')

    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship('Country', back_populates='weather')

    value = Column(Integer)

    def __repr__(self):
        return "'%s'" % self.year


class Category(Base):
    __tablename__ = 'categories'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))


class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

engine = create_engine('sqlite:///weather.db')

Base.metadata.create_all(engine)
