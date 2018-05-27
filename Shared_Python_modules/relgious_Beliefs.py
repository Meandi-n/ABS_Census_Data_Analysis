class RELIGIOUSBELIEFS_R_POSTCODE:
	def __init__(self):
		self.DATA_DIR="../Processing_Data/2016_Religious_Data.csv"
		file_obj = open(self.DATA_DIR, 'r')
		self.file_data = file_obj.readlines()[1:-1:1]
		self.associations = {
		'Buddhism':3, 'Anglican':6, 'Asyrin Apstlic':9, 'Baptist':12,
		'Brethren':15, 'Catholic': 18, 'Christian-Christ':21, 
		'Eastern Orthadox':24, 'Jehovas Witnesses':27, 
		'Latter Day Saints':30, 'Lutheran':33, 'Oriental Orthadox':36, 
		'Other Protestant':39, 'Pentecostal':42, 'Ptsbytrin Refrmd': 45, 
		'Salvation Army':48, 'Seventh Day Adventist':51, 'Uniting Church':54,
		'Christian Non-defined': 57, 'Christian Other': 60, 'Christian Total':63, 
		'Hinduism':66, 'Islam':69, 'Judaism':72, 'Indigenous':75, 
		'Sikhism':78, 'Other':81, 'Secular Beliefs': 84, 'Secular Beliefs Non Religious': 87, 
		'Secular 2': 90, 'Atheist':93, 'Not stated':96
		}
	def religious_count(self,religion):
		index = self.associations[religion]

		data = sum([float(self.file_data[i].split(',')[index]) for i in range(len(self.file_data))])

		### simply returns sum of all data in list - total population
		return data

	def religious_count_poa(self,religion):
		index = self.associations[religion]

		data_poa = [self.file_data[i].split(',')[index] for i in range(len(self.file_data))]

		### returns data in list which corresponds to postal codes
		return data_poa
	def atheistic_count_poa(self):
		index = self.associations[religion]

		data_poa = [self.file_data[i].split(',')[index] for i in range(len(self.file_data))]



