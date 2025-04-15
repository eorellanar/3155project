from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from ..dependecies.database import Base

class Promotion(Base):
    __tablename__ = 'promotions'
    promotion_code = Column(Integer)
    expiration_date = Column(DateTime)