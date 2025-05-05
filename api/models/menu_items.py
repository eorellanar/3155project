from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dishes = Column(String(100))
    ingredients = Column(String(100))
    price = Column(DECIMAL(4, 2))
    calories = Column(Integer)
    food_category = Column(String(100))
