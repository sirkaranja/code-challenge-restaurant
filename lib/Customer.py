from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine= create_engine('sqlite:///customer.db')
session = sessionmaker(bind=engine)


class Customer(Base):
    __tablename__= 'customers'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    family_name = Column(String)

    all_customers=[]

    def __init__(self, surname, family_name):
        self.last_name= surname
        self.family_name=family_name
        Customer.all_customers.append(self)

    def surname(self):
        return self.last_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.family_name} {self.last_name}"

    @classmethod
    def all(cls):
        return cls.all_customers
        



