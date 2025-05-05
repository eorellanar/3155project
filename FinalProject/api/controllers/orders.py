from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional
from datetime import date
from ..models import promotions as promo_model
import uuid

def create(db: Session, request):
    discount_applied = 0

    if request.promo_code:
        promo = db.query(promo_model.Promotion).filter(
            promo_model.Promotion.code == request.promo_code
        ).first()

        if not promo:
            raise HTTPException(status_code=400, detail="Invalid promo code")
        if promo.expiration_date and promo.expiration_date < date.today():
            raise HTTPException(status_code=400, detail="Promo code has expired")

        discount_applied = promo.discount_amount

    tracking_number = str(uuid.uuid4())[:8]

    new_item = model.Order(
        tracking_number=tracking_number,
        order_status="pending",
        total_price=request.total_price,
        delivery_type=request.delivery_type,
        promo_code=request.promo_code,
        discount=discount_applied
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=400, detail=error)

    return new_item


def read_all(db: Session, start_date: Optional[date] = None, end_date: Optional[date] = None):
    try:
        query = db.query(model.Order)
        if start_date:
            query = query.filter(model.Order.order_date >= start_date)
        if end_date:
            query = query.filter(model.Order.order_date <= end_date)
        result = query.all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update_status_by_tracking(db: Session, tracking_number: str, new_status: str):
    try:
        order = db.query(model.Order).filter(model.Order.tracking_number == tracking_number).first()
        if not order:
            raise HTTPException(status_code=404, detail="Tracking number not found")

        order.order_status = new_status
        db.commit()
        db.refresh(order)
        return order
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=400, detail=error)