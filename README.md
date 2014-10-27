openrave-django
===============

Prerequisites
-----------
* docker
  * ```curl -sSL https://get.docker.com/ | sh```
* fig
  * ```curl -L https://github.com/docker/fig/releases/download/1.0.0/fig-`uname -s`-`uname -m` > /usr/local/bin/fig; chmod +x /usr/local/bin/fig```

Setup
-----

```
git clone https://github.com/ziyan/openrave-django.git
cd openrave-django/production
fig up -d
fig run django python manage.py createsuperuser
```

Point your browser to http://localhost/ to see the website. You need to login using the credentials you've created in the last step.

Once you are done, you can run ```fig kill; fig rm --force``` to clean up.

API
---

#### List existing robots ```GET /api/robots```
```curl -u username:password http://localhost/api/robots```

#### Get details about a robot ```GET /api/robots/:id```
```curl -u username:password http://localhost/api/robots/1```

#### Upload a new robot ```POST /api/robots```
```curl -u username:password -X POST -H 'Content-Type: application/zip' --data-binary @/path/to/robot.zae http://localhost/api/robots```

**NOTE:** For files ending in ```.xml```, you need to provide ```application/xml``` as the content type. For files ending in ```.zae```, you need ```application/zip```. These are the only two types of files supported.

#### Update an existing robot ```PUT /api/robots/:id```
```curl -u username:password -X PUT -H 'Content-Type: application/zip' --data-binary @/path/to/robot.zae http://localhost/api/robots/1```

#### Delete a robot ```DELETE /api/robots/:id```
```curl -u username:password -X DELETE http://localhost/api/robots/1```

Test
----

All APIs are tested. The easiest way to run test:

```
fig run django python manage.py test
```

Misc
----

You can create API key to use with the API endpoints. This way, you don't have to leak your username and password in the basic auth. You can use the Django admin interface to add API keys. http://localhost/admin/user/key/

Once a key is added, you can use it as your username in the basic auth. For example:

```
curl -u mllsh7GZyloNdsEcpHSFdIeHf87SbSYNT4w02cV3NjQxEr6HZvTNNga5OZ7OjQ4k: http://localhost/api/robots
```

