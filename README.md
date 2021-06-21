# Requirement File

The Project named as rishprac1 and application is rk01
This project is about practicing with new challanges.

Requirements for this project are as follows:

Project is run in virtual env named venv.

- python3 -m venv venv
- source venv/bin/activate

Installed apps are

- asgiref==3.3.4
- crispy-bootstrap5==0.4
- Django==3.2.4
- django-crispy-forms==1.12.0
- django-phonenumber-field==5.2.0
- install==1.3.4
- psycopg2==2.9.1
- pytz==2021.1
- sqlparse==0.4.1

Refer documentation python documentation for working.

Quick referencing is as follows:

    INSTALLED_APPS = (
        ...
        "crispy_forms",
        "crispy_bootstrap5",
        ...
    )

    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

    CRISPY_TEMPLATE_PACK = "bootstrap5"

PSQL 13 is the DB I'm using

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': BASE_DIR / 'rishipalsingh',
            'USER' : 'rishipalsingh',
            'PASSWORD' : '',
            'HOST' : 'localhost',
            'PORT' : '5432',
        }
    }

Thank you for reading.
Rishipal