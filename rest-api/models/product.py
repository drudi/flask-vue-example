from db import db
from models.image import ImageModel

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    price = db.Column(db.Float(precision=2))

    images = db.relationship('ImageModel', lazy='dynamic')

    parent_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    parent = db.relationship('ProductModel')



    def __init__(self, name, description, price, parent_id):
        self.id = None
        self.name = name
        self.description = description
        self.price = price
        self.images = []
        self.parent_id = parent_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'images': [image.json() for image in self.images.all()],
            'parend_id': self.parent_id
        }

    def json_with_children(self):
        children = [x.json() for x in ProductModel.query.filter_by(parent_id=self.id)]
        parent = self.json()
        parent['subproducts'] = children
        return parent


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all_parents(cls):
        return cls.query.filter_by(parent_id=None)

    def get_children(self):
        return ProductModel.query.filter_by(parent_id=self.id).all()

    def get_images(self):
        return self.images.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
