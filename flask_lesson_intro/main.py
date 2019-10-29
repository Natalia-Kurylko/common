from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


def count_words(some_text):
    number = 0
    for _ in some_text.split():
        number += 1
    return number


@app.route('/')
@app.route('/home')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/clock')
def get_alarm_clock_page():
    some_text = get_data()[0]['text']
    name = get_data()[0]['title']
    number = count_words(some_text)
    return render_template("clock.html", some_text=some_text, name=name, number=number)


@app.route('/headphones')
def get_headphones_page():
    some_text = get_data()[1]['text']
    name = get_data()[1]['title']
    number = count_words(some_text)
    return render_template("headphones.html", some_text=some_text, name=name, number=number)


@app.route('/battery')
def get_battery_page():
    some_text = get_data()[5]['text']
    name = get_data()[5]['title']
    number = count_words(some_text)
    return render_template("battery.html", some_text=some_text, name=name, number=number)


@app.route('/calculator')
def get_calculator_page():
    some_text = get_data()[3]['text']
    name = get_data()[3]['title']
    number = count_words(some_text)
    return render_template("calculator.html", some_text=some_text, name=name, number=number)


@app.route('/coffeemaker')
def get_coffeemaker_page():
    some_text = get_data()[4]['text']
    name = get_data()[4]['title']
    number = count_words(some_text)
    return render_template("coffeemaker.html", some_text=some_text, name=name, number=number)


@app.route('/ipod')
def get_ipod_page():
    some_text = get_data()[2]['text']
    name = get_data()[2]['title']
    number = count_words(some_text)
    return render_template("ipod.html", some_text=some_text, name=name, number=number)


@app.route('/author')
def get_author_page():
    some_text = get_data()[6]['text']
    name = get_data()[6]['title']
    return render_template("author.html", some_text=some_text, name=name)

if __name__ == "__main__":
    app.run(debug=True)
