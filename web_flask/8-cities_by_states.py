#!/usr/bin/python3

"""A script that starts a Flask web application"""

from flask import Flask, render_template
from models import *
from models import storage

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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_integer_route(n):
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


@app.teardown_appcontext
def teardown_database(execption):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list_route():
    all_states_list = sorted(list(storage.all("State").values()),
                             key=lambda x: x.name)
    return render_template('7-states_list.html', all_state_list=all_state_list)


@app.route('/cities_by_states')
def html_fetch_cities_by_states():
    state_objs = [s for s in storage.all("State").values()]
    return render_template('8-cities_by_states.html',
                           state_objs=state_objs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
