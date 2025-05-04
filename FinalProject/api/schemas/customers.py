from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True