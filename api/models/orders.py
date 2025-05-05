from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    tracking_num = Column(Integer)
    order_status = Column(String(100))
    total_price = Column(DECIMAL(4,2))