# Flappy Flask File Uploader

Flappy Flask application to upload videos or images to a web server. Users can describe the photo and add a date.

## Features!

* File upload
* Users can upload pictures
* It does not need a database
* Files get stored in the files ystem
* Administrators can view all pictures on one page with the user inserted data

## Dependencies

* The server must run on Linux
* Python3

**pip packages (tested)**

* autopep8 1.5.5
* click 7.1.2
* dnspython 2.1.0
* email-validator 1.1.2
* Flask 1.1.2
* Flask-Login 0.5.0
* Flask-Reuploaded 0.4.0
* Flask-Uploads 0.2.1
* Flask-WTF 0.14.3
* idna 3.1
* itsdangerous 1.1.0
* Jinja2 2.11.2
* MarkupSafe 1.1.1
* pip 20.0.2
* pkg-resources 0.0.0
* pycodestyle 2.6.0
* setuptools 44.0.0
* toml 0.10.2
* Werkzeug 0.16.0
* WTForms 2.3.3

Bootstrap is used with filestyle.

## Installation

For debugging on local host

* install python 3
* go into a new project folder
* execute the "setupDev.sh" script to create a virtual environment and install the dependencies

```
$ sudo apt-get install python3
$ cd nameOfProjectFolder
$ ./setupDev.sh
```

To start the webServer

```
$ cd nameOfProjectFolder
$ ./start.sh
```

To deploy the application on apache2 follow this guide: [<https://www.codementor.io/@abhishake/minimal-apache-configuration-for-deploying-a-flask-app-ubuntu-18-04-phu50a7ft>]

Otherwise, read the documentation. [<https://flask.palletsprojects.com/en/1.1.x/deploying/>]

You can use the "pipi.sh" script to install the pip dependencies,

**Important, before you deploy!** change the SECRET_KEY and ADMIN_PASSWORD in the **init.py**

```
app.config['SECRET_KEY'] = 'xaruoeibvlu2ioabelrziuaze2341rlbauzsrkuib14613422zakevr1'
app.config['ADMIN_PASSWORD'] = "superPassword!!!" #change this!
```

## Todos

* [ ] Fix Date Field
* [ ] Fix color of file upload
* [ ] Change CSS Theme
* [ ] move "database" location

