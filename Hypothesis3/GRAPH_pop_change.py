import matplotlib.pyplot as plt
plt.style.use('ggplot')

y = [2474410, 2230053, 2466752]
plt.bar([1,2,3], y, \
	align='center',color='lightblue', width=0.4)

change = [(2230053-2474410)/2230053*1000000,\
		 (2466752-2230053)/2466752*1000000,0]


plt.arrow(1, y[0], 0, (change[0]), head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.arrow(2, y[1], 0, (change[1]), head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.arrow(3, y[2], 0, (change[2]), head_width=0.1, head_length=0.1, fc='k', ec='k')


plt.plot([1,2,3], [2474410, 2230053, 2466752], 'r-o')
plt.xticks([1,2,3], ['2006', '2011', '2016'])
plt.title("POPULATION CHANGE 2006-2016")
plt.ylabel("POPULATION")
plt.xlabel("YEAR")
plt.savefig("Graphs/POP_CHANGE.png")
plt.show()