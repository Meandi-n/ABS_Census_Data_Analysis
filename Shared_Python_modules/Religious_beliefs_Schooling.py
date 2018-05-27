import matplotlib.pyplot as plt
plt.style.use('ggplot')
class SCHOOLING_INFROMATION:
	def __init__(self):
		file_obj = open("../Processing_Data/2016_Schooling_data.csv", 'r')
		self.file_data = file_obj.readlines()

	def PUBLIC_TO_PRIVATE(self, POA):
		data = [self.file_data[i].split('POA') for i in range(len(self.file_data))][1::]
		
		data = [data[i][1].split(',') for i in range(len(data))]
		
		associations = {
		3: "INFANT_PUBLIC", 6:"INFANRS_CATHOLIC", 9:"INFANTS_PRIVATE",
		15: "SEC_PUBLIC", 18:"SEC_CATHOLIC", 21:"SEC_PRIVATE"
		}
		print(len(data))
		print(data[1][3])
		Y_DATA_IPu = sum([int(data[i][3]) for i in range(len(data))])
		Y_DATA_ICa = sum([int(data[i][6]) for i in range(len(data))])
		Y_DATA_IPr = sum([int(data[i][9]) for i in range(len(data))])
		Y_DATA_SPu = sum([int(data[i][15]) for i in range(len(data))])
		Y_DATA_SCa = sum([int(data[i][18]) for i in range(len(data))])
		Y_DATA_SPr = sum([int(data[i][21]) for i in range(len(data))])

		X_DATA_Abs = [data[i][0] for i in range(len(data))]

		X_DATA_Nos = [1,2,3,4,5,6]
		X_DATA_Cat = ['Infant Public', 'Infant Catholic', 'Infant Private',\
						'Secondary Public', 'Secondary Catholic', 'Secondary Private']
		Y_Data = [Y_DATA_IPu, Y_DATA_ICa, Y_DATA_IPr, Y_DATA_SPu, Y_DATA_SCa, Y_DATA_SPr]

		print(len(Y_Data))
		print(len(X_DATA_Cat))
		color_alpha = '#9900ff'
		plt.xticks(X_DATA_Nos, X_DATA_Cat, rotation=10)
		plt.title("Schooling: Popularity of Institutions(2016) \n")
		plt.ylabel("Number of Students across all POA")
		plt.xlabel("Institution")
		plt.bar(X_DATA_Nos, Y_Data, align='center', color=color_alpha)
		plt.plot(X_DATA_Nos, Y_Data, 'ro')
		plt.legend()
		plt.savefig("../Hypothesis2/Graphs/GRAPH_INSTITUTION_SCHOOLING.png")
		plt.show()


#3 infants pubic 

#6 infants catholic

#9 infants non govt

#15 secondary government

#18 secondary catholic

#21 secondary non govt

x = SCHOOLING_INFROMATION()
x.PUBLIC_TO_PRIVATE(1)


