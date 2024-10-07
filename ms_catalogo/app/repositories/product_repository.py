from typing import List, Type

from app import db
from app.models.producto import Producto


class ProductRepository:

    def save(self, producto: Producto ) -> Producto :
        db.session.add(producto)
        db.session.commit()
        return producto
    
