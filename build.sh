#!/bin/bash

pip install virtualenv

virtualenv .env --no-site-packages -p python3.5
./.env/bin/pip install -r requirements.txt
source ./.env/bin/activate