from mujin.settings import *

#DEBUG = False
#TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_ROOT, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True,
    }
}

