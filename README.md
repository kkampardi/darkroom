# Django API with Django Rest Framework and AngularJS


## Setup

TODO: Add more setup options

### Manual

You're encouraged to setup a `virtualenv` to work in prior to configuring the dependencies.

    $ virtualenv -p /usr/bin/python3 venv

    Activate the virtual env

    $ source venv bin activate


1. Install Python Requirements

        pip install -r requirements.txt
        python setup.py develop


5. Setup the Database

        make create_database; make make_fixtures

6. Run the Server

        ./manage.py runserver
