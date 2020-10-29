from random import randint
import random
print('Enter students last names with space bar as a separator')
last_names=list(input().split(sep=' '))
#print(last_names)
number_of_students=len(last_names) 
print('Enter students subjects with space bar as a separator')
subjects=list(input().split(sep=' '))
amount_of_subjects=len(subjects) #количество оценок каждого студента


spisok=[]
for i in range(number_of_students):
	spisok.append(random.sample((0,2,3,4,5), amount_of_subjects))

slovar={k:v for (k,v) in zip(last_names,spisok)}
for person in slovar:
	print(person, slovar[person])


def amount_of_absence_in_a_group(sub):
	kol_neyavok=0 
	st=[]
	global amount_of_subjects
	global slovar
	for (key,value) in slovar.items():
		if value[sub]==0:
			kol_neyavok+=1
			st.append(key)
	print('Amount of students absent: ',kol_neyavok, st)

def amount_of_unacceptable_marks(sub):
	kol_neud=0 
	st=[]
	global amount_of_subjects
	global slovar
	for (key,value) in slovar.items():
		if value[sub]==2:
			kol_neud+=1
			st.append(key)
	print('Amount of students with unacceptable marks: ',kol_neud, st)

def amount_of_acceptable_marks(sub):
	kol_ud=0 
	st=[]
	global amount_of_subjects
	global slovar
	for (key,value) in slovar.items():
		if value[sub]==3:
			kol_ud+=1
			st.append(key)
	print('Amount of students with acceptable marks: ',kol_ud, st)

def amount_of_good_marks(sub):
	kol_good=0 
	st=[]
	global amount_of_subjects
	global slovar
	for (key,value) in slovar.items():
		if value[sub]==4:
			kol_good+=1
			st.append(key)
	print('Amount of students with good marks: ',kol_good, st)

def amount_of_excellent_marks(sub):
	kol_excellent=0 
	st=[]
	global amount_of_subjects
	global slovar
	for (key,value) in slovar.items():
		if value[sub]==5:
			kol_excellent+=1
			st.append(key)
	print('Amount of students with excellent mark: ',kol_excellent, st)

print('Enter subject to check')
needed_subject=str(input())
while needed_subject!='':
	i_n_s=subjects.index(needed_subject)
	amount_of_absence_in_a_group(i_n_s)
	amount_of_unacceptable_marks(i_n_s)
	amount_of_acceptable_marks(i_n_s)
	amount_of_good_marks(i_n_s)
	amount_of_excellent_marks(i_n_s)
	needed_subject=str(input())
	

'''
Markovich Voroshilov Vyrodov Sibilev Antonyuk Kazmin
'''