FROM ziyan/openrave

RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y gettext && \
    rm -rf /var/lib/apt/lists/*

ADD requirements.txt /tmp/requirements.txt

RUN \
    cd /usr/src && \
    pip install -r /tmp/requirements.txt

ADD . /django

WORKDIR /django
CMD python manage.py compilemessages && \
    python manage.py collectstatic --noinput && \
    python manage.py syncdb --noinput && \
    gunicorn --config mujin/gunicorn.py mujin.wsgi

VOLUME ["/data"]
EXPOSE 8000

