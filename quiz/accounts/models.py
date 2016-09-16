from django.db import models

# Create your models here.

class User_Account(models.Model):
	user_id = models.IntegerField()
	name = models.CharField(max_length = 500)
	password = models.CharField(max_length = 100)
	mail = models.CharField(max_length = 100)
	phone_no = models.CharField(max_length = 25)
	vericode = models.CharField(max_length = 100)
	verified = models.IntegerField()
	score = models.IntegerField()

