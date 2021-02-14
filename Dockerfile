FROM debian:buster
EXPOSE 7777
WORKDIR /app
COPY . .
RUN apt update
RUN apt -y upgrade
RUN apt -y install python3-venv gunicorn3 python3-pip
RUN pip3 install click dnspython email-validator Flask Flask-Reuploaded Flask-Uploads Flask-WTF idna itsdangerous Jinja2 MarkupSafe setuptools Werkzeug WTForms flask_login
CMD gunicorn3 -w 4 -b 0.0.0.0:7777 app:app
