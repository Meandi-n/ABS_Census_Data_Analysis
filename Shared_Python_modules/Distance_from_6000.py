### OBTAINS DISTANCE OF POSTCODE FROM CENTRAL POSTCODE 6000 ###

'''
Author's Module Note:
Output's data as a CSV file. Obtained data is sufficient enough not to run programme agin 
Please dont run more than once in code - it takes a good 5 mins to ping google for the 
coordinates of all the postcodes.
'''
import re
from math import sin, cos, sqrt, atan2, radians

class POSTCODEPROCESSING:	
	def __init__(self, CENSUS_DATA_DIR, COORD_OUTPUT_DIR, DISTANCE_OUTPUT_DIR):
		#FILE DEFINITIONS
		self.DATA_FILE = open(CENSUS_DATA_DIR, 'r') #CENSUS DATA FILE
		self.file_distance = open(DISTANCE_OUTPUT_DIR,'w+') #DIST FILE
		self.reading_data_file()

		COORDS_FILE = open('../Processing_Data/Coordinates_of_Postcodes.csv', 'r')
		self.COORDS = COORDS_FILE.read().split('}')

		if self.COORDS == ['']:
			self.COORDS = []
			self.outputting_coords()

		self.outputting_distances()

	def reading_data_file(self):
		### GAINING POSTCOES IN INTEGER FORM FROM DATA ###
		DATA = self.DATA_FILE.readlines()
		self.POACODES = [((DATA[i]).split(',')[0])[3::] for i in range(1,len(DATA)-1)]
		#print(self.POACODES)
		return self.POACODES

	def outputting_coords(self):
		self.file_coords = open(COORD_OUTPUT_DIR,'w') # COORDINATE FILE	
		import requests 	
		import time
		self.COORDS = []
		### GETTING LATITUDE AND LONGITUDE ###
		for i in range(len(self.POACODES)):
			Error = True
			while(Error == True):
				time.sleep(1)
				try:
					url = "https://maps.googleapis.com/maps/api/geocode/json?address="\
						+self.POACODES[i]
					response = requests.get(url)
					resp_json_payload = response.json()
					print(resp_json_payload['results'][0]['geometry']['location'])	

					self.COORDS = self.COORDS + [resp_json_payload['results'][0]['geometry']['location']]

					print('Tial:',str(i), "/", str(len(self.POACODES)))

					Error = False
				except:
					Error = True
					print('connection not established')
					time.sleep(2)
		### SAVING LATUIDE AND LONGITUDE ###
		for i in range(len(self.COORDS)):
			self.file_coords.write(str(self.COORDS[i]))
			self.file_coords.write(',')

		#print(self.COORDS)
		return self.COORDS


	### USING COORDINATES TO OBTAIN DISTANCE FROM 6000 ###
	def outputting_distances(self):
		#printing coordinates of postcodes for analysis
		#print(self.COORDS)
		### PROCESSING VECTOR DISTANCES ###

		### GETTING LONG AND LAT OF 6000
		lat1 = radians(radians(abs(float(re.findall(r'\d+.\d+', self.COORDS[0])[0]))))
		lon1 = radians(radians(abs(float(re.findall(r'\d+.\d+', self.COORDS[0])[1]))))

		DISTANCE = []


		for i in range(len(self.COORDS)-1):
			###GETTING LONG AND LAT OF POINT
			lat2 = radians(radians(abs(float(re.findall(r'\d+.\d+', self.COORDS[i])[0]))))
			lon2 = radians(radians(abs(float(re.findall(r'\d+.\d+', self.COORDS[i])[1]))))
			
			dlon = (lon2-lon1)
			dlat = (lat2-lat1)

			a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
			c = 2 * atan2(sqrt(a), sqrt(1 - a))
			distance = 6371.01 * c
			DISTANCE = DISTANCE + [distance]



		### OUTPUTTING DISTANCE TO FILE ###

		for i in range(len(DISTANCE)):
			self.file_distance.write(str(DISTANCE[i]))
			self.file_distance.write(',')

		#print("wrote to file")

		#print(self.file_distance.read())

		return DISTANCE


''' this would be in my python code '''

'''
CENSUS_DATA_DIR = "../Processing_Data/2016_Census_POA.csv"
COORD_OUTPUT_DIR = '../Processing_Data/Coordinates_of_Postcodes.csv'
DISTANCE_OUTPUT_DIR = "../Processing_Data/POA_Distance_from_6000.csv"

x = POSTCODEPROCESSING(CENSUS_DATA_DIR, COORD_OUTPUT_DIR, DISTANCE_OUTPUT_DIR)
'''

