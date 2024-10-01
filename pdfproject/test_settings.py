import sys
import os
from mongoengine import connect


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

connection_uri = os.environ.get("MONGO_URI")

if 'test' in sys.argv:
    connect(
        db="test_database",
        host=connection_uri,
        ssl=True,
        retryWrites=True,
    )
else:
    connect(
        db=os.environ.get('DBNAME'),
        host=connection_uri,
        ssl=True,
        retryWrites=True,
    )
