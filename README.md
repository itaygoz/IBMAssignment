# IBMAssignment

A web application that manages logins and allows users to edit their data

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes. 
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python
local mysql db
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be:


Set up python env
```
You have to install the virtualEnv that attached to your mail,
or pip install the following libs to the project interpreter:

Click	7.0	
Flask	1.0.2	1.0.2
Flask-MySQL	1.4.0	1.4.0
Flask-SQLAlchemy	2.3.2	2.3.2
Jinja2	2.10	2.10
MarkupSafe	1.1.1	1.1.1
PyMySQL	0.9.3	0.9.3
SQLAlchemy	1.3.0	1.3.0b3
Werkzeug	0.14.1	0.14.1
itsdangerous	1.1.0	1.1.0
pip	9.0.1	19.0.3
setuptools	28.8.0	40.8.0
```

Set up mysql
```
In order to set up the the mysql db you need to configure a db in localhost/test under username: 'root' without a password.
You can also configure the db as you with and change the db settings in the code.
Anywhere you see "engine = create_engine('mysql+pymysql://root:''@localhost/test', echo=True)" you have to change it to your db settings.
The templte is 'mysql+pymysql://{username}:'{password}'@localhost/test'

```

Set up dummy data
```
Run the dummy.py file before the app

admin user is:
username: admin
password: password

regular user is:
username: python
password: python
```


## Deployment

In order to deploy the system on a live system you should run app.py file than access http://localhost:4000 in you browser.

## Built With

* [python](https://www.python.org/) - The framework used
* [Flask](http://flask.pocoo.org/) - The web framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - The MySQL management tool
* [phpMyAdmin](https://www.phpmyadmin.net/) - handle MySQL
* [jinja](http://jinja.pocoo.org/) - Python template tool

## Authors

* **Itay Goz** - *Initial work* 


