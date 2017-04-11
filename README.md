# Darkroom image repository

A shareable repository of images written in python/Django.  

## Setup

TODO: Add more setup options

### Getting started

You're encouraged to setup a `virtualenv` to work in prior to configuring the dependencies.

    virtualenv -p /usr/bin/python3 venv

#### Activate the virtual env

    source venv/bin/activate

1. Install Python Requirements

       pip install -r requirements/base.txt

       python setup.py develop


2. Setup the Database

       make db_setup;

3. Run the Server

       ./manage.py runserver
