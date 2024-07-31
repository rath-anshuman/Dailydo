#!/bin/bash

# Check Python version
python3 --version

# Install pip for Python 3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# Install required Python packages
pip3 install -r requirements.txt
python3 manage.py migrate
