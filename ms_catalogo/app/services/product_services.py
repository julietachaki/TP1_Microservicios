from typing import List

from app import db
from app.models.producto import Producto
from app.repositories.product_repository import ProductRepository

repository = ProductRepository()
class ProductService:
    
    def save(self, producto: Producto) -> Producto:
        db.session.add(producto)
        db.session.commit()
        return producto
    

    