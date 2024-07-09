from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import logging
from models.product import Product
from models.store import Store
from models.audit import Audit

classes = {"Product": Product, "Store": Store, "Audit": Audit}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqlconnector://admin_mgt:Pwd1.mgt@127.0.0.1/management_db')
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        try:
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()  # Roll back the transaction in case of an error
            raise e
    def rollback(self):
        """Roll back the current transaction."""
        try:
            self.__session.rollback()
        except Exception as e:
            logging.error(f"Error during database rollback: {e}")

    def delete(self, obj=None):
        """Delete obj from the current database session if it's not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
    
    def reload(self):
        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()
        except Exception as e:
            logging.error(f"Error during session reload: {e}")
        # No finally block needed here as we're setting up the session

    def close(self):
        """Call remove() method on the private session attribute."""
        self.__session.close()

    def get(self, cls, id):
        """Return the object based on the class name and its ID, or None if not found."""
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        for value in all_cls.values():
            if value.id == id:
                return value
        return None

    def count(self, cls=None):
        """Count the number of objects in storage."""
        if not cls:
            count = 0
            for clas in classes.values():
                count += len(self.all(clas).values())
        else:
            count = len(self.all(cls).values())

        return count

