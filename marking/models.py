from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Standard(models.Model): #Info about the standard
	standard_number = models.CharField(max_length=5)
	title = models.CharField(max_length=50)
	level = models.IntegerField(default=2)
	CHOICES = (
		('AMME', 'AMME'),
		('AMEE', 'AMEE'),
		('AEME', 'AEME'),
		('AEEM', 'AEEM'),
		)
	q1_type = models.CharField(max_length=5, choices = CHOICES, default='AMME')
	q2_type = models.CharField(max_length=5, choices = CHOICES, default='AMME')
	q3_type = models.CharField(max_length=5, choices = CHOICES, default='AMME')


	def __str__(self):
		return str(self.standard_number + ': ' + self.title + '. Level '+ str(self.level))


class Paper(models.Model):
	school = models.IntegerField()
	user = models.ForeignKey(User, related_name='user', default=1, on_delete=models.SET_DEFAULT)
	standard = models.ForeignKey(Standard, related_name='paper_standard', default=1, on_delete=models.SET_DEFAULT)

	q1a = models.CharField(max_length=2, default='N')
	q1b = models.CharField(max_length=2, default='N')
	q1c = models.CharField(max_length=2, default='N')
	q1d = models.CharField(max_length=2, default='N')

	q2a = models.CharField(max_length=2, default='N')
	q2b = models.CharField(max_length=2, default='N')
	q2c = models.CharField(max_length=2, default='N')
	q2d = models.CharField(max_length=2, default='N')

	q3a = models.CharField(max_length=2, default='N')
	q3b = models.CharField(max_length=2, default='N')
	q3c = models.CharField(max_length=2, default='N')
	q3d = models.CharField(max_length=2, default='N')

	q1_total = models.IntegerField(default=0)
	q2_total = models.IntegerField(default=0)
	q3_total = models.IntegerField(default=0)

	q1_letter = models.CharField(max_length=2, default='N0')
	q2_letter = models.CharField(max_length=2, default='N0')
	q3_letter = models.CharField(max_length=2, default='N0')
	
	total_score = models.IntegerField(default=0)

	paper_submitted = models.BooleanField(default=False)
	marking_created = models.DateTimeField(auto_now_add=True)
	marking_updated = models.DateTimeField(auto_now=True)

	paper_void = models.BooleanField(default=False)

	check_marker = models.CharField(max_length=20, default='')
	check_marked = models.BooleanField(default=False)

	#Need a void field, 
	def __str__(self):
		return str('User: ' + self.user.first_name + '. School: ' + str(self.school))

class Marker(models.Model): #Extends the User model
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	chief_marker = models.BooleanField(default=False)
	standard = models.ForeignKey(Standard, related_name='standard', default=1, on_delete=models.SET_DEFAULT)
	

	def __str__(self):
		return str(self.user.first_name)

class Cutscore(models.Model): #Records the cutscores
	achieved = models.IntegerField(default=7)
	merit = models.IntegerField(default=14)
	excellence = models.IntegerField(default=19)
	standard = models.ForeignKey(Standard, related_name='cutscore_standard', default=1, on_delete=models.SET_DEFAULT)




#Have standard as a model. Then can link to it in Marker, Paper, and Cutscore.

