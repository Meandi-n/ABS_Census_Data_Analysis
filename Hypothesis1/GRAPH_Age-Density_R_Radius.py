'''/////////////////////////////////////////////////////////////////
HEADER
#DEPENDENCIES
	Age_across_postcode 
	sys
	matplotlib.pyplot

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
	../Processing_Data/Bubble.csv 							<csv>
	../Processing_Data/POA_Distance_from_6000.csv			<csv>
	../Processing_Data/2016_Census_POA.csv					<csv>
OUTPUT FILES:
	/Graphs/POPULATION_R_DENSITYAGE.png 					<png/GRAPH>
/////////////////////////////////////////////////////////////////'''

import sys
sys.path.insert(0, '../Shared_Python_modules/')
from Age_across_postcode import AGEACROSSPOSTCODE  
import matplotlib.pyplot as plt

## AREA OF POSTCODES
AREA_FOBJ = open("../Processing_Data/Bubble.csv", 'r')
AREA_DATA = AREA_FOBJ.read().split(",")[0:50:1]


#DISTANCES OF POSTCODES FROM CITY CENTRE
DISTANCE_FILE = open('../Processing_Data/POA_Distance_from_6000.csv','r')
DISTANCE = (DISTANCE_FILE.read().split(','))[0:50:1]
DISTANCE = [float(DISTANCE[i]) - float(DISTANCE[i])%5 for i in range(len(DISTANCE))]

def FETCHPOP(DISTANCE, AREA_DATA, age):
	CENSUS_DATA_DIR = "../Processing_Data/2016_Census_POA.csv"

	x = AGEACROSSPOSTCODE(CENSUS_DATA_DIR)
	POPULATION = x.poa_pop_age(age)[1]

	for i in range(len(AREA_DATA)):
		print("_________")
		print("Area:", AREA_DATA[i])
		print("Pop: ", POPULATION[i])

	POP_DENSITY = []
	POP_DENSITY = POP_DENSITY + [float(POPULATION[i])/float(AREA_DATA[i]) for i in range(len(AREA_DATA))]

	
	DATA = [[DISTANCE[i], POP_DENSITY[i]] for i in range(len(DISTANCE))]

	import itertools

	def extract_key(v):
		return v[0]

	DATA = sorted(DATA, key=extract_key)

	result = [
		[k, [x[1] for x in g]]
		for k, g in itertools.groupby(DATA, extract_key)
	]
	DATA=result

	for i in range(len(DATA)):
		DATA[i][1]=(sum(DATA[i][1]))

	for item in range(len(DATA)):
		print(DATA[item])

	return DATA[0:9:1]

DATA_T 		= FETCHPOP(DISTANCE, AREA_DATA, 'total')
DATA_04 	= FETCHPOP(DISTANCE, AREA_DATA, '0t4')
DATA_514	= FETCHPOP(DISTANCE, AREA_DATA, '5t14')
DATA_1519	= FETCHPOP(DISTANCE, AREA_DATA, '15t19')
DATA_2024	= FETCHPOP(DISTANCE, AREA_DATA, '20t24')
DATA_2534	= FETCHPOP(DISTANCE, AREA_DATA, '25t34')
DATA_3544	= FETCHPOP(DISTANCE, AREA_DATA, '35t44')
DATA_4554	= FETCHPOP(DISTANCE, AREA_DATA, '45t54')
DATA_5564	= FETCHPOP(DISTANCE, AREA_DATA, '55t64')
DATA_6574	= FETCHPOP(DISTANCE, AREA_DATA, '65t74')
DATA_7584	= FETCHPOP(DISTANCE, AREA_DATA, '75t84')
DATA_O85	= FETCHPOP(DISTANCE, AREA_DATA, 'o85')

X_AXIS = [DATA_T[i][0] for i in range(len(DATA_T))]

Y_AXIS_04 	= [DATA_04[i][1] for i in range(len(DATA_T))]
Y_AXIS_514 	= [DATA_514[i][1] for i in range(len(DATA_T))]
Y_AXIS_1519 = [DATA_1519[i][1] for i in range(len(DATA_T))]
Y_AXIS_2024 = [DATA_2024[i][1] for i in range(len(DATA_T))]
Y_AXIS_2534 = [DATA_2534[i][1] for i in range(len(DATA_T))]
Y_AXIS_3544 = [DATA_3544[i][1] for i in range(len(DATA_T))]
Y_AXIS_4554 = [DATA_4554[i][1] for i in range(len(DATA_T))]
Y_AXIS_5564 = [DATA_5564[i][1] for i in range(len(DATA_T))]
Y_AXIS_6574 = [DATA_6574[i][1] for i in range(len(DATA_T))]
Y_AXIS_7584 = [DATA_7584[i][1] for i in range(len(DATA_T))]
Y_AXIS_O85	= [DATA_O85[i][1] for i in range(len(DATA_T))]


plt.style.use('ggplot')

plt.plot(X_AXIS, Y_AXIS_04, label='0 to 4')
plt.plot(X_AXIS, Y_AXIS_514, label='5 to 14')
plt.plot(X_AXIS, Y_AXIS_1519, label='15 to 19')
plt.plot(X_AXIS, Y_AXIS_2024, label='20 to 24')
plt.plot(X_AXIS, Y_AXIS_2534, label='25 to 34')
plt.plot(X_AXIS, Y_AXIS_3544, label='35 to 44')
plt.plot(X_AXIS, Y_AXIS_4554, label='45 to 54')
plt.plot(X_AXIS, Y_AXIS_5564, label='55 to 64')
plt.plot(X_AXIS, Y_AXIS_6574, label='65 to 74')
plt.plot(X_AXIS, Y_AXIS_7584, label='75 to 84')
plt.plot(X_AXIS, Y_AXIS_O85, label='Over 85')

plt.xlabel("DISTANCE FROM POA6000")
plt.ylabel("POPULATION DENSITY")
plt.legend()
plt.title("POPULATION DENSITY AS A FUNCTION OF DISTANCE FROM CITY CENTRE")
plt.savefig("Graphs/POPULATION_R_DENSITYAGE.png")
plt.show()