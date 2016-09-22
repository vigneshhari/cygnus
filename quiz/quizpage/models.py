from django.db import models

# Create your models here.

class Quiz(models.Model):
	quiz_id = models.IntegerField()
	quizname = models.CharField(max_length = 500)
	creationdate = models.DateTimeField()
	quiz_link = models.CharField(max_length = 5000)
	attempt = models.IntegerField()

class Quiz_data(models.Model):
	quiz_id = models.IntegerField()
	question = models.CharField(max_length = 500)
	question_desc = models.CharField(max_length = 5000)
	question_type = models.CharField(max_length = 100)
	question_clue = models.IntegerField()
	Option1 = models.CharField(max_length = 100)
	Option2 = models.CharField(max_length = 100)
	Option3 = models.CharField(max_length = 100)
	Option4 = models.CharField(max_length = 100)
	answer = models.CharField(max_length = 100)

class Quiz_history(models.Model):
	quiz_id = models.IntegerField()
	user_id = models.IntegerField()
	score = models.IntegerField()
	Date = models.DateTimeField()
