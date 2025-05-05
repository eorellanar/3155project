from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import order_details as model
from ..schemas import order_details as schema
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request: schema.OrderDetailCreate):
    new_item = model.OrderDetail(
        order_id=request.order_id,
        sandwich_id=request.sandwich_id,
        amount=request.amount
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return new_item

def read_all(db: Session):
    try:
        return db.query(model.OrderDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

# Adjusted read_one - Jordon
def read_one(db: Session, item_id: int):
    item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderDetail not found")
    return item

def delete(db: Session, item_id: int):
    item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OrderDetail not found")
    try:
        db.delete(item)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return {"message": "OrderDetail deleted"}
