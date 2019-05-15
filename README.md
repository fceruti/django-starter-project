# Django Starter Project

Starting point for all django projects.

The services provided are:

* **web** Web server running django on port 8000.
* **worker** Run async tasks with celery.
* **redis** Used to store celery tasks.
* **webpack** Automatically watched changes and recompiles static files for development.

The database should be configured in the host machine, as it is easier for development.

### Running the project
You have two ways of running the project, using Docker or calling everything yourself.

#### Docker

The first step is to create two environment files called `.env` and `.env.docker`

**.env**
```
ENV=dev
DEBUG=on
SECRET_KEY=123
TIMEZONE=America/Santiago
STATIC_URL=/static/
MEDIA_URL=/media/
DATABASE_URL=postgres://localhost:5432/django_db
DJANGO_SETTINGS_MODULE=conf.settings
DEFAULT_FROM_EMAIL=hello@fceruti.com
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
USE_DEBUG_TOOLBAR=on
```

**.env.docker**
```
DATABASE_URL=postgres://fceruti@host.docker.internal:5432/django_db
```
Docker containers needs to access database in your host machine, so it should have a different address as pytest for example that runs completely on you host machine. Make sure you create a database and change the DATABASE_URL in both files accordingly.

Now to run the project using Docker execute `docker-compose up` and everything will be set for you in your local machine.

```
docker exec -it <container_id> psql -U postgres -c "create database django_db"
```

Here are a few advanced commands that may come in handy

Command | Description
--- | ---
`docker ps` | List all containers (-a to include stopped)
`docker logs --follow <container_id>` | Display the logs of a container
`docker exec -it <container_id> /bin/bash` | Attach into a running container
`docker run --rm <image_name> /bin/bash` | Run a docker container based on an image and get a prompt
`docker-compose run --rm web /bin/bash` | Same as before but for services defined in docker-compose.yml
`docker-compose run --rm web /bin/bash -c 'python manage.py migrate'` | Run a management command

#### The old way
First of all, install pyenv so you can use the specified python version (check out .python-version). Then, run `pip install pipenv` to install it's pip's successor: pipenv. Then install dependencies by running `pipenv install`. You can now start developing.

These commands are at your disposal:

Command | Shortcut for
--- | ---
`pipenv run server` | `pipenv run python manage.py runserver_plus`
`pipenv run tests` | `pipenv run pytest`
`pipenv run celery` | `pipenv run python manage.py celery_autoreload`
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

#### Celery
Name | Values | Default | Description
--- | --- | --- | ---
CELERY_BROKER_URL | Database url | -- | A common value for development is to use redis://cache, but it's recommended for production to use RabbitMQ

#### Django debug toolbar
Name | Values | Default | Description
--- | --- | --- | ---
USE_DEBUG_TOOLBAR | on, off | off | Enables django debug toolbar
