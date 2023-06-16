# Dockerfile with Multi-stage-build using statements
# - each statement begins a new stage of the build
# - stage 1 builds dependency wheels
# - stage 2 runs the application
# - create .dockerignore file in root folder
# - list files to ignore while building images

# set python version, from docker hub registry
# bullseye image https://hub.docker.com/_/python
ARG PYTHON_VERSION=3.11.2-bullseye

# set base image to build docker image on
FROM python:${PYTHON_VERSION} as python

# Stage 1 - build dependecy wheels
# set image source, environment as development
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=development

# update pypi, install packages with no extra recommended packages
# build essential ensures install of essential tools
# lipbq is required dev files for postgres and psycopg2
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

# copy requirements folder to container root directory 
COPY ./requirements .

# create wheels for python dependency & sub dependency 
# from packages listed in development.txt
RUN pip wheel --wheel-dir /usr/src/app/wheels \
  -r ${BUILD_ENVIRONMENT}.txt


# Stage 2 - run the application
# set image source, environment as development
FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=development

# set container home directory
ARG APP_HOME=/app

# set env vars, skip .pyc files in modules
ENV PYTHONDONTWRITEBYTECODE 1

# set env vars, ensure output not buffered
ENV PYTHONUNBUFFERED 1

# set env vars, build env as development
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

# set working dir as container home dir
WORKDIR ${APP_HOME}

# install latest packages with no extra recommended packages
# gettext is tool for internalization & localization
# get purge cleans ununecessary files, or packages not needed
RUN apt-get update && apt-get install --no-install-recommends -y \
  libpq-dev \
  gettext \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# copy wheels from build stage above to container wheels
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# install dependency, disable cache files, no search pypi for packages
# find & intsall all packages in wheels dir created above, not from pypi
# remove the wheels dir after install of packages
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

# copy from entrypoint file to container entrypoint
# entrypoint ensures connect to db before spinning APi
COPY ./docker/development/django/entrypoint /entrypoint

# set entrypoint file has unique style line endings, not windows style
RUN sed -i 's/\r$//g' /entrypoint

# set entrypoint as script program in docker image
RUN chmod +x /entrypoint

# set models migrated, collect static files, run server
COPY ./docker/development/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# COPY ./docker/development/django/celery/worker/start /start-celeryworker
# RUN sed -i 's/\r$//g' /start-celeryworker
# RUN chmod +x /start-celeryworker

# COPY ./docker/development/django/celery/flower/start /start-flower
# RUN sed -i 's/\r$//g' /start-flower
# RUN chmod +x /start-flower

# copy code from project root to container home directory
COPY . ${APP_HOME}

# set to run when starting container from build image
ENTRYPOINT [ "/entrypoint" ]