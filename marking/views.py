from django.shortcuts import render, redirect
from .models import Paper, User, Marker, Cutscore
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .my_functions import *

# Create your views here.

def mark_menu(request):

	#Who is the user?
	try:
		user = User.objects.get(username=request.user.username)
		the_marker = Marker.objects.get(user=user)
	except:
		return redirect('login_user')

	content = {
	'the_marker': the_marker

	}

	return render(request, 'mark_menu.html', content)

def enter_school_id(request):
	#This is the first step in marking. It creates a new, empty paper with the school id and standard number
	#Then goes from here to first question.

	#Who is the user?
	try:
		user = User.objects.get(username=request.user.username)
		the_marker = Marker.objects.get(user=user)
		the_standard = the_marker.standard
	except:
		return redirect('login_user')

	if request.method=='POST': #Check if school is submitted
		current_school_number = int(request.POST['school_number'])
		current_paper = Paper(user=user, school=current_school_number, standard=the_standard)
		current_paper.save()

		return redirect('mark_current_question', current_question='1' )

	else: 	#If it isnt submitted, then display the form
		content = {'the_marker': the_marker}
		return render(request, 'enter_school_id.html', content)

def login_user(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		
		if user is not None:
			login(request, user)
			messages.success(request, ('You have successfully logged in'))
			return redirect('mark_menu')

        
		else:
			messages.success(request, ('Error logging in...'))
			return redirect('login_user')
        

	else:	
		return render(request, 'login.html', {})

def logout_user(request):
	messages.success(request, ('You have been logged out.'))
	logout(request)
	return redirect('mark_menu')

def mark_current_question(request, current_question):
	#This takes the last paper in user's database (hopefully the one they just created)
	
	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	if request.method=="POST": #User submits answers. 
		current_paper = Paper.objects.filter(user=user).last()

		if current_question == '1': 

			#Save the answers to the database
			#Here we need to figure out what form to send out
			what_standard = Marker.objects.get(user=user).standard

			if what_standard.q1_type == 'AMME':
				f = Q1Form_AMME(request.POST, instance=current_paper)
			elif what_standard.q1_type == 'AMEE':
				f = Q1Form_AMEE(request.POST, instance=current_paper)
			elif what_standard.q1_type == 'AEME':
				f = Q1Form_AEME(request.POST, instance=current_paper)
			elif what_standard.q1_type == 'AEEM':
				f = Q1Form_AEEM(request.POST, instance=current_paper)
			
			f.save()

			#Get ready to go to next question
			current_question = int(current_question) + 1
			return redirect('mark_current_question', current_question=current_question)

		if current_question == '2':

			#Save the answers to the database
			#Here we need to figure out what form to send out
			what_standard = Marker.objects.get(user=user).standard

			if what_standard.q2_type == 'AMME':
				f = Q2Form_AMME(request.POST, instance=current_paper)
			elif what_standard.q2_type == 'AMEE':
				f = Q2Form_AMEE(request.POST, instance=current_paper)
			elif what_standard.q2_type == 'AEME':
				f = Q2Form_AEME(request.POST, instance=current_paper)
			elif what_standard.q2_type == 'AEEM':
				f = Q2Form_AEEM(request.POST, instance=current_paper)
			f.save()

			#Get ready to go to next question
			current_question = int(current_question) + 1
			return redirect('mark_current_question', current_question=current_question)

		if current_question == '3':

			#Save the answers to the database
			#Here we need to figure out what form to send out
			what_standard = Marker.objects.get(user=user).standard

			if what_standard.q3_type == 'AMME':
				f = Q3Form_AMME(request.POST, instance=current_paper)
			elif what_standard.q3_type == 'AMEE':
				f = Q3Form_AMEE(request.POST, instance=current_paper)
			elif what_standard.q3_type == 'AEME':
				f = Q3Form_AEME(request.POST, instance=current_paper)
			elif what_standard.q3_type == 'AEEM':
				f = Q3Form_AEEM(request.POST, instance=current_paper)
			f.save()

			#Go to totals page				
			return redirect('total_marks')



	else: #Sends form out. This form is populated with answers already stored (default = N)
		if current_question == '1': #Send the Q1 form
			current_paper = Paper.objects.filter(user=user).last()
			
			#Here we need to figure out what form to send out
			what_standard = Marker.objects.get(user=user).standard

			if what_standard.q1_type == 'AMME':
				form = Q1Form_AMME(instance=current_paper)
			elif what_standard.q1_type == 'AMEE':
				form = Q1Form_AMEE(instance=current_paper)
			elif what_standard.q1_type == 'AEME':
				form = Q1Form_AEME(instance=current_paper)
			elif what_standard.q1_type == 'AEEM':
				form = Q1Form_AEEM(instance=current_paper)
			

			content = {
			'form':form,
			'button_label':'Go to Q2',
			'page_heading':'Question 1',
			'current_marking': True,
			}
			#return render(request, 'test.html', content)
			return render(request, 'mark_q1.html', content)

		if current_question == '2': #Send the Q2 form
			current_paper = Paper.objects.filter(user=user).last()

			#Here we need to figure out what form to send out
			what_standard = Marker.objects.get(user=user).standard

			if what_standard.q2_type == 'AMME':
				form = Q2Form_AMME(instance=current_paper)
			elif what_standard.q2_type == 'AMEE':
				form = Q2Form_AMEE(instance=current_paper)
			elif what_standard.q2_type == 'AEME':
				form = Q2Form_AEME(instance=current_paper)
			elif what_standard.q2_type == 'AEEM':
				form = Q2Form_AEEM(instance=current_paper)
			
			content = {
			'form':form,
			'button_label':'Go to Q3',
			'page_heading':'Question 2',
			'current_marking': True,
			}
			return render(request, 'mark_q1.html', content)

		if current_question == '3': #Send the Q3 form
			current_paper = Paper.objects.filter(user=user).last()

			#Here we need to figure out what form to send out
			what_standard = Marker.objects.get(user=user).standard

			if what_standard.q3_type == 'AMME':
				form = Q3Form_AMME(instance=current_paper)
			elif what_standard.q3_type == 'AMEE':
				form = Q3Form_AMEE(instance=current_paper)
			elif what_standard.q3_type == 'AEME':
				form = Q3Form_AEME(instance=current_paper)
			elif what_standard.q3_type == 'AEEM':
				form = Q3Form_AEEM(instance=current_paper)

			content = {
			'form':form,
			'button_label':'Go to Totals',
			'page_heading':'Question 3',
			'current_marking': True,
			}
			return render(request, 'mark_q1.html', content)

def total_marks(request):
	#Totals the scores
	
	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	current_paper = Paper.objects.filter(user=user).last()

	#Work out the letter grade eg A4 for each question, and write to database
	letter_grades, number_totals = get_letter_grades(current_paper)

	current_paper.save()

	content = {'current_paper': current_paper,
	'user': user,
	}
	return render(request, 'total_marks.html', content)

def review_marks(request, sort_type, the_marker):
	#Review and edit the scores, sorted by date
	
	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')



	#We want to view papers by marker, not the logged in user (so chief markers can use)
	marker_id = int(the_marker)
	view_marker = Marker.objects.get(pk=marker_id)
	name_on_page = User.objects.get(marker__id=marker_id)


	#Are we ordering by date 'd' or school 's'
	if sort_type=='d':
		#Order papers by date
		all_papers = Paper.objects.filter(user__marker__id=marker_id).filter(paper_submitted=True).filter(check_marked=False).order_by('-pk')
		sort_by_date = True
	else:
		#Order papers by school
		all_papers = Paper.objects.filter(user__marker__id=marker_id).filter(paper_submitted=True).filter(check_marked=False).order_by('-pk').order_by('school')
		sort_by_date = False


	#count the papers
	total_papers_count = len(all_papers)
	all_void_papers = Paper.objects.filter(user__marker__id=marker_id).filter(paper_submitted=True).filter(check_marked=False).filter(paper_void=True)
	total_void_count = len(all_void_papers)
	total_graded_count = total_papers_count - total_void_count

	content = {'all_papers':all_papers,
	'sort_by_date': sort_by_date, 
	'total_papers_count': total_papers_count,
	'total_void_count': total_void_count,
	'total_graded_count': total_graded_count,
	'view_marker': view_marker,
	'name_on_page': name_on_page,
	}

	return render(request, 'review_marks.html', content)

def review_check_marks(request):
	#Review and edit the scores, sorted by date
	
	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	#Check they are a chief marker
	the_marker = Marker.objects.get(user=user)
	
	#Pull out the standard
	the_standard = Marker.objects.get(user=user).standard


	if the_marker.chief_marker==True:
		all_papers = Paper.objects.filter(user=user).filter(paper_submitted=True).filter(check_marked=True).filter(standard=the_standard).order_by('-pk').order_by('school').order_by('check_marker')
		#count the papers
		total_papers_count = len(all_papers)


		content = {'all_papers':all_papers,
		}
		return render(request, 'review_check_marks.html', content)
	else:
		return redirect('mark_menu')


def confirm_void(request):
	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	if request.method=="POST": #Confirms the paper is void 
		current_paper = Paper.objects.filter(user=user).last()
		current_paper.paper_void = True
		make_all_grades_void(current_paper)
		current_paper.save()

		return redirect('total_marks')

	else:
		return render(request, 'confirm_void.html', {})

def edit_menu(request, paper_id):
	
	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')
	
	#Grab the paper to be editted
	editing_paper = Paper.objects.get(pk=int(paper_id))


	#Check to see if you are allowed to access this paper
	the_marker = Marker.objects.get(user=user)

	if editing_paper.user==user or the_marker.chief_marker==True:
		#See if it is either the chief marker OR the actual person who marked this paper
		

		content = {
		'paper_id': paper_id,
		'editing_paper': editing_paper,
		'the_marker': the_marker,
		}

		return render(request, 'edit_menu.html', content)

	else: #If it isnt an allowed person to edit, they get sent back to the marking menu. 
		return redirect('mark_menu')

def confirm_void_menu(request, paper_id):
	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')
	
	#Grab the paper to be editted
	editing_paper = Paper.objects.get(pk=int(paper_id))


	#Check to see if you are allowed to access this paper
	the_marker = Marker.objects.get(user=user)

	if editing_paper.user==user or the_marker.chief_marker==True:
		#See if it is either the chief marker OR the actual person who marked this paper
		
		if request.method=="POST": #They have confirmed that they wish to change the void status
			
			if editing_paper.paper_void==True: #The paper needs to change to UN void
				editing_paper.paper_void = False
				editing_paper.save()

				#Back to edit_menu
				return redirect('edit_menu', paper_id=paper_id)

			else: #Wish to change to VOID
				make_all_grades_void(editing_paper) #Change all grades to N0, 0 etc

				editing_paper.save()

				#Back to edit_menu
				return redirect('edit_menu', paper_id=paper_id)
		

		else: #Display the page

			content = {
			'paper_id': paper_id,
			'editing_paper': editing_paper,
			'the_marker': the_marker,
			}

			return render(request, 'confirm_void_menu.html', content)

	else: #If it isnt an allowed person to edit, they get sent back to the marking menu. 
		return redirect('mark_menu')

def confirm_delete(request, paper_id):
		#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')
	
	#Grab the paper to be editted
	editing_paper = Paper.objects.get(pk=int(paper_id))


	#Check to see if you are allowed to access this paper
	the_marker = Marker.objects.get(user=user)

	if editing_paper.user==user or the_marker.chief_marker==True:
		#See if it is either the chief marker OR the actual person who marked this paper
		
		if request.method=="POST": #They have confirmed that they wish to delete
			
			editing_paper.delete()
			messages.success(request, ('You have deleted this paper'))

			#Back to edit_menu
			return redirect('review_marks', sort_type='d', the_marker=the_marker.id)
		

		else: #Display the page

			content = {
			'paper_id': paper_id,
			'editing_paper': editing_paper,
			'the_marker': the_marker,
			}

			return render(request, 'confirm_delete.html', content)

	else: #If it isnt an allowed person to edit, they get sent back to the marking menu. 
		return redirect('mark_menu')

def edit_paper(request, paper_id, question_number):

	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')
	
	#Grab the paper to be editted
	editing_paper = Paper.objects.get(pk=int(paper_id))


	#Check to see if you are allowed to access this paper
	the_marker = Marker.objects.get(user=user)

	if editing_paper.user==user or the_marker.chief_marker==True:
		#See if it is either the chief marker OR the actual person who marked this paper
		
		if request.method=="POST": #They have confirmed that they wish to edit
			what_standard = Marker.objects.get(user=user).standard
			if question_number == '1': 

				#Grab the data from the form and save
				if what_standard.q1_type == 'AMME':
					f = Q1Form_AMME(request.POST, instance=editing_paper)
				elif what_standard.q1_type == 'AMEE':
					f = Q1Form_AMEE(request.POST, instance=editing_paper)
				elif what_standard.q1_type == 'AEME':
					f = Q1Form_AEME(request.POST, instance=editing_paper)
				elif what_standard.q1_type == 'AEEM':
					f = Q1Form_AEEM(request.POST, instance=editing_paper)
				f.save()

				#Grab the paper from database again, so you can update the totals
				editing_paper = Paper.objects.get(pk=int(paper_id))
				
				#Work out the letter grade eg A4 for each question
				letter_grades, number_totals = get_letter_grades(editing_paper)

				editing_paper.save()

				messages.success(request, ('Q1 is updated'))

				#Back to edit_menu
				return redirect('edit_menu', paper_id=paper_id)
			
			if question_number == '2': 

				#Save the answers to the database
				#Grab the data from the form and save
				if what_standard.q2_type == 'AMME':
					f = Q2Form_AMME(request.POST, instance=editing_paper)
				elif what_standard.q2_type == 'AMEE':
					f = Q2Form_AMEE(request.POST, instance=editing_paper)
				elif what_standard.q2_type == 'AEME':
					f = Q2Form_AEME(request.POST, instance=editing_paper)
				elif what_standard.q2_type == 'AEEM':
					f = Q2Form_AEEM(request.POST, instance=editing_paper)
				f.save()

				#Grab the paper from database again, so you can update the totals
				editing_paper = Paper.objects.get(pk=int(paper_id))
				
				#Work out the letter grade eg A4 for each question
				letter_grades, number_totals = get_letter_grades(editing_paper)

				editing_paper.save()

				messages.success(request, ('Q2 is updated'))

				#Back to edit_menu
				return redirect('edit_menu', paper_id=paper_id)

			if question_number == '3': 

				#Save the answers to the database
				if what_standard.q3_type == 'AMME':
					f = Q3Form_AMME(request.POST, instance=editing_paper)
				elif what_standard.q3_type == 'AMEE':
					f = Q3Form_AMEE(request.POST, instance=editing_paper)
				elif what_standard.q3_type == 'AEME':
					f = Q3Form_AEME(request.POST, instance=editing_paper)
				elif what_standard.q3_type == 'AEEM':
					f = Q3Form_AEEM(request.POST, instance=editing_paper)
				f.save()
				f.save()

				#Grab the paper from database again, so you can update the totals
				editing_paper = Paper.objects.get(pk=int(paper_id))
				
				#Work out the letter grade eg A4 for each question
				letter_grades, number_totals = get_letter_grades(editing_paper)

				editing_paper.save()

				messages.success(request, ('Q3 is updated'))

				#Back to edit_menu
				return redirect('edit_menu', paper_id=paper_id)
		
		else: #Sends form out. This form is populated with answers already stored (default = N)
			#Here we need to figure out what form to send out
			what_standard = Marker.objects.get(user=user).standard
			
			if question_number == '1': #Send the Q1 form


				if what_standard.q1_type == 'AMME':
					form = Q1Form_AMME(instance=editing_paper)
				elif what_standard.q1_type == 'AMEE':
					form = Q1Form_AMEE(instance=editing_paper)
				elif what_standard.q1_type == 'AEME':
					form = Q1Form_AEME(instance=editing_paper)
				elif what_standard.q1_type == 'AEEM':
					form = Q1Form_AEEM(instance=editing_paper)


				content = {
				'form':form,
				'button_label':'Save Edit',
				'page_heading':'Edit Question 1',
				}
			
				return render(request, 'mark_q1.html', content)
		
			if question_number == '2': #Send the Q2 form
				if what_standard.q2_type == 'AMME':
					form = Q2Form_AMME(instance=editing_paper)
				elif what_standard.q2_type == 'AMEE':
					form = Q2Form_AMEE(instance=editing_paper)
				elif what_standard.q2_type == 'AEME':
					form = Q2Form_AEME(instance=editing_paper)
				elif what_standard.q2_type == 'AEEM':
					form = Q2Form_AEEM(instance=editing_paper)

				content = {
				'form':form,
				'button_label':'Save Edit',
				'page_heading':'Edit Question 2',
				}

				return render(request, 'mark_q1.html', content)
		
			if question_number == '3': #Send the Q3 form
				if what_standard.q3_type == 'AMME':
					form = Q3Form_AMME(instance=editing_paper)
				elif what_standard.q3_type == 'AMEE':
					form = Q3Form_AMEE(instance=editing_paper)
				elif what_standard.q3_type == 'AEME':
					form = Q3Form_AEME(instance=editing_paper)
				elif what_standard.q3_type == 'AEEM':
					form = Q3Form_AEEM(instance=editing_paper)

				content = {
				'form':form,
				'button_label':'Save Edit',
				'page_heading':'Edit Question 3',
				}
			
				return render(request, 'mark_q1.html', content)

	else: #If it isnt an allowed person to edit, they get sent back to the marking menu. 
		return redirect('mark_menu')

def super_review_menu(request):

	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	#Check they are a chief marker
	the_marker = Marker.objects.get(user=user)
	#Pull out the standard
	the_standard = Marker.objects.get(user=user).standard

	if the_marker.chief_marker==True:
		
		all_markers = Marker.objects.filter(standard=the_standard).order_by('user__first_name')

		return render(request, 'super_review_menu.html', {'all_markers': all_markers})

	else:
		return redirect('mark_menu')

def test_page(request):
		#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	#Check they are a chief marker
	the_marker = Marker.objects.get(user=user)

	#Pull out the standard
	the_standard = Marker.objects.get(user=user).standard

	all_markers = Marker.objects.filter(standard=the_standard).order_by('user__first_name')

	all_papers = Paper.objects.filter(standard=the_standard).filter(paper_submitted=True)

	content = {'the_standard': the_standard,
				'all_markers': all_markers,
				'all_papers': all_papers,
				}


	return render(request, 'test.html', content)

def statistics(request):

	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	#Check they are a chief marker
	the_marker = Marker.objects.get(user=user)

	#Pull out the standard
	the_standard = Marker.objects.get(user=user).standard

	if the_marker.chief_marker==True:
		
		all_markers = Marker.objects.filter(standard=the_standard).order_by('user__first_name')
		all_chief_markers = Marker.objects.filter(standard=the_standard).filter(chief_marker=True).order_by('user__first_name')

		#Count all papers
		all_papers = Paper.objects.filter(standard=the_standard).filter(paper_submitted=True).filter(check_marked=False)
		total_papers_count = len(all_papers)

		#Count the voids
		all_void_papers = Paper.objects.filter(paper_submitted=True).filter(paper_void=True).filter(standard=the_standard).filter(check_marked=False)
		total_void_count = len(all_void_papers)

		#Count the non_voids
		total_graded_count = total_papers_count - total_void_count

		#Count all thye check marked
		all_check_marked_papers = Paper.objects.filter(standard=the_standard).filter(paper_submitted=True).filter(check_marked=True)
		total_check_marked_count = len(all_check_marked_papers)

		#Count the voids
		all_void_check_marked_papers = Paper.objects.filter(paper_submitted=True).filter(paper_void=True).filter(standard=the_standard).filter(check_marked=True)
		total_check_marked_void_count = len(all_void_check_marked_papers)

		#Count the non_voids
		total_graded_check_marked_count = total_check_marked_count - total_check_marked_void_count

		marking_stats_by_person = []
		for marker in all_markers: #Gets stats on papers marked per person
			#Count their papers
			all_papers_for_marker = Paper.objects.filter(user__marker__id=marker.id).filter(paper_submitted=True).filter(check_marked=False)
			person_total_papers_count = len(all_papers_for_marker)

			#Count their voids
			all_void_papers_for_marker = Paper.objects.filter(user__marker__id=marker.id).filter(paper_submitted=True).filter(paper_void=True).filter(check_marked=False)
			person_total_void_count = len(all_void_papers_for_marker)

			#Count their non voids
			person_total_graded_count = person_total_papers_count - person_total_void_count

			#Collect info ready to send to template
			person_stats = {
			'name': marker.user.first_name, 
			'person_total_papers_count': person_total_papers_count,
			'person_total_void_count': person_total_void_count,
			'person_total_graded_count': person_total_graded_count,
			}

			#Append to the list at start of for loop
			marking_stats_by_person.append(person_stats) 

		marking_stats_by_chief_markers = []
		#Marking stats for the chief markers
		for chief_marker in all_chief_markers:
			#Count their papers
			all_papers_for_marker = Paper.objects.filter(user__marker__id=chief_marker.id).filter(paper_submitted=True).filter(check_marked=True)
			person_total_papers_count = len(all_papers_for_marker)

			#Count their voids
			all_void_papers_for_marker = Paper.objects.filter(user__marker__id=chief_marker.id).filter(paper_submitted=True).filter(paper_void=True).filter(check_marked=True)
			person_total_void_count = len(all_void_papers_for_marker)

			#Count their non voids
			person_total_graded_count = person_total_papers_count - person_total_void_count

			#Collect info ready to send to template
			person_stats = {
			'name': chief_marker.user.first_name, 
			'person_total_papers_count': person_total_papers_count,
			'person_total_void_count': person_total_void_count,
			'person_total_graded_count': person_total_graded_count,
			}

			#Append to the list at start of for loop
			marking_stats_by_chief_markers.append(person_stats) 

		#Count marks per question
		all_non_void_papers = Paper.objects.filter(paper_submitted=True).filter(paper_void=False).filter(standard=the_standard).filter(check_marked=False)
		
		#A list to hold the totals of each score
		stats_total_score = [0] * 25

		#A list of lists to hold all grades given. Later will count the grades in each list
		list_of_lists = [[] for i in range(15)]

		#Have some sort of holding list/dictionary for totals
		for paper in all_non_void_papers:
			#Count the total scores
			stats_total_score[paper.total_score] += 1

			#record all the question scores. Count after the for loop
			stats_all_question_scores = add_score_to_list(paper, list_of_lists)

		#Get all the stats for the q1a questions
		all_percentages_per_question = count_all_grades(list_of_lists[3:], question_type='q1a')

		all_labels = ['Q1 Total', 'Q2 Total', 'Q3_Total', 
		'Q1a', 'Q1b', 'Q1c', 'Q1d', 
		'Q2a', 'Q2b', 'Q2c', 'Q2d',  
		'Q3a', 'Q3b', 'Q3c', 'Q3d', 
		]

		#Get all the stats for the q1, q2, q3 questions
		all_percentages_per_question_letter = count_all_grades(list_of_lists[0:3], question_type='q1_letter')


		#zipped list
		zipped = zip(all_labels[3:], all_percentages_per_question)
		zipped_letter = zip(all_labels[0:3], all_percentages_per_question_letter)

		#Cutscores
		cutscore = Cutscore.objects.get(standard=the_standard)
		output_totals = cutscore_calculator(cutscore, stats_total_score)


		content = {
		'total_papers_count': total_papers_count,
		'total_void_count': total_void_count,
		'total_graded_count': total_graded_count,
		'total_graded_check_marked_count': total_graded_check_marked_count,
		'total_check_marked_count': total_check_marked_count,
		'total_check_marked_void_count': total_check_marked_void_count,
		'marking_stats_by_person': marking_stats_by_person,
		'stats_total_score': stats_total_score,
		'zipped': zipped,
		'zipped_letter': zipped_letter,
		'output_totals': output_totals, 
		'cutscore': cutscore,
		'marking_stats_by_chief_markers': marking_stats_by_chief_markers,
		}



		return render(request, 'statistics.html', content)

	else:
		return redirect('mark_menu')

def change_cutscores(request): 
	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	#Check they are a chief marker
	the_marker = Marker.objects.get(user=user)

	#Pull out the standard
	the_standard = Marker.objects.get(user=user).standard

	if the_marker.chief_marker==True:
		if request.method=="POST": #User changes cutscores
			current_cutscores = Cutscore.objects.get(standard=the_standard)

			f = CutscoreForm(request.POST, instance=current_cutscores)
			f.save()

			messages.success(request, ('Cutscores updated'))

			return redirect('statistics')

		else: #Populate the form
			current_cutscores = Cutscore.objects.get(standard=the_standard)

			form = CutscoreForm(instance=current_cutscores)

			return render(request, 'change_cutscores.html', {'form':form,})

	else:
		return redirect('mark_menu')

def check_marking(request): 

	#Check the user is logged in
	try:
		user = User.objects.get(username=request.user.username)
	except:
		return redirect('login_user')

	#Check they are a chief marker
	the_marker = Marker.objects.get(user=user)
	#Pull out the standard
	the_standard = Marker.objects.get(user=user).standard

	if the_marker.chief_marker==True:
		
		all_markers = Marker.objects.filter(standard=the_standard).order_by('user__first_name')

	if request.method=='POST': #Check if school is submitted
		current_school_number = int(request.POST['school_number'])
		
		#Find who the marker is you are checking, and add their name to database
		current_check_marker_id = int(request.POST['check_marker'])
		current_check_marker = Marker.objects.get(pk=current_check_marker_id)
		#current_check_marker_name = current_check_marker.user__first_name
		current_paper = Paper(user=user, school=current_school_number, 
			check_marker=current_check_marker, check_marked=True)
		current_paper.save()

		return redirect('mark_current_question', current_question='1' )

	else: 	#If it isnt submitted, then display the form
		content = {'all_markers': all_markers}
		return render(request, 'check_marking.html', content)

'''To do


-Add logged in name to menu bar?


'''