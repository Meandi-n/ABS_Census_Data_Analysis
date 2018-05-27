'''///////////////////////////////////////////////////////////////// 
HEADER
#DEPENDENCIES
	religious_Beliefs 
	sys
	matplotlib.pyplot

#FUNCTION AND DESCRIPTION
	This is a simple programme that looks at religious beleifs across the
	population, and produces a range of line plots, bar charts
	and pie charts to map out the population
	the population examined here is the year 2016. 
////////////////////////////////////////////////////////////////////
#AUTHOR: RYAN MAY
#STUDENT ID: 19477774
#PUBLISHED: 26/05/2018
#CURTIN UNIVERISTY COMP1001 COURSE
////////////////////////////////////////////////////////////////////
FILES:
	../Processing_Data/postcodes.csv						<CSV>
	../Shared_Python_Modiles/religious_Beliefs.py			<Python>
	../Processing_Data/2016_Census_POA.csv					<CSV>
	../Processing_Data/2011_Census_POA.csv					<CSV>
OUTPUT FILES:
	/Graphs/PIE_RELIGION_PERTH.png 							<png/GRAPH>
	/Graphs/RELIGION_R_POA 									<png/GRAPH>
	/Graphs/ATHEISM_R_POA 									<png/GRAPH>
/////////////////////////////////////////////////////////////////'''
import sys
sys.path.insert(0, '../Shared_Python_modules/')
from relgious_Beliefs import RELIGIOUSBELIEFS_R_POSTCODE
import matplotlib.pyplot as plt
plt.style.use('ggplot')

### SETTING VARIABLES

x = RELIGIOUSBELIEFS_R_POSTCODE()

associations = x.associations
inv_associations = {v: k for k, v in associations.items()}

RELIGIONS = []

### DATA OBTAINING

#OBTAINING BY POSTCODE POPULATIONS OF 81 DIFFERING RELIGIONS
for a in range(3, 60, 3):
	RELIGIONS = RELIGIONS + [x.religious_count_poa(inv_associations[a])]
for a in range(69, 96, 3):
	RELIGIONS = RELIGIONS + [x.religious_count_poa(inv_associations[a])]
#for b in range(69, 96, 3):
#	RELIGIONS = RELIGIONS + [x.religious_count_poa(inv_associations[b])]

print(len(RELIGIONS))


##OPENING POSTCODE FILE
POSTCODE_FILE = open('../Processing_Data/postcodes.csv','r')
POSTCODE = (POSTCODE_FILE.read()).split('\n')[:-2:]
POSTCODE = [str(POSTCODE[i]) for i in range(len(POSTCODE))]

###FUNCTIONS

def RELIGION_PLOT(RELIGION_INDEX):
	DATA = [[POSTCODE[i],RELIGIONS[RELIGION_INDEX][i]] for i in range(len(POSTCODE))]

	X_AXIS = [DATA[i][0] for i in range(len(DATA))]
	Y_AXIS = [int(DATA[i][1]) for i in range(len(DATA))]

	plt.plot(X_AXIS[0:50], Y_AXIS[0:50], label = inv_associations[(RELIGION_INDEX+1)*3])

def RELIGION_COUNT(x):
	REGOT = []
	LABEL = []
	for a in range(3, 60, 3):
		REGOT = REGOT + [x.religious_count(inv_associations[a])]
		LABEL = LABEL + [inv_associations[a]]
	for a in range(69,96,3):
		REGOT = REGOT + [x.religious_count(inv_associations[a])]
		LABEL = LABEL + [inv_associations[a]]
	
	SUM_REG = sum(REGOT)
	REGOT = [REGOT[i]/SUM_REG*100 for i in range(len(REGOT))]
	
	# making pie chart from data
	# Pie chart, where the slices will be ordered and plotted counter-clockwise:
	# Pie chart
	labels = LABEL
	sizes = REGOT

	plt.rcParams['font.size'] = 5

	#colors
	colors = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]

	fig1, ax1 = plt.subplots()

	ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=20, pctdistance=0.45, labeldistance=1)

	
	#draw circle
	centre_circle = plt.Circle((0,0),0.50,fc='white')
	fig = plt.gcf()
	fig.gca().add_artist(centre_circle)

	# Equal aspect ratio ensures that pie is drawn as a circle
	ax1.axis('equal')
	plt.tight_layout()
	plt.savefig('Graphs/PIE_RELIGION_PERTH.png')
	plt.show()

def ATHEISM_DATA(RELIGION_INDEX):
	DATA = [[POSTCODE[i],RELIGIONS[RELIGION_INDEX][i]] for i in range(len(POSTCODE))]

	X_AXIS = [DATA[i][0] for i in range(len(DATA))]
	Y_AXIS = [int(DATA[i][1]) for i in range(len(DATA))]

	return Y_AXIS

def THEISM_COUNT(POSTCODE, DATA_Y):
	# returns an array of all religious people per postcode
	for i in range(len(RELIGIONS)-6):
		Y_AXIS = ATHEISM_DATA(i)
		for a in range(len(DATA_Y)):
			DATA_Y[a] += Y_AXIS[a]
	return DATA_Y

def ATHEISM_COUNT(RELIGIONS, DATA_Y_A):
	for i in range(len(RELIGIONS)-5, len(RELIGIONS)):
		Y_AXIS = ATHEISM_DATA(i)
		for a in range(len(DATA_Y_A)):
			DATA_Y_A[a] += Y_AXIS[a]
	return DATA_Y_A

def PLOTTING_ATHEISM(POSTCODE, DATA_Y):
	plt.bar(POSTCODE[0:50], DATA_Y[0:50], color = 'r', label = 'THEISTIC IN SOME MANNER')
	plt.bar(POSTCODE[0:50], DATA_Y_A[0:50], color='g', bottom=DATA_Y[0:50], label='ATHEISTIC')

def MATPLOTLIBSETUP(plt, title, x, y, savefig):
	plt.legend(fontsize=6)
	plt.title(title)
	plt.ylabel(y)
	plt.xlabel(x)
	plt.savefig(savefig)
	plt.show()

for i in range(len(RELIGIONS)):
	print(i)
	RELIGION_PLOT(i)

MATPLOTLIBSETUP(plt, "Religion as a function of postalcode", \
				"Postalcode", "Population", 'Graphs/RELIGION_R_POA.png')


DATA_Y = [0 for i in range(len(POSTCODE))]
DATA_Y_A = [0 for i in range(len(POSTCODE))]

DATA_Y = THEISM_COUNT(POSTCODE, DATA_Y)
DATA_Y_A = ATHEISM_COUNT(RELIGIONS, DATA_Y_A)

PLOTTING_ATHEISM(POSTCODE, DATA_Y)

MATPLOTLIBSETUP(plt, "Atheism as a function of postalcode", \
				"Postalcode", "Population", 'Graphs/ATHEISM_R_POA.png')

RELIGION_COUNT(x)