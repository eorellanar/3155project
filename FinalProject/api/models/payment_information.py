from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependecies.database import Base

class PaymentInformation(Base):
    __tablename__ = 'payment_information'
    card_number = Column(Integer)
    transaction_status = Column(String(100))
    payment_type = Column(String(100))