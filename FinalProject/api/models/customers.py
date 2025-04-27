from sqlalchemy import Column, Integer, String, Decimal
from sqlalchemy.orm import relationship
from ..dependecies.database import Base

class Customer(Base):
    __tablename__ = 'customers'
    name = Column(String(100))
    email = Column(String(100))
    phone_number = Column(String(100))
    address = Column(String(100))