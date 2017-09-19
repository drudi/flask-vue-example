from flask_restful import Resource, reqparse
from models.product import ProductModel

parser = reqparse.RequestParser()
parser.add_argument('name',
    type=str,
    required=True,
    help='This field must hold the name of the product and cannot be blank'
)
parser.add_argument('description',
    type=str,
    required=True,
    help='This field must hold the description of the product and cannot be blank'
)
parser.add_argument('parent_id',
    type=int,
    required=False,
    help='If this field isn\'t provided, the product will be a parent product'
)
parser.add_argument('price',
    type=float,
    required=True,
    help='This field is required. Every product needs a price.'
)


class Product(Resource):

    def get(self, _id):
        product = ProductModel.find_by_id(_id)

        if not product:
            return {'message': 'Product not found'}, 404

        return product.json_with_children()


    def delete(self, _id):
        product = ProductModel.find_by_id(_id)

        status = 404
        message = 'Product not found.'
        if product:
            status = 200
            message = 'Product deleted'
            product.delete()

        return {'message': message}, status

    def put(self, _id):
        data = parser.parse_args()

        product = ProductModel.find_by_id(_id)

        status = 200
        if product:
            product.name = data['name']
            product.description = data['description']
            product.price = data['price']
        else:
            product = ProductModel(
                data['name'],
                data['description'],
                data['price'],
                data['parent_id']
            )
            status = 201

        product.save()

        return product.json(), status

class ProductList(Resource):

    def get(self):
        return {'products': [x.json_with_children() for x in ProductModel.find_all_parents()]}

    def post(self):
        data = parser.parse_args()

        product = ProductModel(data['name'], data['description'], data['price'], data['parent_id'])

        try:
            product.save()
        except Exception as e:
            return {'message': 'An error occurred inserting into db: {}'.format(e)}, 500

        return product.json(), 201


class ProductSimple(Resource):

    def get(self, _id):
        return ProductModel.find_by_id(_id).json()



class ProductSimpleList(Resource):

    def get(self):
        return {'products': [x.json() for x in ProductModel.query.all()]}


class ProductChildren(Resource):

    def get(self, _id):
        product = ProductModel.find_by_id(_id)

        if not product:
            return {'message': 'Product not found.'}, 404

        products = product.get_children()
        if len(products) == 0:
            return {'message': 'No children found.'}, 404

        return {'products': [x.json() for x in products]}

class ProductImages(Resource):

    def get(self, _id):
        product = ProductModel.find_by_id(_id)

        if not product:
            return {'message': 'Product not found.'}, 404

        images = product.get_images()
        if len(images) == 0:
            return {'message': 'No images found.'}, 404

        return {'images': [x.json() for x in images]}
