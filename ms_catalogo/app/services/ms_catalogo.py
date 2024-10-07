
from app import db
from models.producto import Producto


class Calatogo:

    def find(self, id: int) -> Producto:
        if id is None or id == 0:
            return None
        try:
            Producto.activate = True
            return db.session.query(Producto).filter(Producto.id == id).one()
        
        except:
            return None
    