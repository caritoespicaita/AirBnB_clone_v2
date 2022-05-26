#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.city import City
from models.amenity import Amenity
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False)
                      )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='place', cascade='all, delete')
        amenities = relationship("Amenity", secondary=place_amenity, backref="place", viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter reviews"""
            from models import storage
            revisar = storage.all(City)
            lista_retorno = []
            for i in revisar.values():
                if self.id == i.state_id:
                    lista_retorno.append(i)
            return lista_retorno
        
        @property
        def amenities(self):
            """Getter amenities"""
            from models import storage
            lugares = storage.all(Amenity)
            lista_retorno = []
            for i in lugares.values():
                if self.id == i.amenity_ids:
                    lista_retorno.append(i)
            return lista_retorno

        @amenities.setter
        def amenities(self, value):
            """ Setter amenities"""
            if type(value) is Amenity:
                self.amenities.append(value)
