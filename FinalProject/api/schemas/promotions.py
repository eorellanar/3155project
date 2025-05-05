from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PromotionBase(BaseModel):
    promo_code: str
    expiration_date: datetime

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    promo_code: Optional[str] = None
    expiration_date: Optional[datetime] = None

class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True