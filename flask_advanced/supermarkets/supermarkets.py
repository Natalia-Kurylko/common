import os
import uuid

from flask import Blueprint, request, render_template, session
from werkzeug.utils import secure_filename
from supermarkets.form import AddSupermarketForm
from supermarkets.supermarkets_list import  supermarkets_list

supermarkets = Blueprint('supermarkets', __name__, template_folder='template_s',static_folder='static_s')


@supermarkets.route('/supermarkets', methods=['GET'])
def get_all_supermarkets():
    if request.method == 'GET':
        if request.args:
            try:
                for k, v in request.args.items():
                    if k == 'id':
                        return render_template("all_products.html",
                                               supermarkets=[i for i in supermarkets_list if i[k] == int(v)])
            except KeyError:
                return render_template('404.html')

        return render_template("all_supermarkets.html", supermarkets=supermarkets_list)


@supermarkets.route('/supermarket/<int:id>')
def get_supermarket(id):
    try:
        all_data = supermarkets_list
        data = [s for s in all_data if s.get('id') == id]
        session[data[0]['name']] = True
        return render_template('supermarkets.html', data=data[0])
    except (IndexError,KeyError):
        os.abort(404)


@supermarkets.route('/<supermarket_name>/<supermarket_location>/<supermarket_img>')
def get_the_supermarket(supermarket_name, supermarket_location, supermarket_img):
    session[supermarket_name] = True
    return render_template("supermarkets.html", supermarket_name=supermarket_name, supermarket_location= supermarket_location,
                           supermarket_img=supermarket_img)


@supermarkets.route('/add_supermarket', methods=['GET','POST'])
def add_supermarket():
    form = AddSupermarketForm()
    if request.method == 'POST':
        data = {"id": str(uuid.uuid4()), "name": request.form['name'], "location": request.form['location'],
                "img_name": secure_filename(request.files['image'].filename)}
        supermarkets_list.append(data)
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join('supermarkets/static_s', secure_filename(filename)))

    return render_template('add_supermarkets.html', form=form)

