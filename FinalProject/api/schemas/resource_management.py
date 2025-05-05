from pydantic import BaseModel
from typing import Optional

class ResourceAmountBase(BaseModel):
    resource1: str
    resource1Amount: int
    resource2: str
    resource2Amount: int
    resource3: str
    resource3Amount: int

class ResourceAmountCreate(ResourceAmountBase):
    pass

class ResourceAmountUpdate(BaseModel):
    resource1: Optional[str] = None
    resource1Amount: Optional[int] = None
    resource2: Optional[str] = None
    resource2Amount: Optional[int] = None
    resource3: Optional[str] = None
    resource3Amount: Optional[int] = None

class ResourceAmount(ResourceAmountBase):
    id: int

    class ConfigDict:
        from_attributes = True