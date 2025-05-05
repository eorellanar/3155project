from pydantic import BaseModel
from typing import Optional

class RatingReviewBase(BaseModel):
    review_text: str
    rating: int

class RatingReviewCreate(RatingReviewBase):
    pass

class RatingReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    rating: Optional[int] = None

class RatingReview(RatingReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True