from django.db import models
import datetime;
# Create your models here.

OBJECT_NEWS=1
OBJECT_PROGRAMME=2
OBJECT_OPTIONS=(
	(OBJECT_NEWS,'News'),
	(OBJECT_PROGRAMME,'Programme'),
)

SERVICE_TRAVEL=1
SERVICE_APPLICATION=2
SERVICE_RECHARGE=3

SERVICE_OPTIONS=(
	(SERVICE_TRAVEL,"Travel Services"),
	(SERVICE_APPLICATION,"Application Services"),
	(SERVICE_RECHARGE,"Recharge Services"),
)

class User(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	def __str__(self):
		return self.name+' ('+self.email+')'

class Message(models.Model):
	msg=models.CharField(max_length=500)
	time=models.DateTimeField('Creation time',auto_now=True)
	user=models.ForeignKey(User)
	def __str__(self):
		return self.msg
		
class Object(models.Model):
	content=models.CharField(max_length=500)
	time=models.DateTimeField('Creation time',auto_now=True)
	object_type=models.IntegerField(choices=OBJECT_OPTIONS)
	def __str__(self):
		return self.content;

class Service(models.Model):
	name=models.CharField(max_length=100)
	service_type=models.IntegerField(choices=SERVICE_OPTIONS)
	def __str__(self):
		return self.name
