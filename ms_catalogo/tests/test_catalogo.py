import unittest

from app import create_app, db
from app.models.producto import Producto
from flask import current_app


class CatalogoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        #db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
            
    def test_catalogo(self):
        producto = Producto()
        producto.name = 'remera'
        producto.price = 12334
        producto.save()
        producto.find()
        self.assertEqual(producto.activate ,True)
        self.assertEqual(producto.name, 'remera')
        self.assertEqual(producto.price, 12334)
    def test_catalogo_fail(self):
        producto = Producto()
        producto.name = 'remera1'
        producto.price = 123343
        producto.find()
        self.assertEqual(producto.activate ,False)
        self.assertEqual(producto.name, 'remera1')
        self.assertEqual(producto.price, 123343)
if __name__ == "__main__":
    unittest.main()