openrave-django
===============

Prerequisites
-----------
* docker
** ```curl -sSL https://get.docker.com/ | sh```
* fig
** ```curl -L https://github.com/docker/fig/releases/download/1.0.0/fig-`uname -s`-`uname -m` > /usr/local/bin/fig; chmod +x /usr/local/bin/fig```

Setup
-----

```
git clone https://github.com/ziyan/openrave-django.git
cd openrave-django/production
fig up -d
fig run django python manage.py createsuperuser
```

Point your browser to http://localhost/ to see the website. You need to login using the credentials you've created in the last step

