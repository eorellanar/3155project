from ..models import orders as model
from fastapi import APIRouter, Depends, FastAPI, status, Response, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import date
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db


router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Order])
def read_all(
    db: Session = Depends(get_db),
    start_date: date = Query(None),
    end_date: date = Query(None)
):
    return controller.read_all(db=db, start_date=start_date, end_date=end_date)

@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

@router.patch("/status/{tracking_number}")
def update_order_status(tracking_number: str, new_status: str, db: Session = Depends(get_db)):
    return controller.update_status_by_tracking(db, tracking_number, new_status)

@router.get("/track/{tracking_number}")
def track_order(tracking_number: str, db: Session = Depends(get_db)):
    order = db.query(model.Order).filter(model.Order.tracking_number == tracking_number).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {
        "tracking_number": order.tracking_number,
        "status": order.status,
        "customer_name": order.customer_name
    }