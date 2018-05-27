'''/////////////////////////////////////////////////////////////////
HEADER
#DEPENDENCIES
	Age_across_postcode 
	sys
	matplotlib.pyplot
	itertools
	numpy

#FUNCTION AND DESCRIPTION
	this is a simple function that fethes the population and age of 
	postcodes and then plots it as a function of population density 
	of ages to distance from postcode 6000
////////////////////////////////////////////////////////////////////
#AUTHOR: RYAN MAY
#STUDENT ID: 19477774
#PUBLISHED: 26/05/2018
#CURTIN UNIVERISTY COMP1001 COURSE
////////////////////////////////////////////////////////////////////
FILES:
	../Shared_Python_moldules/Age_across_postcode.py 		<python>
	../Processing_Data/POA_Distance_from_6000.csv 			<csv>
	../Processing_Data/2016_Census_POA.csv					<csv>
OUTPUT FILES:
	Graphs/POPULATION_R_AGEDRADIALCATEGORISEDRESTRICTED.png <png/GRAPH>
/////////////////////////////////////////////////////////////////'''

import sys
sys.path.insert(0, '../Shared_Python_modules/')
from Age_across_postcode import AGEACROSSPOSTCODE  
import matplotlib.pyplot as plt
import itertools
import numpy as np

def extract_key(v):
	return v[0]

def AGE_DATA(AGE):
	# Getting census data from class
	CENSUS_DATA_DIR = "../Processing_Data/2016_Census_POA.csv"
	x = AGEACROSSPOSTCODE(CENSUS_DATA_DIR)
	#getting population of "AGE" paramater per postcode
	POPULATION = x.poa_pop_age(AGE)
	#getting distance of each postcode from 6000, and storing it as array
	DISTANCE_FILE = open('../Processing_Data/POA_Distance_from_6000.csv','r')
	DISTANCE = (DISTANCE_FILE.read().split(','))
	#this just processes the population array (2D) to make the distance in an interval of 5 kms. A - A%5 = closest multiple of A to 5
	for i in range(len(POPULATION[0])):
		POPULATION[0][i] = str(float(DISTANCE[i])-float(DISTANCE[i])%5)
		#this line just turns the population (actual pop) to a float to make the following code a little easier. 
		POPULATION[1][i] = float(POPULATION[1][i])
	#defining list (data) that refornats POPULATION array into better dimensions for processing (may be made redundant with tweaking)
	data = []
	data = data + [[(POPULATION[0][i]), (POPULATION[1][i])] for i in range(len(POPULATION[0]))]
	#sort that data :)
	data = sorted(data, key=extract_key)
	#now we make a restult array -- the point of this array is that we want to sort the data in increasing distance WITHOUT losing data assocations
	#within the 2D array between distance and population. 
	result = [
		[k, [x[1] for x in g]]
		for k, g in itertools.groupby(data, extract_key)
	]
	#we then reformat it
	RESULT = [\
				[float(sum(result[i][1])), \
			  	float(result[i][0])] \
			 	for i in range(len(result))\
			 ]
	#and sort it BY COLUMNS without loosing 2D data associations
	RESULT = sorted(RESULT, key=lambda x: x[1])
	#return that 2D array
	return RESULT

def plt_age():

	#initate arrays of each age, to plot with matplotlib. 
	X_AXIS_T 	= [AGE_DATA('total')[i][1] for i in range(len(AGE_DATA('total')))]
	#Y_AXIS_T 	= [AGE_DATA('total')[i][0] for i in range(len(AGE_DATA('total')))]
	###
	Y_AXIS_04	= [AGE_DATA('0t4')[i][0] for i in range(len(AGE_DATA('0t4')))]
	###
	Y_AXIS_514 	= [AGE_DATA('5t14')[i][0] for i in range(len(AGE_DATA('5t14')))]
	###
	Y_AXIS_1519 = [AGE_DATA('15t19')[i][0] for i in range(len(AGE_DATA('15t19')))]
	###
	Y_AXIS_2024 = [AGE_DATA('20t24')[i][0] for i in range(len(AGE_DATA('20t24')))]
	###
	Y_AXIS_2534 = [AGE_DATA('25t34')[i][0] for i in range(len(AGE_DATA('25t34')))]
	###
	Y_AXIS_3544 = [AGE_DATA('35t44')[i][0] for i in range(len(AGE_DATA('35t44')))]
	###
	Y_AXIS_4554 = [AGE_DATA('45t54')[i][0] for i in range(len(AGE_DATA('45t54')))]
	###
	Y_AXIS_5564 = [AGE_DATA('55t64')[i][0] for i in range(len(AGE_DATA('55t64')))]
	###
	Y_AXIS_6574 = [AGE_DATA('65t74')[i][0] for i in range(len(AGE_DATA('65t74')))]
	###
	Y_AXIS_7584 = [AGE_DATA('75t84')[i][0] for i in range(len(AGE_DATA('75t84')))]
	###
	Y_AXIS_85 = [AGE_DATA('o85')[i][0] for i in range(len(AGE_DATA('o85')))]

	plt.style.use('ggplot')
	plt.title("POPULATION PER POSTCODE")
	plt.xlabel("DISTANCE OF POSTCODE AS VECTOR FROM 6000")
	plt.ylabel("POPULATION")

	plt.plot(	X_AXIS_T, Y_AXIS_04, label = '0 to 4')
	plt.plot(	X_AXIS_T, Y_AXIS_514, label = '5 to 14')
	plt.plot(	X_AXIS_T, Y_AXIS_1519, label = '15 to 19')
	plt.plot(	X_AXIS_T, Y_AXIS_2024, label = '20 to 24')
	plt.plot(	X_AXIS_T, Y_AXIS_2534, label = '25 to 34')
	plt.plot(	X_AXIS_T, Y_AXIS_3544, label = '35 to 44')
	plt.plot(	X_AXIS_T, Y_AXIS_4554, label = '45 to 54')
	plt.plot(	X_AXIS_T, Y_AXIS_5564, label = '55 to 64')
	plt.plot(	X_AXIS_T, Y_AXIS_6574, label = '65 to 74')
	plt.plot(	X_AXIS_T, Y_AXIS_7584, label = '75 to 84')
	plt.plot(	X_AXIS_T, Y_AXIS_85, label = 'Over 85')

	plt.legend()
	plt.savefig("Graphs/POPULATION_R_AGEDRADIALCATEGORISED.png")
	plt.show()

	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_04[0:10:1], label = '0 to 4')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_514[0:10:1], label = '5 to 14')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_1519[0:10:1], label = '15 to 19')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_2024[0:10:1], label = '20 to 24')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_2534[0:10:1], label = '25 to 34')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_3544[0:10:1], label = '35 to 44')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_4554[0:10:1], label = '45 to 54')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_5564[0:10:1], label = '55 to 64')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_6574[0:10:1], label = '65 to 74')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_7584[0:10:1], label = '75 to 84')
	plt.plot(	X_AXIS_T[0:10:1], Y_AXIS_85[0:10:1], label = 'Over 85')

	plt.legend()
	plt.savefig("Graphs/POPULATION_R_AGEDRADIALCATEGORISEDRESTRICTED.png")
	plt.show()

if __name__ == '__main__':
	plt_age()