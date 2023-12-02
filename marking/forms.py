from django import forms
from django.forms import ModelForm
from .models import Paper, Cutscore

# Create the form class.
class Q1Form(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q1a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q1b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q1c = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q1d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q1a', 'q1b', 'q1c', 'q1d')

class Q1Form_AMME(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q1a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q1b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q1c = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q1d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q1a', 'q1b', 'q1c', 'q1d')

class Q1Form_AMEE(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q1a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q1b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q1c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q1d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q1a', 'q1b', 'q1c', 'q1d')

class Q1Form_AMMEE(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAMEE_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),
    ('EE', 'EE'),
    )
	q1a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q1b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q1c = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q1d = forms.ChoiceField(choices=NAMEE_choice, widget=forms.RadioSelect)

	class Meta:
		model = Paper
		fields = ('q1a', 'q1b', 'q1c', 'q1d')

class Q1Form_AEME(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q1a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q1b = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q1c = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q1d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q1a', 'q1b', 'q1c', 'q1d')

class Q1Form_AEEM(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q1a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q1b = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q1c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q1d = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q1a', 'q1b', 'q1c', 'q1d')

class Q2Form(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q2a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q2b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q2c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q2d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q2a', 'q2b', 'q2c', 'q2d')

class Q2Form_AMME(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q2a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q2b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q2c = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q2d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q2a', 'q2b', 'q2c', 'q2d')

class Q2Form_AMEE(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q2a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q2b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q2c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q2d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q2a', 'q2b', 'q2c', 'q2d')

class Q2Form_AEME(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q2a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q2b = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q2c = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q2d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q2a', 'q2b', 'q2c', 'q2d')

class Q2Form_AEEM(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q2a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q2b = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q2c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q2d = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q2a', 'q2b', 'q2c', 'q2d')

class Q3Form(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q3a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q3b = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q3c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q3d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q3a', 'q3b', 'q3c', 'q3d')

class Q3Form_AMME(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q3a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q3b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q3c = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q3d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q3a', 'q3b', 'q3c', 'q3d')

class Q3Form_AMEE(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q3a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q3b = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q3c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q3d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q3a', 'q3b', 'q3c', 'q3d')

class Q3Form_AEME(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q3a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q3b = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q3c = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q3d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q3a', 'q3b', 'q3c', 'q3d')

class Q3Form_AEEM(ModelForm):
	NA_choice = (
    ('N','N'),
    ('A', 'A'),)
	NAM_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),)
	NAME_choice = (
    ('N','N'),
    ('A', 'A'),
    ('M', 'M'),
    ('E', 'E'),)
	q3a = forms.ChoiceField(choices=NA_choice, widget=forms.RadioSelect)
	q3b = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q3c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q3d = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	class Meta:
		model = Paper
		fields = ('q3a', 'q3b', 'q3c', 'q3d')

		
class CutscoreForm(ModelForm):
	achieved = forms.IntegerField(min_value=3, max_value=10)
	merit = forms.IntegerField(min_value=10, max_value=16)
	excellence = forms.IntegerField(min_value=16, max_value=24)
	class Meta:
		model = Cutscore
		fields = ('achieved', 'merit', 'excellence')