from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.product_model import Product
from app.schemas.product_schema import ProductOut
from typing import List

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ProductOut])
def get_products_by_module(module: str = Query(...), db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.module.ilike(module)).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products
