def calc_general_question(q1a, q1b, q1c, q1d, mark_scheme):

	conversion_dict = {'N':0, 'A': 1, 'M': 2, 'E': 3, 'EE': 6}
	ncea_grade = ['N0', 'N1', 'N2', 'A3', 'A4', 'M5', 'M6', 'E7', 'E8']
	total_dict = {'N0':0, 'N1':1, 'N2':2, 'A3':3, 'A4':4,
					 'M5':5, 'M6':6, 'E7':7, 'E8':8}

	grade_numbers = [conversion_dict[q1a], 
	conversion_dict[q1b], 
	conversion_dict[q1c], 
	conversion_dict[q1d],
	]

	total_score = sum(grade_numbers)

	if 6 in grade_numbers: #The got an EE grade. 
		#Remove the 6, replace with two 3's. Then sort. Then remove last entry (smallest number). 
		grade_numbers.remove(6)
		grade_numbers.append(3)
		grade_numbers.append(3)
		grade_numbers.sort(reverse=True)
		del grade_numbers[-1]

		total_score = sum(grade_numbers)

	#Have in descending order
	grade_numbers.sort(reverse=True)

	#Count the Es, Ms and As
	no_of_Es = 0
	no_of_Ms = 0
	no_of_As = 0
	for value in grade_numbers: 
		if value == 3:
			no_of_Es += 1
		elif value == 2:
			no_of_Ms += 1
		elif value == 1:
			no_of_As += 1

	#Now match the scores to the grade from the mark scheme.
	if no_of_Es > 2: #They got EEEM, EEEA, EEEN
		if no_of_Ms == 1: 
			question_grade = mark_scheme.grades_eeem 
		elif no_of_As == 1:
			question_grade = mark_scheme.grades_eeea
		else:
			question_grade = mark_scheme.grades_eeen


	elif no_of_Es == 2:  #They got 2 Es
		if no_of_Ms == 2: #EEMM
			question_grade = mark_scheme.grades_eemm

		elif no_of_Ms == 1: 
			if no_of_As  == 1: #EEMA
				question_grade = mark_scheme.grades_eema
			else:  #EEMN
				question_grade = mark_scheme.grades_eemn

		elif no_of_As == 2: # EEAA
			question_grade = mark_scheme.grades_eeaa

		elif no_of_As == 1: #EEAN
			question_grade = mark_scheme.grades_eean

		else:  #EENN
			question_grade = mark_scheme.grades_eenn

	elif no_of_Es == 1: #They got 1 E
		if no_of_Ms == 2:
			if no_of_As == 1: #EMMA
				question_grade = mark_scheme.grades_emma
			else: #emmn
				question_grade = mark_scheme.grades_emmn
		elif no_of_Ms == 1:
			if no_of_As == 2 :
				question_grade = mark_scheme.grades_emaa
			elif no_of_As == 1:
				question_grade = mark_scheme.grades_eman
			else:
				question_grade = mark_scheme.grades_emnn
		elif no_of_As == 3:
			question_grade = mark_scheme.grades_eaaa
		elif no_of_As == 2:
			question_grade = mark_scheme.grades_eaan
		elif no_of_As == 1:
			question_grade = mark_scheme.grades_eann
		else:
			question_grade = mark_scheme.grades_ennn

	elif no_of_Ms >=1:
		if no_of_Ms == 4:
			question_grade = mark_scheme.grades_mmmm  
		elif no_of_Ms == 3:
			if no_of_As==1:
				question_grade = mark_scheme.grades_mmma
			else:
				question_grade = mark_scheme.grades_mmmn
		elif no_of_Ms==2:
			if no_of_As==2:
				question_grade = mark_scheme.grades_mmaa
			elif no_of_As == 1:
				question_grade = mark_scheme.grades_mman
			else:
				question_grade = mark_scheme.grades_mmnn
		else:
			if no_of_As == 3:
				question_grade = mark_scheme.grades_maaa
			elif no_of_As == 2:
				question_grade = mark_scheme.grades_maan
			elif no_of_As == 1:
				question_grade = mark_scheme.grades_mann
			else:
				question_grade = mark_scheme.grades_mnnn

	elif no_of_As >=1:
		if no_of_As == 4:
			question_grade = mark_scheme.grades_aaaa
		elif no_of_As == 3:
			question_grade = mark_scheme.grades_aaan
		elif no_of_As == 2:
			question_grade = mark_scheme.grades_aann
		elif no_of_As == 1:
			question_grade = mark_scheme.grades_annn

	else:
		question_grade = 'N0'


	total_score = total_dict[question_grade]
	return total_score, question_grade	




def get_letter_grades(current_paper, mark_scheme):

	q1_total_score, q1_question_grade = calc_general_question(current_paper.q1a,
			current_paper.q1b,
			current_paper.q1c,
			current_paper.q1d, 
			mark_scheme,
			)

	q2_total_score, q2_question_grade = calc_general_question(current_paper.q2a,
			current_paper.q2b,
			current_paper.q2c,
			current_paper.q2d,
			mark_scheme,)

	q3_total_score, q3_question_grade = calc_general_question(current_paper.q3a,
			current_paper.q3b,
			current_paper.q3c,
			current_paper.q3d,
			mark_scheme,)



	letter_grades = [q1_question_grade, q2_question_grade, q3_question_grade]
	number_totals = [q1_total_score, q2_total_score, q3_total_score]


	#Update the database with totals, ready for saving
	current_paper.q1_total=q1_total_score
	current_paper.q2_total=q2_total_score
	current_paper.q3_total=q3_total_score
	current_paper.total_score=sum(number_totals)
	#Update the database with the letter grades
	current_paper.q1_letter=q1_question_grade
	current_paper.q2_letter=q2_question_grade
	current_paper.q3_letter=q3_question_grade
	current_paper.paper_submitted=True

	return letter_grades, number_totals

def make_all_grades_void(current_paper):
	current_paper.q1a = 'N'
	current_paper.q1b = 'N'
	current_paper.q1c = 'N'
	current_paper.q1d = 'N'
	current_paper.q2a = 'N'
	current_paper.q2b = 'N'
	current_paper.q2c = 'N'
	current_paper.q2d = 'N'
	current_paper.q3a = 'N'
	current_paper.q3b = 'N'
	current_paper.q3c = 'N'
	current_paper.q3d = 'N'
	current_paper.q1_letter='N0'
	current_paper.q2_letter='N0'
	current_paper.q3_letter='N0'
	current_paper.q1_total=0
	current_paper.q2_total=0
	current_paper.q3_total=0
	current_paper.total_score=0
	current_paper.paper_void = True

	return

def add_score_to_list(paper, list_of_lists):
	#In the list of lists we have
	#q1a, q1b, q1c, q1d, q1_letter_grade, q2a, etc
	list_of_lists[0].append(paper.q1_letter)
	list_of_lists[1].append(paper.q2_letter)
	list_of_lists[2].append(paper.q3_letter)
	list_of_lists[3].append(paper.q1a)
	list_of_lists[4].append(paper.q1b)
	list_of_lists[5].append(paper.q1c)
	list_of_lists[6].append(paper.q1d)
	list_of_lists[7].append(paper.q2a)
	list_of_lists[8].append(paper.q2b)
	list_of_lists[9].append(paper.q2c)
	list_of_lists[10].append(paper.q2d)
	list_of_lists[11].append(paper.q3a)
	list_of_lists[12].append(paper.q3b)
	list_of_lists[13].append(paper.q3c)
	list_of_lists[14].append(paper.q3d)
	


	return list_of_lists

def count_all_grades(list_of_lists, question_type): #Counts all grades for statistics purposes
	question_averages_list = [[] for i in range(len(list_of_lists))]
	
	'''all_labels = ['q1_letter', 'q2_letter', 'q3_letter', 
	'q1a', 'q1b', 'q1c', 'q1d', 
	'q2a', 'q2b', 'q2c', 'q2d',  
	'q3a', 'q3b', 'q3c', 'q3d', 
	] '''

	all_percentages = []
	ncea_grade = ['N0', 'N1', 'N2', 'A3', 'A4', 'M5', 'M6', 'E7', 'E8']
	for i in range(len(list_of_lists)):
		if len(question_type) == 3: #Its a 'q1a', not 'q1_letter'
			count_N = list_of_lists[i].count('N')
			count_A = list_of_lists[i].count('A')
			count_M = list_of_lists[i].count('M')
			count_E = list_of_lists[i].count('E')
			count_EE = list_of_lists[i].count('EE')

			#totals

			total_papers = count_N+count_A+count_M+count_E+count_EE

			average_q = (count_A + 2*count_M+3*count_E+count_EE*6)/total_papers

			percentages = [round(count_N/total_papers*100), 
			round(count_A/total_papers*100),
			round(count_M/total_papers*100),
			round(count_E/total_papers*100),
			round(count_EE/total_papers*100),
			round(average_q,1),
			]

			for j in range(len(percentages)):
				if percentages[j]==0:
					percentages[j]=''

			all_percentages.append(percentages)

		else: #Its a q1_letter etc
			counting_NCEA_list = []
			for j in ncea_grade:
				the_count = list_of_lists[i].count(j)
				counting_NCEA_list.append(the_count)

			total_papers = sum(counting_NCEA_list)

			#Work out percentages and average
			percentages = [] 
			cumulative_average = 0
			for index, value in enumerate(counting_NCEA_list):
				the_percent = value/total_papers*100
				cumulative_average+=(index*the_percent/100)
					
				percentages.append(round(the_percent))


			#Work out the averages
			

			percentages.append(round(cumulative_average, 2))

			all_percentages.append(percentages)

	return all_percentages

def cutscore_calculator(cutscore, stats_total_score): #Outputs the totals using the cutscores

		total_papers = sum(stats_total_score)
		total_N = round(sum(stats_total_score[0:cutscore.achieved])/total_papers*100)
		total_A = round(sum(stats_total_score[cutscore.achieved:cutscore.merit])/total_papers*100)
		total_M = round(sum(stats_total_score[cutscore.merit:cutscore.excellence])/total_papers*100)
		total_E = round(sum(stats_total_score[cutscore.excellence:])/total_papers*100)

		output_totals = [total_N, total_A, total_M, total_E]

		return output_totals





'''def calc_general_question(q1a, q1b, q1c, q1d):
	conversion_dict = {'N':0, 'A': 1, 'M': 2, 'E': 3, 'EE': 6}
	ncea_grade = ['N0', 'N1', 'N2', 'A3', 'A4', 'M5', 'M6', 'E7', 'E8']

	grade_numbers = [conversion_dict[q1a], 
	conversion_dict[q1b], 
	conversion_dict[q1c], 
	conversion_dict[q1d],
	]

	total_score = sum(grade_numbers)

	if 6 in grade_numbers: #The got an EE grade
		if total_score >= 8:
			question_grade = 'E8'
			total_score = 8
		else:
			question_grade = ncea_grade[total_score]

	elif 3 in grade_numbers: #They got at least one E grade
		no_of_Es = 0
		for value in grade_numbers: #Count number of Es
			if value == 3:
				no_of_Es += 1

		if no_of_Es == 2: #They got 2 Es
			if total_score >= 8:
				question_grade = 'E8'
				total_score = 8
			else:
				question_grade = ncea_grade[total_score]

		else: #They got 1 E. 
			if 2 in grade_numbers: #They got an E and an M
				if total_score >= 6: #They got at least an E, M, A
					question_grade = 'E7'
					total_score = 7
				else: #They only got an E, M
					question_grade = ncea_grade[total_score]
			elif total_score >= 4: #They got E,A or E, A, A or E, A, A, A
				question_grade = 'A4'
				total_score = 4
			else:	#The got an E only
				question_grade = ncea_grade[total_score]

	elif 2 in grade_numbers: #They got at least one M

		no_of_Ms = 0
		for value in grade_numbers: #Count the Ms
			if value == 2:
				no_of_Ms += 1

		if no_of_Ms == 3: #They got 3 Ms
			question_grade = 'M6'
			total_score = 6

		elif no_of_Ms == 2: #They got 2 Ms
			question_grade = 'M5'
			total_score = 5

		elif no_of_Ms == 1: #They got 1M
			if total_score >= 4: #They got at least M, A, A or M, A, A, A
				question_grade = 'A4'
				total_score = 4

			else: #They got M, A, or they got M
				question_grade = ncea_grade[total_score]

	else: #They got a mix of As and Ns
			question_grade = ncea_grade[total_score]
	

	return total_score, question_grade	


def calc_general_question_91171(q1a, q1b, q1c, q1d): #Calculate for Mechanics Paper. Need to tidy comments
	conversion_dict = {'N':0, 'A': 1, 'M': 2, 'E': 3, 'EE': 6}
	ncea_grade = ['N0', 'N1', 'N2', 'A3', 'A4', 'M5', 'M6', 'E7', 'E8']

	grade_numbers = [conversion_dict[q1a], 
	conversion_dict[q1b], 
	conversion_dict[q1c], 
	conversion_dict[q1d],
	]

	total_score = sum(grade_numbers)
	no_of_Es = 0
	no_of_Ms = 0
	no_of_As = 0
	for value in grade_numbers: #Count number of E's, M's, A's
		if value == 3:
			no_of_Es += 1
		elif value == 2:
			no_of_Ms += 1
		elif value == 1:
			no_of_As += 1

	if 6 in grade_numbers: #The got an EE grade
		if total_score > 8:
			question_grade = 'E8'
			total_score = 8 
		elif total_score >= 7:
			question_grade = 'E7'
			total_score = 7 
		else:
			question_grade = ncea_grade[total_score]

	elif 3 in grade_numbers: #They got at least one E grade

		if no_of_Es == 2: #They got 2 Es
			if total_score > 8:
				question_grade = 'E8'
				total_score = 8 
			elif total_score >= 7:
				question_grade = 'E7'
				total_score = 7 
			else:
				question_grade = ncea_grade[total_score]

		else: #They got 1 E. 
			if 2 in grade_numbers: #They got an E and an M
				if total_score >= 8: #They got at least an E, M, A
					question_grade = 'E7'
					total_score = 7
				elif total_score >= 6:
					question_grade = 'M6'
					total_score = 6
				else: #They only got an E, M
					question_grade = ncea_grade[total_score]
			elif total_score == 6: #They got E, A, A, A
				question_grade = 'M5'
				total_score = 5
			elif total_score == 5: #They got E, A, A 
				question_grade = 'A4'
				total_score = 4
			elif total_score == 4: #They got E, A, 
				question_grade = 'A3'
				total_score = 3
			else:	#The got an E only
				question_grade = ncea_grade[total_score]

	elif 2 in grade_numbers: #They got at least one M

		if no_of_Ms == 3: #They got 3 Ms
			question_grade = 'M6'
			total_score = 6

		elif no_of_Ms == 2: #They got 2 Ms
			question_grade = 'M5'
			total_score = 5

		elif no_of_Ms == 1: #They got 1M
			if total_score >= 4: #They got at least M, A, A or M, A, A, A
				question_grade = 'A4'
				total_score = 4

			else: #They got M, A, or they got M
				question_grade = ncea_grade[total_score]

	else: #They got a mix of As and Ns
			question_grade = ncea_grade[total_score]
	

	return total_score, question_grade	'''
