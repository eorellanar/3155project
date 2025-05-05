from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base

class RatingsReview(Base):
    __tablename__ = 'ratings_reviews'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)  # <-- Add this
    review_text = Column(String(500))
    rating = Column(Integer)