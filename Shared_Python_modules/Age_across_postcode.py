### OBTAINES POPULATION BY POSTCODE FOR CENSUS FILE ###
class AGEACROSSPOSTCODE:
	def __init__(self, CENSUS_DATA_DIR):
		self.DATA_FILE = open(CENSUS_DATA_DIR, 'r') #CENSUS DATA FILE
		### GAINING POSTCOES IN INTEGER FORM FROM DATA ###
		self.DATA = self.DATA_FILE.readlines()
		self.POA = [((self.DATA[i]).split(',')[0])[3::] for i in range(1,len(self.DATA)-1)]
		#print("POSTAL ADDRESSES -------------")
		#print(self.POA)		

	def poa_pop(self):
		self.pop = []
		Pop_Data_a = self.DATA_FILE.readlines()
		Pop_Data_b = [(Pop_Data_a[i]).split(',')[3] for i in range(len(Pop_Data_a))]
		self.pop_poa = dict(zip(self.POA, Pop_Data_b))
		return self.pop_poa

	def poa_pop_age(self, age):
		age_to_index = {
		'total': 3, '0t4': 6,
		'5t14' : 9, '15t19' : 12, 
		'20t24' : 15, '25t34': 18, 
		'35t44' : 21, '45t54' : 24, 
		'55t64' : 27, '65t74' : 30,
		'75t84' : 33, 'o85' : 36
		}

		Pop_Data_d = [(self.DATA[i]).split(',')[age_to_index[age]] for i in range(1,len(self.DATA))]
		#print("POP DATA D--------------------")
		#print(Pop_Data_d)

		self.output = [self.POA, Pop_Data_d]

		return self.output