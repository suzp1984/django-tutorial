# django-tutorial
a collection of django projects for study purpose

# How to install

The recommanded way to run django projects is to use virtual env.

## Install Virtualenv and Django

```sh
sudo pip install virtualenv
virtualenv djangoenv
cd djangoenv
source bin/activate
pip install django==1.7.2
```

## prepare the DB

```sh
python manage.py makemigrations
python manage.py migrate
```

## run the server

```sh
python manage.py runserver
```
