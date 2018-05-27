'''/////////////////////////////////////////////////////////////////
HEADER
#DEPENDENCIES
	Population_poa 
	sys
	matplotlib.pyplot

#FUNCTION AND DESCRIPTION
	Independent of age- this function just plots the population of 
	perth as a function of its distance from postcode 6000. 
	POA6000. 
////////////////////////////////////////////////////////////////////
#AUTHOR: RYAN MAY
#STUDENT ID: 19477774
#PUBLISHED: 26/05/2018
#CURTIN UNIVERISTY COMP1001 COURSE
////////////////////////////////////////////////////////////////////
FILES:
	../Shared_Python_moldules/Population_poa.py 			<python>
	../Processing_Data/POA_Distance_from_6000.csv			<csv>
	../Processing_Data/2016_Census_POA.csv					<csv>
OUTPUT FILES:
	Graphs/POPULATION_R_DIST.png 							<png/GRAPH>
	Graphs/POPULATION_R_RESTRICTEDDIST.png 					<png/GRAPH>
	Graphs/POPULATION_R_RESTRICTEDDISCATEGORISED.png 		<png/GRAPH>
/////////////////////////////////////////////////////////////////'''

import sys
sys.path.insert(0, '../Shared_Python_modules/')
from Population_poa import POPOFPOA  

import matplotlib.pyplot as plt

CENSUS_DATA_DIR = "../Processing_Data/2016_Census_POA.csv"

x = POPOFPOA(CENSUS_DATA_DIR)
POPULATION = x.processing()

DISTANCE_FILE = open('../Processing_Data/POA_Distance_from_6000.csv','r')
DISTANCE_A = (DISTANCE_FILE.read().split(','))
DISTANCE = []

for i in range(len(DISTANCE_A)-1):
	try:
		DISTANCE += [float(DISTANCE_A[i])]
	except:
		print("Index: ", i, "failed")

POP_TO_DIST = dict(zip(DISTANCE, POPULATION[0:-1:]))

'''
POPULATION BY DISTANCE
'''
DISTANCE_GRAPHING = sorted(DISTANCE)
POPULATION_GRAPHING = [POP_TO_DIST[DISTANCE_GRAPHING[i]] for i in range(len(DISTANCE))]

plt.style.use('ggplot')
plt.plot(DISTANCE_GRAPHING, \
		POPULATION_GRAPHING)
plt.title("POPULATION PER POSTCODE")
plt.xlabel("DISTANCE OF POSTCODE AS VECTOR FROM 6000")
plt.ylabel("POPULATION")
plt.savefig("Graphs/POPULATION_R_DIST.png")
plt.show()

'''
RESTRICTED POPULATION BY DISTANCE
'''
 
DISTANCE_GRAPHING = (sorted(DISTANCE))[0:300:1]
POPULATION_GRAPHING = [POP_TO_DIST[DISTANCE_GRAPHING[i]] for i in range(0,300)]

plt.style.use('ggplot')
plt.plot(DISTANCE_GRAPHING, \
		POPULATION_GRAPHING)
plt.title("POPULATION PER POSTCODE")
plt.xlabel("DISTANCE OF POSTCODE AS VECTOR FROM 6000")
plt.ylabel("POPULATION")
plt.savefig("Graphs/POPULATION_R_RESTRICTEDDIST.png")
plt.show()

'''
POPULATION PLOTTED (BAR) BY DISTANCE IN RINGS OF 5kms
'''

DISTANCE_GRAPHING = [DISTANCE_GRAPHING[i]-DISTANCE_GRAPHING[i]%5 for i in range(0,300)]
print(DISTANCE_GRAPHING)


DATA = [[DISTANCE_GRAPHING[i], float(POPULATION_GRAPHING[i])] for i in range(0,300)]

import itertools

def extract_key(v):
	return v[0]

DATA = sorted(DATA, key=extract_key)

result = [
	[k, [x[1] for x in g]]
	for k, g in itertools.groupby(DATA, extract_key)
]
print(result)

histogram_data = [sum(result[i][1]) for i in range(len(result))]

xdata = [0,5,10,15,20,25,30,35]

print(histogram_data)

plt.style.use('ggplot')
plt.bar(xdata, histogram_data, width=5.0)
plt.title("POPULATION PER POSTCODE")
plt.xlabel("DISTANCE OF POSTCODE AS VECTOR FROM 6000")
plt.ylabel("POPULATION")
plt.savefig("Graphs/POPULATION_R_RESTRICTEDDISCATEGORISED.png")
plt.show()

