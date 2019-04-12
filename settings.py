import os

from peewee import *
from playhouse.db_url import connect

production_mode = os.environ.get('PRODUCTION_MODE', False)
url = os.environ.get('DATABASE_URL', 'postgres://postgres:postgres@localhost:5432/renpan')
db = connect(url)
