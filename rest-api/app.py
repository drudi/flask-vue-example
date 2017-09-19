import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.product import *
from resources.image import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', default='sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecret'
api = Api(app)


# Items a) and c) from the assignment. Only GET
api.add_resource(ProductSimple, '/v1/product-simple/<int:_id>')
api.add_resource(ProductSimpleList, '/v1/product-simple')

# Items b) and d) from the assignment
# GET, DELETE and PUT
api.add_resource(Product, '/v1/product/<int:_id>')
# GET and POST
api.add_resource(ProductList, '/v1/product')

# GET and PUT
api.add_resource(ImageSimpleList, '/v1/image')
# GET, DELETE and PUT
api.add_resource(ImageSimple, '/v1/image/<int:_id>')

# Item e)
api.add_resource(ProductChildren, '/v1/product/<int:_id>/children')

# Item f)
api.add_resource(ProductImages, '/v1/product/<int:_id>/images')



if __name__ == '__main__':
    from db import db
    db.init_app(app)

    # Create db tables if they don't exist
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(debug=True)
