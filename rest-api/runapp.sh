#! /bin/bash

source venv/bin/activate

export DATABASE_URL="sqlite:///data.db"

python app.py
