#!/usr/bin/python3
'''sql db'''
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from sqlalchemy import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base

class DBStorage:
    '''db engine'''
    __engine = None
    __session = None

    def __init__(self):
        '''initialize db engine'''
        usr = getenv('HBNB_MYSQL_USER')
        pswd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                                      format(usr, pswd, host, db,
                                             pool_pre_ping=True))
        if getenv('HBNB_MYSQL_ENV') == 'test':
            drop_all(self.__engine)

    def all(self, cls=None):
        '''show all objects'''
        if cls:
            query = self.__session.query(cls).all()
        else:

    def new(self, obj):
        '''add object to current database session'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete object from current database session'''
        if obj:
            return self.__session.delete(obj)

    reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
