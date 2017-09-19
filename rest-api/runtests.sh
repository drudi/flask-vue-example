#! /bin/bash

source venv/bin/activate

export DATABASE_URL="sqlite:///test_data.db"

python test_api.py
