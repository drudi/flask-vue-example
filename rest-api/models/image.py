from db import db

class ImageModel(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10))
    url = db.Column(db.String(1024))

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


    def __init__(self, _type, url, p_id):
        self.id = None
        self.type = _type
        self.url = url
        self.product_id = p_id

    def json(self):
        return {
            'id': self.id,
            'type': self.type,
            'url': self.url,
            'product_id': self.product_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_product(cls, product_id):
        return cls.query.filter_by(product_id=product_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
