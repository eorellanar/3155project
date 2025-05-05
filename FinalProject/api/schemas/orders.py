from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    delivery_type: str


class OrderCreate(BaseModel):
    customer_name: str
    description: Optional[str] = None
    promo_code: Optional[str] = None
    delivery_type: Optional[str] = None

    class Config:
        orm_mode = True


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
