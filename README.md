# Django Starter Project

Starting point for all django projects.

### Running the project
Make sure you have pipenv installed in your virtual environment. You have the following development commands at your disposal:

Command | Shortcut for
--- | ---
`pipenv run server` | `pipenv run python manage.py runserver_plus`
`pipenv run tests` | `pipenv run pytest`
`pipenv run shell` | `pipenv run python manage.py shell_plus`
`pipenv run makemigrations` | `pipenv run python manage.py makemigrations`
`pipenv run migrate` | `pipenv run python manage.py migrate`

To compile your static files, you need to have npm installed and all the local dependencies (run `npm install`). Then can execute the following commands
Command | Shortcut for
--- | ---
`npm run dev` | `webpack --mode development --watch`
`npm run build` | `webpack --mode production`

### Environment variables
These environment variables must be provided to properly run the project in each environment they run on.

#### Django
Name | Values | Default | Description
--- | --- | --- | ---
ENV | dev, test, qa, prod | prod | Indicates in which environmet the project is running on
DEBUG | on, off | off | Run server in debug mode
LANGUAGE_CODE | Language Identifier (RFC 3066) | en-US | [List of language codes](http://www.i18nguy.com/unicode/language-identifiers.html)
TIME_ZONE | Record of IANA time zone database | America/Santiago | [List of timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
USE_I18N | on, off | on | Enable translation system
USE_L10N | on, off | on | Enable localized formatting
USE_TZ | on, off | on | Enable timezone aware dates in
DEFAULT_FROM_EMAIL | E-mail addresss | -- | Email address from which transactional emails will be sent from
EMAIL_BACKEND | Path to backend | django.core.mail.backends.smtp.EmailBackend | The backend to use for sending emails. [List of backends](https://docs.djangoproject.com/en/2.2/topics/email/#email-backends)
SECRET_KEY | Random string | -- | Used to provide cryptographic signing
ALLOWED_HOSTS | List of domains | -- | Represents the host/domain names that this site can serve.
DJANGO_DATABASE_URL | Database url | -- | Describes the database connection with [a url strucure](https://github.com/joke2k/django-environ).
LOGIN_URL | Url | /login/ | Url to redirect users when login is needed
LOGIN_REDIRECT_URL | Url | / | Url to redirect users after login in
STATIC_URL | Url | /static/ | Url from which static files are served
MEDIA_URL | Url | /media/ | Url from which media files are served

#### Django debug toolbar
Name | Values | Default | Description
--- | --- | --- | ---
USE_DEBUG_TOOLBAR | on, off | off | Enables django debug toolbar
