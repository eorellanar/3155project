from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
import enum


class OrderStatus(str, enum.Enum):
    pending = "pending"
    preparing = "preparing"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"
    cancelled = "cancelled"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    tracking_number = Column(String(100), unique=True, index=True)
    order_status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    total_price = Column(DECIMAL(4, 2))
    delivery_type = Column(String(50), default="takeout")
