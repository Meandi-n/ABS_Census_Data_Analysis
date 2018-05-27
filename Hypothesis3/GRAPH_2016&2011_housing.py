import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

plt.style.use('ggplot')

def HOUSING_TYPES_PLOT(DIR, inc):
	file_obj = open(DIR)
	file_data = file_obj.read().split('POA')[1::]

	c = [0,0,0,0,0]

	for a in range(len(file_data)):
		for i in range(5):
			try:
				c[i] = c[i] + float(file_data[a].split(',')[i+inc])
			except:
				c[i] = c[i]
				print("Conversion of ", file_data[i][2], "failed")

	print(c)
	x = [1,2,3,4,5]
	plt.bar(x,c,align='center')
	plt.xticks([1,2,3,4,5],\
		 ['Seperate Dwelling', 'SemiDetached',\
		  'Flat', 'Other', 'Notstated'], rotation=10)
	plt.plot(x,c,'ro')
	f = interp1d(x, c, kind='quadratic')
	x_int = np.linspace(1,5,1000)
	y_int = f(x_int)
	plt.plot(x_int, y_int)
	plt.ylim(0,700000)
	plt.title("HOUSING TYPES (2016)\n")
	plt.ylabel("RESIDENTS")
	if inc < 37: plt.savefig("Graphs/2011_HOUSING_DATA.png")
	if inc >= 37:plt.savefig("Graphs/2016_HOUSING_DATA.png")
	plt.show()

if __name__ == "__main__":
	HOUSING_TYPES_PLOT('../Processing_Data/2016_housing_data.csv', 19)
	HOUSING_TYPES_PLOT('../Processing_Data/2011_housing_data.csv', 37)
