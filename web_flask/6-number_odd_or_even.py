#!/usr/bin/python3

"""A script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_number_route(n):
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_even_integer_route(n):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, even_or_odd='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, even_or_odd='odd')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
