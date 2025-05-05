from pydantic import BaseModel
from typing import Optional

class PaymentInformationBase(BaseModel):
    card_number: str
    payment_type: str

class PaymentInformationCreate(PaymentInformationBase):
    pass

class PaymentInformationUpdate(BaseModel):
    card_number: Optional[str] = None
    payment_type: Optional[str] = None

class PaymentInformation(PaymentInformationBase):
    id: int

    class ConfigDict:
        from_attributes = True