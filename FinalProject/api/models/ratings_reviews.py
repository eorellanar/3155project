from sqlalchemy import Column, Integer, String
from ..dependecies.database import Base

class RatingsReviews(Base):
    __tablename__ = 'ratings_reviews'
    review_text = Column(String(100))
    rating = Column(Integer)