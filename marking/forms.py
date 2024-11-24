from django import forms
from django.forms import ModelForm
from .models import Paper, Cutscore, Total

# Create the form class.

class TotalForm(ModelForm):
	total_choice = (
		('E8', 'E8'),
		('E7', 'E7'),
		('M6', 'M6'),
		('M5', 'M5'),
		('A4', 'A4'),
		('A3', 'A3'),
		('N2', 'N2'),
		('N1', 'N1'),
		('N0', 'N0'),
		)

	grades_eemm = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eema = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eemn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eeaa = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eean = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eenn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_emma = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_emmn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_emaa = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eman = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_emnn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eaaa = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eaan = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_eann = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_ennn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_mmma = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_mmmn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_mmaa = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_mman = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_mmnn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_maaa = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_maan = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_mann = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_mnnn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_aaaa = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_aaan = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_aann = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_annn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)
	grades_nnnn = forms.ChoiceField(choices=total_choice, widget=forms.RadioSelect)

	class Meta:
		model = Total
		fields = ('grades_eemm', 'grades_eema', 'grades_eemn', 'grades_eeaa',
			 'grades_eean' , 'grades_eenn' , 'grades_emma' , 'grades_emmn',
			 'grades_emaa', 'grades_eman', 'grades_emnn', 'grades_eaaa',
			 'grades_eaan', 'grades_eann', 'grades_ennn',
			 'grades_mmma', 'grades_mmmn', 'grades_mmaa', 'grades_mman',
			 'grades_mmnn', 'grades_maaa', 'grades_maan', 'grades_mann',
			 'grades_mnnn',
			 'grades_aaaa', 'grades_aaan', 'grades_aann', 'grades_annn',
			 'grades_nnnn',
			 )

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

class Q2Form_MEEE(ModelForm): #Added this question for 2024
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
	q2a = forms.ChoiceField(choices=NAM_choice, widget=forms.RadioSelect)
	q2b = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q2c = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
	q2d = forms.ChoiceField(choices=NAME_choice, widget=forms.RadioSelect)
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