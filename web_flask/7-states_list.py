#!/usr/bin/python3

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list_route():
    all_states_list = sorted(list(storage.all("State").values()),
                             key=lambda x: x.name)
    return render_template('7-states_list.html', all_state_list=all_state_list)


@app.teardown_appcontext
def teardown_database(execption):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
