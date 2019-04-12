from settings import db
import peewee as sql

class BaseModel(sql.Model):
	class Meta:
		database = db

class User(BaseModel):
	name = sql.TextField()

try:
	db.create_tables([User], safe=True)
except Exception as e: 
	raise
