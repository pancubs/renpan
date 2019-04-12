from settings import db
import peewee as sql

class Table(sql.Model):
	class Meta:
		database = db

class User(Table):
	name = sql.CharField()
	password = sql.CharField()
	verified = sql.BooleanField()

class Thing(Table):
	key = sql.CharField()

class Version(Table):
	revision = sql.IntegerField()
	thing_id = sql.ForeignKeyField(Thing, backref='versions')
	author_id = sql.ForeignKeyField(User, backref='versions')
	ip = sql.CharField() # should use sql.IPField()
	comment = sql.CharField()
	created = sql.TimestampField()

class Datum(Table):
	thing_id = sql.ForeignKeyField(Thing, backref='data')
	begin_revision = sql.IntegerField()
	end_revision = sql.IntegerField()
	key = sql.CharField()
	value = sql.TextField() # data
	datatype = sql.CharField() # 'string', 'reference', 'int', 'float', or 'date'
	ordering = sql.IntegerField() # default null

def init():
	try:
		db.create_tables([User,Thing,Version,Datum], safe=True)
	except Exception as e: 
		raise
