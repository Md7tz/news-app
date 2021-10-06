# news-app

A Blog app built with Django web framework styled with Bootstrap with Authentication, Authorization and CRUD features
check production build example at [mystic-news](https://mystic-news.herokuapp.com/)

> Enhanced Blog Django starter project.

## 🚀 Features

- Django 3.1 & Python 3.8
- Install via [Pip](https://pypi.org/project/pip/), [Pipenv](https://pypi.org/project/pipenv/)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v4](https://github.com/twbs/bootstrap)
- Forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
- Auth


## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
  * [Pipenv](#pipenv)
* [Setup](#setup)
* [Support](#support)
* [License](#license)

----

## 📖 Installation
news-app can be installed via Pip or Pipenv depending upon your setup. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Md7tz/news-app.git
$ cd news-app
```

### Pip

```
$ python3 -m venv news-app
$ source news-app/bin/activate
(news-app) $ pip install -r requirements.txt
(news-app) $ python manage.py migrate
(news-app) $ python manage.py createsuperuser
(news-app) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### Pipenv

```
$ pipenv install
$ pipenv shell
(news-app) $ python manage.py migrate
(news-app) $ python manage.py createsuperuser
(news-app) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

## Setup

```
# Run Migrations
(news-app) $ python manage.py migrate

# Create a Superuser
(news-app) $ python manage.py createsuperuser

# Confirm everything is working:
(news-app) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

----

## ⭐️ Support

Give a ⭐️  if this project helped you!

## License

[The MIT License](LICENSE)
