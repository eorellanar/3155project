from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import rating_reviews as controller
from ..schemas import rating_reviews as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Rating Reviews'],
    prefix="/ratingreviews"
)

@router.post("/", response_model=schema.RatingReview)
def create(request: schema.RatingReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.RatingReview])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)