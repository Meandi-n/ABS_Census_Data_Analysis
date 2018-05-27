'''/////////////////////////////////////////////////////////////////
HEADER:
#DEPENDENCIES
	Population_poa
	sys
	matplotlib.pyplot

#FUNCTION AND DESCRIPTION
	this is a simple function that fethes the population and age of 
	postcodes and then plots it as a function of postcode address. 
	this does not take distance or population density into account
////////////////////////////////////////////////////////////////////
#AUTHOR: RYAN MAY
#STUDENT ID: 19477774
#PUBLISHED: 26/05/2018
#CURTIN UNIVERISTY COMP1001 COURSE
////////////////////////////////////////////////////////////////////
FILES: 
	../Shared_Python_moldules/Population_poa.py             <python>
	../Processing_Data/2016_Census_POA.csv					<csv>
	../Processing_Data/postcodes.csv						<csv>
OUTPUT FILES:	
	Graphs/POPULATION_R_POA.png 							<png/GRAPH>
/////////////////////////////////////////////////////////////////'''

import sys
sys.path.insert(0, '../Shared_Python_modules/')
from Population_poa import POPOFPOA  
import matplotlib.pyplot as plt

CENSUS_DATA_DIR = "../Processing_Data/2016_Census_POA.csv"

x = POPOFPOA(CENSUS_DATA_DIR)
POPULATION = x.processing()

POSTCODE_FILE = open('../Processing_Data/postcodes.csv','r')
POSTCODE = (POSTCODE_FILE.read()).split('\n')[:-1:]

plt.style.use('ggplot')
plt.plot(POSTCODE, POPULATION)
plt.title("POPULATION PER POSTCODE")
plt.xlabel("POSTODE OF RESIDENCY")
plt.ylabel("POPULATION OF POSTCODE")
plt.savefig("Graphs/POPULATION_R_POA.png")
plt.show()

