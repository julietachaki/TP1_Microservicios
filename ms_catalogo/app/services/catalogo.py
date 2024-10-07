
from app import db
from models.producto import Producto


class CalatogoService:

    def find(self):
        if self.id is None or self.id == 0:
            self.activate = False
            db.session.add(self)
            db.session.commit()
            return None

        try:
            producto = db.session.query(Producto).filter(Producto.id == self.id).one_or_none()
            if producto is not None:
                self.activate = True
            else:
                self.activate = False

            db.session.add(self)
            db.session.commit()
            return producto
        except Exception as e:
            self.activate = False
            db.session.add(self)
            db.session.commit()
            return None