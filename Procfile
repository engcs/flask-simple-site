web: gunicorn app:app

heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python

heroku config:set PYTHON_RUNTIME_VERSION=3.10.4

heroku config:set POETRY_VERSION=1.1.13