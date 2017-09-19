# REST api for products

The goal of this API is to store and retrieve information about products in an embedded database. This information os going to be consumed by a frontend application, allowing hypothetical users store and retrieve information about products, sub-products, and also image URLs attached to those products.

This API was built using Python 3.6, the Flask Framework, Flask-RESTful, SQLAlchemy and SQLite database. I'm using the file storage in SQLite, despite the recommendation in the assignment, because the memory storage in SQLite only persists for the current connection, and all data is lost as soon as the connection is closed.

To setup the project:

```
$ cd rest-api
$ virtualenv -p `which python3` venv
$ pip install -r requirements.txt
```

To run the tests:
```
$ ./runtests.sh
```

To run the API:
```
$ ./runapp.sh
```
The application will listen in the localhost (127.0.0.1) on port 5000

---

Below are some sample calls to the API:

Post a product:
```
curl -X POST \
  http://127.0.0.1:5000/v1/product \
  -H 'content-type: application/json' \
  -d '{
	"name": "Mesa "
	"price": 200.00
	"parent_id": null
}'
```

Post a subproduct:
```
curl -X POST \
  http://127.0.0.1:5000/v1/product \
  -H 'content-type: application/json' \
  -d '{
	"name": "Cadeira"
	"price": 100.00
	"parent_id": 1
}'
```

Post an image:
```
curl -X POST \
  http://127.0.0.1:5000/v1/image \
  -H 'content-type: application/json' \
  -d '{
	"type": "JPG",
	"url": "https://i2.zst.com.br/thumbs/49/21/39/181911324.jpg",
	"product_id": 1
}'
```

- Get all products excluding relationships (child products, images):
```
curl -X GET \
  http://127.0.0.1:5000/v1/product-simple \
  -H 'content-type: application/json' \
```

- Get all products including specified relationships (child product and/or images):
```
curl -X GET \
  http://127.0.0.1:5000/v1/product \
  -H 'content-type: application/json' \
```

- Same as a) using specific product identity
```
curl -X GET \
  http://127.0.0.1:5000/v1/product-simple/1 \
  -H 'content-type: application/json' \
```

- Same as b) using specific product identity:
```
curl -X GET \
  http://127.0.0.1:5000/v1/product/1 \
  -H 'content-type: application/json' \
```

- Get set of child products for specific product:
```
curl -X GET \
  http://127.0.0.1:5000/v1/product/1/children \
  -H 'content-type: application/json' \
```

- Get set of images for specific product:
```
curl -X GET \
  http://127.0.0.1:5000/v1/product/1/images \
  -H 'content-type: application/json' \

```
