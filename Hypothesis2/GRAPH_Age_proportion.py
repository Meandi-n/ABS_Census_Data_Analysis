'''///////////////////////////////////////////////////////////////// 
HEADER
#DEPENDENCIES
	Age_across_postcode 
	sys
	matplotlib.pyplot

#FUNCTION AND DESCRIPTION
	This is a simple programme that creates a plot of proportion of
	particular ages brackets from the year 2011 to 2016. This age 
	bracket is graphed as a bar-plot with coloured sections 
	proportionate to populations. 
////////////////////////////////////////////////////////////////////
#AUTHOR: RYAN MAY
#STUDENT ID: 19477774
#PUBLISHED: 26/05/2018
#CURTIN UNIVERISTY COMP1001 COURSE
////////////////////////////////////////////////////////////////////
FILES:
	../Processing_Data/postcodes.csv						<CSV>
	../Shared_Python_Modiles/Age_across_postcode.py			<Python>
	../Processing_Data/2016_Census_POA.csv					<CSV>
	../Processing_Data/2011_Census_POA.csv					<CSV>
OUTPUT FILES:
	/Graphs/POPULATION_R_AGE_PROPORTION.png 				<png/GRAPH>
/////////////////////////////////////////////////////////////////'''

import sys
sys.path.insert(0, '../Shared_Python_modules/')
from Age_across_postcode import AGEACROSSPOSTCODE  
import matplotlib.pyplot as plt

##OPENING POSTCODE FILE
POSTCODE_FILE = open('../Processing_Data/postcodes.csv','r')
POSTCODE = (POSTCODE_FILE.read()).split('\n')[:-1:]
POSTCODE = [str(POSTCODE[i]) for i in range(len(POSTCODE))]



def POP_DATA(CENSUS_DATA_DIR):
	INDEX = {
	0:'total',1:'0t4',2:'5t14',3:'15t19',4:'20t24',5:'25t34', 
	6:'35t44',7:'45t54',8:'55t64',9:'65t74',10:'75t84',11:'o85'}
	POP = [0,0,0,0,0,0,0,0,0,0,0,0]
	FILE_OBJ = open(CENSUS_DATA_DIR, 'r').readlines()
	DATA_NUMERATOR = len(FILE_OBJ)-1
	x = AGEACROSSPOSTCODE(CENSUS_DATA_DIR)
	TOTAL = sum([float(x.poa_pop_age('total')[1][i]) for i in range((DATA_NUMERATOR))])
	print("TOTAL POP: ",TOTAL)
	for a in range(1,12):
		POP[a] = sum([float(x.poa_pop_age(INDEX[a])[1][i]) for i in range((DATA_NUMERATOR))])/TOTAL*100
		print("\tPOP[a]: ", POP[a], "%" )
	print("\t\nTOTAL: ", sum(POP), "%")
	
	return POP

POP_2016 = POP_DATA("../Processing_Data/2016_Census_POA.csv")
POP_2011 = POP_DATA("../Processing_Data/2011_Census_POA.csv")

print(POP_2016)
print(POP_2011)


plt.style.use('ggplot')

for i in range(len(POP_2016)):
	try:
		print(POP_2016[i]+POP_2016[i-1])
	except:
		print('0')


def plotting(POP, index):
	INDEX = {
	0:'total',1:'0t4',  2:'5t14', 3:'15t19',4:'20t24', 5:'25t34', 
	6:'35t44',7:'45t54',8:'55t64',9:'65t74',10:'75t84',11:'o85'}
	COLOUR = {
	0: '#FECBBF', 1: '#FD8368', 2:  '#FC3003', 3:  '#971D02', 
	4: '#BFD0FF', 5: '#5884FE', 6:  '#0140EF', 7:  '#012589', 
	8: '#A9D86E', 9: '#77B22F', 10: '#77B26F', 11: '#77B22F'
	}

	w=0.5

	plt.bar(index, POP[0], bottom=0, width=w, align='edge', color = COLOUR[0])
	for i in range(1,len(POP)):
		
		plt.bar(index, POP[i], bottom=sum([POP[a] for a in range(i)]), \
			width=w, align='edge', color = COLOUR[i], label=str(INDEX[i]))

		x = 0.1 + int(index)

		label = str(int(POP[i]))  + "%  " + str(INDEX[i])

		if i != len(POP)-1: y = POP[i]+sum([POP[a] for a in range(i)])-3
		else: y = -100
			
		plt.text(x, y, label, ha='center', va='baseline')

		print("LIVE DATA:")
		print("\t POP[", str(INDEX[i]), "] =", str(POP[i]))
	
	print(sum(POP))
	return plt

plt = plotting(POP_2016, '1')
plt = plotting(POP_2011, '0')

plt.title("POPULATION AGE PROPOTION 2011 to 2016")
plt.ylabel("% PROPOTION")
plt.xlabel("CENSUS YEAR (ABS)")
plt.xticks([0.25,1.25], ['2011', '2016'])
plt.savefig("Graphs/POPULATION_R_AGE_PROPORTION.png")
plt.show()
