from flask_restful import Resource, reqparse
from models.image import ImageModel

parser = reqparse.RequestParser()
parser.add_argument('type',
    type=str,
    required=True,
    help='Type of the image is required (GIF, JPG, PNG, etc)'
)
parser.add_argument('url',
    type=str,
    required=True,
    help='Image URL is required.'
)
parser.add_argument('product_id',
    type=int,
    required=True,
    help='Every image must me associated with a product.'
)


class ImageSimpleList(Resource):

    def get(self):
        return {'images': [x.json() for x in ImageModel.query.all()]}

    def post(self):
        data = parser.parse_args()

        image = ImageModel(
            data['type'],
            data['url'],
            data['product_id']
        )

        try:
            image.save()
        except Exception as e:
            return {'message': 'An error occurred inserting into db: {}'.format(e)}, 500

        return image.json(), 201

class ImageSimple(Resource):

    def get(self, _id):
        image = ImageModel.find_by_id(_id)

        if not image:
            return {'message': 'Image not found.'}, 404

        return image.json()

    def delete(self, _id):
        image = ImageModel.find_by_id(_id)

        status = 404
        message = 'Image not found'
        if image:
            image.delete()
            status = 200
            message = 'Image deleted'

        return {'message': message}, status

    def put(self, _id):
        data = parser.parse_args()

        image = ImageModel.find_by_id(_id)

        status = 200
        if image:
            image.type = data['type']
            image.url = data['url']
        else:
            image = ImageModel(
                data['type'],
                data['url'],
                data['product_id']
            )
            status = 201

        image.save()

        return image.json(), status
