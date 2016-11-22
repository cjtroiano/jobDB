from django.db import models

class job(models.Model):
	company = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	date = models.DateTimeField('date applied')