'''///////////////////////////////////////////////////////////////// 
HEADER
#DEPENDENCIES
	Age_across_postcode 
	sys
	matplotlib.pyplot

#FUNCTION AND DESCRIPTION
	Simple script that looks for the population per postcode, 
	specifically concerning what proportion of the opopulation is 
	school-aged
////////////////////////////////////////////////////////////////////
#AUTHOR: RYAN MAY
#STUDENT ID: 19477774
#PUBLISHED: 26/05/2018
#CURTIN UNIVERISTY COMP1001 COURSE
////////////////////////////////////////////////////////////////////
FILES:
	../Processing_Data/postcodes.csv						<CSV>
	../Shared_Python_Modules/Age_across_postcode.py			<Python>
	../Processing_Data/2016_Census_POA.csv					<CSV>
OUTPUT FILES:
	/Graphs/POPULATION_R_RESTRICTEDPOA.png 					<png/GRAPH>
/////////////////////////////////////////////////////////////////'''
import sys
sys.path.insert(0, '../Shared_Python_modules/')
from Age_across_postcode import AGEACROSSPOSTCODE  
import matplotlib.pyplot as plt

CENSUS_DATA_DIR = "../Processing_Data/2016_Census_POA.csv"

def plot(POSTCODE, POPULATION, POPULATION_2):
	print(POSTCODE)
	print(POPULATION)

	plt.style.use('ggplot')
	plt.bar(POSTCODE, POPULATION_2, width = 1, color='red', label = '15 to 19')
	plt.bar(POSTCODE, POPULATION, width = 0.5, label = '4 to 14')
	plt.legend()
	plt.title("POPULATION PER POSTCODE")
	plt.xlabel("POSTODE OF RESIDENCY")
	plt.ylabel("POPULATION OF POSTCODE")
	plt.savefig("Graphs/POPULATION_R_RESTRICTEDPOA.png")
	plt.show()

##OPENING POSTCODE FILE
POSTCODE_FILE = open('../Processing_Data/postcodes.csv','r')
POSTCODE = (POSTCODE_FILE.read()).split('\n')[:-1:]
POSTCODE = [str(POSTCODE[i]) for i in range(len(POSTCODE))]
## OBTAINING POPULATION
x = AGEACROSSPOSTCODE(CENSUS_DATA_DIR)
TOTAL = [float(x.poa_pop_age('total')[1][i]) for i in range(len(POSTCODE))]
POPULATION = [float(x.poa_pop_age('5t14')[1][i]) for i in range(len(POSTCODE))]
POPULATION_2 = [float(x.poa_pop_age('15t19')[1][i]) for i in range(len(POSTCODE))]
print("15 to 19", sum(POPULATION_2))
print("4 to 14", sum(POPULATION))
print("School Age", sum(POPULATION_2)+sum(POPULATION))
print("Thats ", (sum(POPULATION_2)+sum(POPULATION))/sum(TOTAL) *100, "%")

#TWO GRAPHS
POSTCODE = POSTCODE[0:50:1]
POPULATION = POPULATION[0:50:1]
POPULATION_2 = POPULATION_2[0:50:1]
plot(POSTCODE, POPULATION, POPULATION_2)

POSTCODE = POSTCODE[0:30:1]
POPULATION = POPULATION[0:30:1]
POPULATION_2 = POPULATION_2[0:30:1]
plot(POSTCODE, POPULATION, POPULATION_2)
