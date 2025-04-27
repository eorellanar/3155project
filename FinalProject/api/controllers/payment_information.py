from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import payment_information as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.PaymentInformation(
        card_number = request.card_number,
        payment_type = request.payment_type
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
        result = db.query(model.PaymentInformation).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result