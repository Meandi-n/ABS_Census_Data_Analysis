'''/////////////////////////////////////////////////////////////////
HEADER
#DEPENDENCIES
	Age_across_postcode 
	sys
	matplotlib.pyplot

#FUNCTION AND DESCRIPTION
	This is a script that reads the religions of people (2006), from
	the abs census, and then continues to plot the prominence of the 
	religion in a pie-chart. 
////////////////////////////////////////////////////////////////////
#AUTHOR: RYAN MAY
#STUDENT ID: 19477774
#PUBLISHED: 26/05/2018
#CURTIN UNIVERISTY COMP1001 COURSE
////////////////////////////////////////////////////////////////////
FILES:
	../Processing_Data/2006_Religious_data.csv				<CSV>
OUTPUT FILES:
	/Graphs/PIE_RELIGION_PERTH_2006.png 					<png/GRAPH>
/////////////////////////////////////////////////////////////////'''

import re
import matplotlib.pyplot as plt

file_obj = open('../Processing_Data/2006/2006_Religious_data.csv','r')
file_data = file_obj.readlines()
i = 0
while 1:
	if i > len(file_data):
		break
	exam = str(file_data[i])
	
	if len(re.findall(r"Total", exam)) > 0:
		file_data.pop(i)

	i += 1


data =[]
data = data + [file_data[i].split(';') for i in range(len(file_data))]


LABEL = [[data[i][0]] for i in range(len(data))]


POP = [[''.join((str(data[i][3])[0:-1]).split(','))] for i in range(len(data))]

i=0
while 1:
	if i > len(LABEL):
		break
	if POP[i] == ['']:
		LABEL.pop(i)
		POP.pop(i)
	i += 1

for i in range(len(POP)):
	print(LABEL[i], " ", POP[i])

plt.rcParams['font.size'] = 5


#colors
colors = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]

fig1, ax1 = plt.subplots()
ax1.pie(POP, colors = colors, labels=LABEL, autopct='%1.1f%%', startangle=20, pctdistance=0.45, labeldistance=1)

	
#draw circle
centre_circle = plt.Circle((0,0),0.50,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
plt.tight_layout()
plt.savefig('Graphs/PIE_RELIGION_PERTH_2006.png')
plt.show()