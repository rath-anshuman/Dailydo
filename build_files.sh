#!/bin/bash

# Ensure that pip is installed
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

# Install required Python packages
pip install -r requirements.txt

# Continue with your build steps
python manage.py migrate
