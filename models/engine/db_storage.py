#!/usr/bin/python3
"""file storage DB for AirBnB"""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from os import environ


class DBStorage:
    """ DB with SQL Alchemy and MySQL """
    __engine = None
    __session = None

    def __init__(self):
        """ environment """

        sqlUser = environ.get('HBNB_MYSQL_USER')
        sqlPwd = environ.get('HBNB_MYSQL_PWD')
        sqlHost = environ.get('HBNB_MYSQL_HOST')
        sqlDb = environ.get('HBNB_MYSQL_DB')
        sqlEnv = environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(sqlUser, sqlPwd, sqlHost, sqlDb),
                                      pool_pre_ping=True)

        if sqlEnv == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on current DB session (self.__session)"""

        session = self.__session
        dic = {}
        if not cls:
            tables = [User, State, City, Amenity, Place, Review]

        else:
            if type(cls) == str:
                cls = eval(csl)

            tables = [cls]

        for t in tables:
            query = session.query(t).all()

            for rows in query:
                key = "{}.{}".format(type(rows).__name__, rows.id)
                dic[key] = rows

        return dic

    def new(self, obj):
        """ add object to current DB session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ commit all changes of current DB session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from module import symbol """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the DB"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.close()
