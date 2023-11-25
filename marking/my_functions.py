def calc_general_question(q1a, q1b, q1c, q1d):
	conversion_dict = {'N':0, 'A': 1, 'M': 2, 'E': 3}
	ncea_grade = ['N0', 'N1', 'N2', 'A3', 'A4', 'M5', 'M6', 'E7', 'E8']

	grade_numbers = [conversion_dict[q1a], 
	conversion_dict[q1b], 
	conversion_dict[q1c], 
	conversion_dict[q1d],
	]

	total_score = sum(grade_numbers)
	if total_score ==7 and 3 not in grade_numbers: #Check if its an M6 as no Es
		question_grade = 'M6'
		total_score = 6
	elif total_score ==8: #See if its an E7 or E8, by seeing if there are two E scores
		for i, value in enumerate(grade_numbers[:-1]): 
			if value == 3 and 3 in grade_numbers[i+1:]:
				question_grade = 'E8'
				break
		else:
			question_grade = 'E7'
			total_score = 7
	elif total_score > 8:
		question_grade = 'E8'
		total_score = 8
	else:
		question_grade = ncea_grade[total_score]
	

	return total_score, question_grade

def calc_q1(q1a, q1b, q1c, q1d):
	conversion_dict = {'N':0, 'A': 1, 'M': 2, 'E': 3}
	ncea_grade = ['N0', 'N1', 'N2', 'A3', 'A4', 'M5', 'M6', 'E7', 'E8']

	grade_numbers = [conversion_dict[q1a], 
	conversion_dict[q1b], 
	conversion_dict[q1c], 
	conversion_dict[q1d],
	]

	total_score = sum(grade_numbers)
	if total_score ==7 and 3 not in grade_numbers: #Check if its an M6 as no Es
		question_grade = 'M6'
		total_score = 6
	elif total_score ==8: #See if its an E7 or E8, by seeing if there are two E scores
		for i, value in enumerate(grade_numbers[:-1]): 
			if value == 3 and 3 in grade_numbers[i+1:]:
				question_grade = 'E8'
				break
		else:
			question_grade = 'E7'
			total_score = 7
	elif total_score > 8:
		question_grade = 'E8'
		total_score = 8
	else:
		question_grade = ncea_grade[total_score]
	

	return total_score, question_grade

def calc_q2(q2a, q2b, q2c, q2d):
	conversion_dict = {'N':0, 'A': 1, 'M': 2, 'E': 3}
	ncea_grade = ['N0', 'N1', 'N2', 'A3', 'A4', 'M5', 'M6', 'E7', 'E8']

	grade_numbers = [conversion_dict[q2a], 
	conversion_dict[q2b], 
	conversion_dict[q2c], 
	conversion_dict[q2d],
	]

	total_score = sum(grade_numbers)
	if total_score ==7 and 3 not in grade_numbers:
		question_grade = 'M6'
		total_score = 6
	elif total_score > 8:
		question_grade = 'E8'
		total_score = 8
	else:
		question_grade = ncea_grade[total_score]
	

	return total_score, question_grade

def calc_q3(q3a, q3b, q3c, q3d):
	conversion_dict = {'N':0, 'A': 1, 'M': 2, 'E': 3}
	ncea_grade = ['N0', 'N1', 'N2', 'A3', 'A4', 'M5', 'M6', 'E7', 'E8']

	grade_numbers = [conversion_dict[q3a], 
	conversion_dict[q3b], 
	conversion_dict[q3c], 
	conversion_dict[q3d],
	]

	total_score = sum(grade_numbers)
	if total_score ==7 and 3 not in grade_numbers:
		question_grade = 'M6'
		total_score = 6
	elif total_score > 8:
		question_grade = 'E8'
		total_score = 8
	else:
		question_grade = ncea_grade[total_score]
	

	return total_score, question_grade


def get_letter_grades(current_paper):
	q1_total_score, q1_question_grade = calc_general_question(current_paper.q1a,
		current_paper.q1b,
		current_paper.q1c,
		current_paper.q1d)

	q2_total_score, q2_question_grade = calc_general_question(current_paper.q2a,
		current_paper.q2b,
		current_paper.q2c,
		current_paper.q2d)

	q3_total_score, q3_question_grade = calc_general_question(current_paper.q3a,
		current_paper.q3b,
		current_paper.q3c,
		current_paper.q3d)

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

			#totals

			total_papers = count_N+count_A+count_M+count_E

			average_q = (count_A + 2*count_M+3*count_E)/total_papers

			percentages = [round(count_N/total_papers*100), 
			round(count_A/total_papers*100),
			round(count_M/total_papers*100),
			round(count_E/total_papers*100),
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






