class POPOFPOA:
	def __init__(self, CENSUS_DATA_DIR):
		FILE = open(CENSUS_DATA_DIR,'r')
		self.FILE_DATA = FILE.read().split('POA')

	def processing(self):
		POPULATION = []
		for i in range(2, len(self.FILE_DATA)):
			POPULATION = POPULATION + [self.FILE_DATA[i].split(',')[3]]
		#print(POPULATION)
		return POPULATION

