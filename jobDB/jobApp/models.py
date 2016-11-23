from django.db import models

class Job(models.Model):
	company = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	date = models.DateTimeField('date applied')

	def __str__(self):
		output = self.company + " " + self.position + " " + str(self.date)
		return output