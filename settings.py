import os

from peewee import *
from playhouse.db_url import connect

production_mode = bool(os.environ.get('PRODUCTION_MODE', False))
db = connect(os.environ.get('DATABASE_URL', 'postgres://postgres:postgres@localhost:5432/renpan'))
