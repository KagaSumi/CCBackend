from pathlib import Path

from flask import Flask, jsonify, render_template, request

from database import db
from models import Product, Order, ProductsOrder

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)


@app.route("/api/product/<string:name>", methods=["GET"])
def api_get_product(name):
    """Returns the user the product that belongs to the specified name.

    Args:
        name (str): Name of the product of the database

    Returns:
        Response : A response of the outcome of the get operation
    """
    product = db.session.get(Product, name.lower())
    if not product:
        return ("Product not found", 404)
    product_json = product.to_dict()
    return jsonify(product_json)


if __name__ == "__main__":
    app.run(debug=True)
