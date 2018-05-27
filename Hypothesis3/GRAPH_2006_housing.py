import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
plt.style.use('ggplot')

def DATARETRIEVAL(CSV):
	file_obj = open(CSV)
	file_data = file_obj.readlines()
	graph_data =  [file_data[i].strip().split(';') for i in range(len(file_data))]

	i=0
	while 1:
		if i > len(graph_data)-1:
			break
		if graph_data[i][0] == '':
			graph_data.pop(i)
		if graph_data[i][2] == '':
			graph_data.pop(i)
		i += 1

	return graph_data

def PLOTTING_SMOOTH(INDEX, DATA):
	f = interp1d(INDEX, DATA, kind='quadratic')
	x_int = np.linspace(1,5,1000)
	y_int = f(x_int)
	plt.plot(x_int, y_int, 'b-', label='General Trend Line')

def PLOTTING_SMOOTH_TOTAL(INDEX, DATA):
	f = interp1d([INDEX[0], INDEX[3], INDEX[8], INDEX[-1]], \
		[DATA[0], DATA[3], DATA[8], DATA[-1]], kind='quadratic')
	x_int = np.linspace(1,5,1000)
	y_int = f(x_int)
	plt.plot(x_int, y_int, 'g-', label='Total Number Trend Line')

def PLOTTING(DATA_DWELLINGS, graph_data, title, ylabel):
	LABEL = [graph_data[i][0] for i in range(len(graph_data))]

	INDEX = [i for i in range(1, len(DATA_DWELLINGS)+1)]
	for i in [1,2,3]: LABEL[i] = LABEL[i] + ' (SemiDe)'
	for i in [4,5,6,7,8]: LABEL[i] = LABEL[i] + ' (APT)'

	plt.bar(INDEX[0], DATA_DWELLINGS[0], color='lightblue', align = 'center', width=1)
	plt.bar([INDEX[i] for i in [1,2]], [DATA_DWELLINGS[i] for i in [1,2]], color='red', align = 'center', width=0.4)
	plt.bar(INDEX[3], DATA_DWELLINGS[3], color='red', align = 'center', width=1)
	plt.bar([INDEX[i] for i in range(4,8)], [DATA_DWELLINGS[i] for i in range(4,8)], color='green', align = 'center', width=0.4)
	plt.bar(INDEX[8], DATA_DWELLINGS[8], color='green', align = 'center', width=1)
	plt.bar([INDEX[i] for i in range(9, len(INDEX)-1)], [DATA_DWELLINGS[i] for i in range(9, len(DATA_DWELLINGS)-1)], color='grey', align = 'center', width=0.4)
	plt.bar(INDEX[-1], DATA_DWELLINGS[-1], color='green', align = 'center', width=1)
	plt.xticks(INDEX, LABEL, rotation=90)
	plt.title(title)
	plt.ylabel(ylabel)
	plt.plot(INDEX, DATA_DWELLINGS, 'gs')
	PLOTTING_SMOOTH(INDEX, DATA_DWELLINGS)
	PLOTTING_SMOOTH_TOTAL(INDEX, DATA_DWELLINGS)
	plt.ylim(0, DATA_DWELLINGS[0]+10000)
	plt.legend()
	plt.savefig("Graphs/2006_"+title.strip().upper()+".png")
	plt.show()



if __name__ == '__main__':
	graph_data = DATARETRIEVAL("../Processing_Data/2006/2006_Housing_data.csv")

	DATA_DWELLINGS = [int(graph_data[i][1].replace(',','')) for i in range(len(graph_data))]
	DATA_POPULATIONS = [int(graph_data[i][2].replace(',','')) for i in range(len(graph_data))]

	PLOTTING(DATA_DWELLINGS, graph_data, \
		"NUMBER OF SPECIFIC DWELLINGS, 2006, WA \n",\
		"DWELLING COUNT")
	PLOTTING(DATA_POPULATIONS, graph_data, \
		"POPULATION UNDER SPECIFIC DWELLINGS, 2006, WA \n",\
		"POPULATION")