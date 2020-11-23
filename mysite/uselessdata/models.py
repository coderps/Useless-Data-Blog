from django.db import models
from django.db.models import CharField
from datetime import datetime as dt
from django.utils import timezone

# Create your models here.

class Blogs(models.Model):
	bid = models.AutoField(primary_key=True)
	btitle = models.CharField(max_length=200)
	bsummary = models.CharField(max_length=500,default=btitle)
	created_at = models.DateTimeField(default=dt.now(), blank=True)
	start_date = models.DateTimeField(default=dt.now(), blank=True)
	end_date = models.DateTimeField(default=dt.now(), blank=True)
	bclaps = models.IntegerField(default=0)
	remarks = models.CharField(max_length=500, default='NA')
	bimg = models.ImageField(upload_to='experiments', blank=True)

	def __str__(self):
		return self.btitle

class Comments(models.Model):
	cid = models.AutoField(primary_key=True)
	cdesc = models.CharField(max_length=1000)
	bid = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	username = models.CharField(max_length=50, default='Anonymous')
	written_at = models.DateTimeField(default=dt.now(), blank=True)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return str(self.bid) + ": " + str(self.cdesc[:50]) + " (" + str(self.username) + ")"

class Contacts(models.Model):
	contact_id = models.AutoField(primary_key=True)
	cname = models.CharField(max_length=50, blank=True)  
	email = models.CharField(max_length=500)
	created_at = models.DateTimeField(default=dt.now())
	message = models.CharField(max_length=500, default='NA')

	def __str__(self):
		return str(self.email) + ": " + str(self.message)