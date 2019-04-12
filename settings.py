import os

import peewee

url = os.environ['DATABASE_URL']
db = peewee.playhouse.db_url.connect(url)
