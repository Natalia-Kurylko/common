from flask import Flask, render_template
from products.products import products
from supermarkets.supermarkets import supermarkets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_super_secret_password'

app.register_blueprint(products, url_prefix='/products')
app.register_blueprint(supermarkets, url_prefix='/supermarkets')

app.config['SECRET_KEY'] = 'super_secret_password'

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def get_home_page():
    return render_template("home.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('/404.html')


if __name__ == "__main__":
    app.run(debug=True)
