from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import menu_items as model
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional

def create(db: Session, request):
    new_item = model.MenuItem(
        dishes = request.dishes,
        price = request.price
    )
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item

def read_all(db: Session, category: Optional[str] = None, name: Optional[str] = None):
    try:
        query = db.query(model.MenuItem)
        if category:
            query = query.filter(model.MenuItem.category.ilike(f"%{category}%"))
        if name:
            query = query.filter(model.MenuItem.name.ilike(f"%{name}%"))
        result = query.all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e.__dict__['orig']))
    return result