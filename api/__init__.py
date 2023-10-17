import sqlite3

import flask
from flask import request   # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify   # übersetzt python-dicts in json
import os
from . import db
from datetime import datetime

from . import api


def create_app() -> flask.Flask:
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message
    app.config['DATABASE'] = os.path.join(app.instance_path, '../api/db.sqlite')

    db.init_app(app)

    return app


app = create_app()


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"

@app.route('/api/openTables', methods=['GET'])
def freeTables():
    start_val = request.args.get('from', None)
    end_val = request.args.get('to', None)

    if any([val is None for val in [start_val, end_val]]):
        return {
            'success': False,
            'error': 'No from or to data provided'
        }, 400

    try:
        start = datetime.fromisoformat(start_val)
        end = datetime.fromisoformat(end_val)
    except:
        return {
            'status': False,
            'error': 'Unable to parse from or end data'
        }, 422

    open_tables = api.get_open_tables(start, end)

    return {
        'success': True,
        'data': open_tables
    }


if __name__ == '__main__':
    app.run()
