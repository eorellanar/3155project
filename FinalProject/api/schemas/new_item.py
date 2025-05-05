from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    dishes: str
    price: float

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    dishes: Optional[str] = None
    price: Optional[float] = None

class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True