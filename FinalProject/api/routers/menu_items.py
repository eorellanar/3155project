from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from ..models import menu_items
from ..schemas import menu_items as menu_schema
from ..dependencies.database import get_db
from typing import Optional

router = APIRouter(prefix="/menu_items", tags=["menu_items"])


def get_all_menu_items(
        db: Session = Depends(get_db),
        category: Optional[str] = Query(None),
        name: Optional[str] = Query(None)
):
    query = db.query(menu_items.MenuItem)

    if category:
        query = query.filter(menu_items.MenuItem.category.ilike(f"%{category}%"))
    if name:
        query = query.filter(menu_items.MenuItem.name.ilike(f"%{name}%"))

    return query.all()

@router.get("/{item_id}")
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(menu_items.MenuItem).filter(menu_items.MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

@router.post("/")
def create_menu_item(data: menu_schema.MenuItemCreate, db: Session = Depends(get_db)):
    new_item = menu_items.MenuItem(**data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.put("/{item_id}")
def update_menu_item(item_id: int, data: menu_schema.MenuItemCreate, db: Session = Depends(get_db)):
    item = db.query(menu_items.MenuItem).filter(menu_items.MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    for field, value in data.dict().items():
        setattr(item, field, value)
    db.commit()
    return item

@router.delete("/{item_id}")
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(menu_items.MenuItem).filter(menu_items.MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted"}