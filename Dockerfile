FROM debian:buster
EXPOSE 7777
WORKDIR /app
COPY . .
RUN apt update && apt -y upgrade && apt -y install python3-venv gunicorn3 python3-pip && apt-get clean && pip3 install click dnspython email-validator Flask Flask-Reuploaded Flask-Uploads Flask-WTF idna itsdangerous Jinja2 MarkupSafe setuptools Werkzeug WTForms flask_login attrdict
CMD sed -re "s/superSicher123123/${ADMIN_PASSWORD}/g; s/a6d7f6bhas9d8f76asdf876af8364fgaiefzba3f7ae87zvgiawuzegfivawefz/${SECRET}/g" -i app/config.json && exec gunicorn3 -w 4 -b 0.0.0.0:7777 app:app
