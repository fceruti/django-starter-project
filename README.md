# Django Starter Project

This repo is a starting point for a clasic django web service project running on docker that have the following services:

* **web:** Web server running django on port 8000.
* **worker:** Run async tasks with celery.
* **redis:** Used to store celery tasks.
* **webpack:** Automatically watches changes and recompiles static files for development. By default compiles `sass`.

The database should be configured in the host machine, as it is easier for development.

## Getting started
If you are starting a new project go ahead and clone this repo in a directory of your choosing

```bash
git clone git@github.com:fceruti/django-starter-project.git <new-directory>
cd <new-directory>
```

Create a database for your project (we'll call it django_db). Then you need to create a file called `.env` and write the environment variables you wish to use for development

```
ENV=dev
DEBUG=on
SECRET_KEY=123
DATABASE_URL=postgres://localhost:5432/django_db
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
USE_DEBUG_TOOLBAR=on
```

We now need to override `DATABASE_URL` environment variable inside of Docker to connect directly to you host machine. Create a file called `.env.docker` with the following content:

```
DATABASE_URL=postgres://<user>@host.docker.internal:5432/django_db
```

* **user** is the user in your host machine that has access to postgres in this case.

We are all set up for bringing everything live with

```
docker-compose up
```

Wait for everything to load, and you can visit `https://127.0.0.1:8000` and your new awesomely configured site will be there.



## Docker commands
Here are a few commands that may come in handy

Command | Description
--- | ---
`docker ps` | List all containers (-a to include stopped)
`docker logs --follow <container_id>` | Display the logs of a container
`docker exec -it <container_id> /bin/bash` | Attach into a running container
`docker run --rm <image_name> /bin/bash` | Run a docker container based on an image and get a prompt
`docker-compose run --rm web /bin/bash` | Same as before but for services defined in docker-compose.yml
`docker-compose run --rm web /bin/bash -c 'python manage.py migrate'` | Run a management command

## Old fashion install
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
These environment variables can be provided to configure your project.

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


### VSCode settings

Now a days my go-to editor is VSCode, so here's a template for `.vscode/settings.json`:

```
{
    // Interpreter
    "python.pythonPath": "<path>",
    "python.envFile": "${workspaceFolder}/.env",

    // Linting
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,

    // Search
    "search.exclude": {
        "**/.git": true,
        "**/.vscode": true,
        "**/node_modules": true,
        "**/static": true,
        "**/media": true,
        "**/logs": true,
        "**/tmp": true,
        "**/locale": true,
    },
    "search.showLineNumbers": true,
}
```

To fill the pythonPath run `pipenv --py` after initializing the directory's virtual environment.
