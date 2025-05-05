from sqlalchemy import Column, Integer, String
from ..dependecies.database import Base

class RatingsReview(Base):
    __tablename__ = 'ratings_reviews'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String(500))
    rating = Column(Integer)