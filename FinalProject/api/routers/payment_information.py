from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import payment_information as controller
from ..schemas import payment_information as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Payment Information'],
    prefix="/paymentinformation"
)


@router.post("/", response_model=schema.PaymentInformation)
def create(request: schema.PaymentInformationCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.PaymentInformation])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)