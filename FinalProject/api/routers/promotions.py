from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotions"
)


@router.post("/", response_model=schema.Promotion)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Promotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)