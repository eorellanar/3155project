from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class ResourceManagement(Base):
    __tablename__ = "resource_management"
    resource1 = Column(String(20))
    resource1Amount = Column(Integer)
    resource2 = Column(String(20))
    resource2Amount = Column(Integer)
    resource3 = Column(String(20))
    resource3Amount = Column(Integer)