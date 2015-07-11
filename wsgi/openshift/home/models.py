from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	def __str__(self):
		return self.name+' ('+self.email+')'

class Message(models.Model):
	msg=models.CharField(max_length=500)
	time=models.DateTimeField('Creation time')
	user=models.ForeignKey(User)
	def __str__(self):
		return self.msg
