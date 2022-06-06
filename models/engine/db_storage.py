#!/usr/bin/python3
"""
db storage mysql server
"""


from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """
    New engine DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        constructor de clase
        """
        my_host = os.environ.get("HBNB_MYSQL_HOST")
        usuario = os.environ.get("HBNB_MYSQL_USER")
        contrasena = os.environ.get("HBNB_MYSQL_PWD")
        entorno = os.environ.get("HBNB_ENV")
        base = os.environ.get("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(usuario, contrasena,
                                              my_host, base),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if entorno == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        all method return dictionary of cls
        """
        clases = [State, City, User, Place, Review, Amenity]
        if type(cls) == str:
            cls = eval(cls)
        if cls is None:
            lista = []
            for i in clases:
                lista.extend(self.__session.query(i).all())
        else:
            lista = self.__session.query(cls)
        diccionario_retorno = {}
        for j in lista:
            j.__dict__.pop('_sa_instance_state')
            diccionario_retorno[j.__class__.__name__ + '.' + j.id] = j
        return diccionario_retorno

    def new(self, obj):
        """
        new object to db
        """
        if (obj.__class__.__name__ == 'User'):
            if 'first_name' not in obj.__dict__.keys():
                obj.__dict__['first_name'] = None
            if 'last_name' not in obj.__dict__.keys():
                obj.__dict__['last_name'] = None
        self.__session.add(obj)

    def save(self):
        """
        save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj
        """
        if obj:
            clase = obj.__class__.__name__
            self.__session = clase.delete().where(
                clase.id == obj.__dict__['id'])

    def reload(self):
        """
        create all tables in the database
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()