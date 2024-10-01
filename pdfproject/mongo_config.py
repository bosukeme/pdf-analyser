import os
import sys
from mongoengine import connect

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
