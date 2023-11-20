#!/usr/bin/python3
""" engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """ class definition with private attributes set to None """
    __engine = None
    __session = None

    def __init__(self):
        """ creating the engine linked to MySQL db
        must be retrieved with environment variables specified """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all """
        session = self.__session
        objs = {}
        if cls:
            for obj in session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs[key] = obj
        else:
            for clazz in Base.__subclasses__():
                for obj in session.query(clazz).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """ adds object to current database session """
        self.__session.add(obj)

    def save(self):
        """ commits all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes obj from current database session if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ creates all tables in database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
