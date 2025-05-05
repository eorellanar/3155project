from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from ..models.orders import Order
from ..dependencies.database import get_db

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/revenue")
def get_revenue_for_date(target_date: date = Query(...), db: Session = Depends(get_db)):
    total = db.query(func.sum(Order.total_price)).filter(Order.date == target_date).scalar()
    return {"date": target_date, "total_revenue": total or 0.0}