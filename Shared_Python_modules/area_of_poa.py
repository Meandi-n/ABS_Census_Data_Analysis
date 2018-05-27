### THIS USES THE SHOELACE METHOD TO DETERMINE THE AREA OF A IRREGULAR POLYGON ###
class AREAOFPOA:
	def __init__(self, coords):
		self.x = ['a']
		self.y = ['a']
		self.x += [self.coords[i][0] for i in range(len(self.coords))]
		self.y += [self.coords[i][1] for i in range(len(self.coords))]
		
	def A(self):

		#MATHEMATICAL FORMULA FROM
		#https://en.wikipedia.org/wiki/Shoelace_formula

		E1 = sum([self.x[i]*self.y[i+1] for i in range(1,len(self.x)-1)])
		E2 = self.x[-1]*self.y[1]
		E3 = sum([self.x[i+1]*self.y[i] for i in range(1, len(self.x)-1)])
		E4 = self.x[1]*self.y[-1]

		Area = 0.5 * abs(E1 + E2 - E3 - E4)

		print(Area)

''' testing; will go in python code. 
coords = [[0,1], [0,3], [0,5]]

x = AREAOFPOA(coords)
x.A()
'''