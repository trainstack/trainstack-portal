from django.db.models import CharField, TextField, ForeignKey, BooleanField, Model
from django.contrib.auth.models import User

class Task(Model):
    text=TextField()

class Topology(Model):
    name = CharField(max_length=50)
    jsonData = TextField(blank=True)
    user = ForeignKey(User)
    task = BooleanField(default='false')
    instance_id = CharField(max_length=50)

