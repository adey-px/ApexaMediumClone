###########  Postgres Dockerfile ############

# Set base image for postgres, from docker hub registry
# postgres bulleye - https://hub.docker.com/_/postgres
FROM postgres:15-bullseye

# Copy maintenance folder from local project to docker
COPY ./docker/development/postgres/maintenance /usr/development/bin/maintenance

# Make its content scripts executable iniside container
RUN chmod +x /usr/development/bin/maintenance/*

# Move the folder content to new location, then delete it
RUN mv /usr/development/bin/maintenance/* /usr/local/bin \
  && rmdir /usr/development/bin/maintenance
  