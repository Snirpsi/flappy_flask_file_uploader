# Flappy Flask File Uploader

Flappy Flask application to upload videos or images to a web server. Users can describe the photo and add a date.

## Features!

* File upload
* Users can upload pictures
* It does not need a database
* Files get stored in the files ystem
* Administrators can view all pictures on one page with the user inserted data

## Dependencies

* The server has to run on Linux
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

Customize your instance of this application by editing the "config. json" file. You although can switch between different configurations by setting the environment variable "CONF_FIELD" to a value existing in your json File. 

**config.json**
```
{
    "default": {
      ...
    },
    "bilderupload": {
      ...
    }
}
    
```

**environment variable "CONF_FIELD"**
```
$export CONF_FIELD=default 
```
or 
```
$export CONF_FIELD=bilderupload 
```





To deploy the application on apache2 follow this guide: [<https://www.codementor.io/@abhishake/minimal-apache-configuration-for-deploying-a-flask-app-ubuntu-18-04-phu50a7ft>]

Otherwise, read the documentation. [<https://flask.palletsprojects.com/en/1.1.x/deploying/>]

You can use the "pipi.sh" script to install the pip dependencies.

**Important, before you deploy!** change the ```password``` and ```secret``` in **config.json**

```
        ...
        "password": "superSicher123123", <---change this
        "username": "admin",
        "secret": "a6d7f6bhas9d8f76asdf876af8364fgaiefzba3f7ae87zvgiawuzegfivawefz", <---change this
        ...
```

## Todos

* [ ] Fix Date Field
* [ ] Fix color of file upload
* [ ] Change CSS Theme
* [ ] move "database" location

