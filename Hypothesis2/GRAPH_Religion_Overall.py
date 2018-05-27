'''///////////////////////////////////////////////////////////////// 
HEADER
#DEPENDENCIES
	religious_Beliefs 
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
	../Shared_Python_Modules/religious_Beliefs.py			<Python>
OUTPUT FILES:
	/Graphs/RELIGION_R_OVERALL.png 							<png/GRAPH>
/////////////////////////////////////////////////////////////////'''
import sys
sys.path.insert(0, '../Shared_Python_modules/')
from relgious_Beliefs import RELIGIOUSBELIEFS_R_POSTCODE
import matplotlib.pyplot as plt

x = RELIGIOUSBELIEFS_R_POSTCODE()
associations = x.associations
inv_associations = {v: k for k, v in associations.items()}


count = []

for i in range(3,(len(inv_associations)+1)*3, 3):
	count = count + [x.religious_count(inv_associations[i])]

X_AXIS = [1*i for i in range(len(inv_associations))]
X_LAB = [inv_associations[i] for i in range(3,(len(inv_associations)+1)*3,3)]

print(len(X_AXIS), X_AXIS)
print(len(count), count)

plt.style.use('ggplot')
plt.title("RELIGIOUS BELIEF OVER PERTH POPULATIONS")
plt.ylabel("POPULATION (1000s)")
plt.xlabel("BELIEF")
for i in range(len(count)):
	plt.bar(X_AXIS[i], count[i]/1000)
	label = (count[i]/sum(count)*100)-(count[i]/sum(count)*100)%1
	if label > 0:
		plt.text(X_AXIS[i], (count[i]+5000)/1000, '='+str(label)+'%', fontsize='6')
plt.xticks(X_AXIS, X_LAB, rotation=80, fontsize='8')
plt.savefig("Graphs/RELIGION_R_OVERALL.png")
plt.show()