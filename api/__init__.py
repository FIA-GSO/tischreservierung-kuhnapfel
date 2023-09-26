import flask
from flask import request   # wird benötigt, um die HTTP-Parameter abzufragen
from flask import jsonify   # übersetzt python-dicts in json
import os
from . import db


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
    database = db.get_db()
    cur = database.cursor()
    cur.execute('SELECT * FROM tische')
    tables = cur.fetchall()

    return [t for t in tables]


if __name__ == '__main__':
    app.run()
