from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_item = model.ResourceAmount(
        resource1 = request.resource1,
        resource1Amount = request.resource1Amount,
        resource2 = request.resource2,
        resource2Amount = request.resource2Amount,
        resource3 = request.resource3,
        resource3Amount = request.resource3Amount,
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
        result = db.query(model.ResourceAmount).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result