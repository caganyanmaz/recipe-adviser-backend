#!/bin/bash
source .venv/bin/activate
export FLASK_APP=src/api.py
export FLASK_ENV=development
flask run --eager-loading

