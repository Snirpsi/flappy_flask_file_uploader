#! /bin/bash
. venv/bin/activate
export FLASK_APP=app/__init__.py
export FLASK_ENV=development
export CONF_FIELD=videogruss
flask run --host=0.0.0.0 --port=8000
