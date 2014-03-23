from django.db import models
from django.contrib.auth.models import User

class topology(models.Model):
	name=models.CharField(max_length=50)
	jsonData=models.TextField(blank=True)
	user=models.ForeignKey(User)
	task=models.BooleanField(default='false')
	instance_id=models.CharField(max_length=50)

