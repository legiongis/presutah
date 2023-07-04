# Preservation Utah - Map

This is the [Arches](https://archesproject.org) implementation used for Preservation Utah's [easement tracking program](https://map.reservationutah.org).

Arches version: 6.0.0

## Install

A local install looks like this.

```
# create virtual environment, install arches 6.0.0 from repo
python3 -m venv env && source ./env/bin/activate
git clone https://github.com/legiongis/arches && cd arches
git checkout stable/6.0.0
pip install -e .
cd ..

# clone this repo and install node_modules
git clone https://github.com/legiongis/presutah
cd presutah/presutah
yarn install
cd ..

# add database creds, elasticsearch settings, etc.
nano presutah/settings_local.py

# setup database and load package
python manage.py packages -o load_package -s pkg -db

# run the dev server
python manage.py runserver
```
