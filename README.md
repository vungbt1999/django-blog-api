# Getting Started
Python 3

Create virtualenv:

    $ python3 -m venv venv

Activate the virtualenv for your project:

    $ mac source ./venv/bin/activate
    $ win ./venv/Scripts/activate

Install project dependencies:

    $ pip install -r requirements/local.txt

Then simply apply the migrations:

    $ python3 manage.py migrate

Make migrate when create/update model in module:

    $ python3 manage.py makemigrations
    
You can now run the development server:

    $ python3 manage.py runserver

Create new module:

    $ python3 manage.py startapp <<module_name>>
