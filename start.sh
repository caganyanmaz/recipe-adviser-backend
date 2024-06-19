#!/bin/bash
source .venv/bin/activate
export FLASK_APP=api/api.py
export FLASK_ENV=development
flask run

