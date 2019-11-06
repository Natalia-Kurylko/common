import os
import uuid

from flask import Blueprint, request, render_template, session
from werkzeug.utils import secure_filename
from products.forms import AddProductForm
from products.product_list import product_list

products = Blueprint('products', __name__, template_folder='template_p', static_folder='static_p')


@products.route('/products', methods=['GET'])
def get_all_products():
    if request.method == 'GET':
        if request.args:
            try:
                for k, v in request.args.items():
                    if k == 'price' or k == 'id':
                        return render_template("all_products.html",
                                               products=[i for i in product_list if i[k] == int(v)])
            except KeyError:
                return render_template('404.html')

        return render_template("all_products.html", products=product_list)


@products.route('/products/<int:id>')
def get_product(id):
    try:
        all_data = product_list
        data = [p for p in all_data if p.get('id') == id]
        session[data[0]['name']] = True
        return render_template('products.html', data=data[0])
    except (IndexError, KeyError):
        os.abort(404)


@products.route('/<product_name>/<product_description>/<product_price>/<product_img>')
def get_the_product(product_name, product_description, product_price, product_img):
    session[product_name] = True
    return render_template("products.html", product_name=product_name, product_description=product_description,
                           product_price=product_price, product_img=product_img)


@products.route('/add_product', methods=['GET', 'POST'])
def add_products():
    form = AddProductForm()
    if request.method == 'POST':
        data = {"id": str(uuid.uuid4()), "name": request.form['name'], "description": request.form['description'],
                "img_name": secure_filename(request.files['image'].filename), "price": request.form['price']}
        product_list.append(data)
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join('products/static_p', secure_filename(filename)))

    return render_template('add_products.html', form=form)
