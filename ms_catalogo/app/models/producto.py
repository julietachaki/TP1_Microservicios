from dataclasses import dataclass

from app import db


@dataclass(init=False, repr=True, eq=True)

class Producto(db.Model):
    __tablename__ = 'products'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), unique=True, nullable=False)
    price: float = db.Column(db.Float ,nullable=False)
    activate: bool = db.Column(db.Boolean , unique=True, nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self