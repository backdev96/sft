FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

# Install the necessary packages
RUN apt-get update && \
    apt-get install -y \
      locales apt-utils

# Generate locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen

# Set envs that won't change much
ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US:en"
ENV LC_ALL="en_US.UTF-8"

# Upgrade pip to the latest version
RUN python -m pip install -U --force-reinstall pip

VOLUME /app/src
WORKDIR /app/src

EXPOSE 8000
ENV DB_USER=np-api
ENV DB_PASSWORD=np-api-password
ENV DB_NAME=projects
ENV DB_HOST=database
ENV DB_PORT=5432
ENV STATIC_FILES=/app/static
ENV MEDIA_ROOT=/var/www/app/media
VOLUME /var/www/app/media

COPY requirements.txt /app/requirements.txt
COPY runserver.sh /app/runserver.sh
RUN chmod +x /app/runserver.sh
RUN pip3 install -r /app/requirements.txt
CMD python manage.py runserver
