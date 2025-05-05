from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import resource_management as controller
from ..schemas import resource_management as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Resource Management'],
    prefix="/resourcemanagement"
)


@router.post("/", response_model=schema.ResourceAmount)
def create(request: schema.ResourceAmountCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.ResourceAmount])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)