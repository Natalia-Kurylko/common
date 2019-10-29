from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('home.html')


@app.route('/vegetables')
def vegetables_page():
    some_vegetables = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetable.html', list=some_vegetables)


@app.route('/fruits')
def fruits_page():
    some_fruits = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', list=some_fruits)


if __name__ == "__main__":
    app.run(debug=True)
