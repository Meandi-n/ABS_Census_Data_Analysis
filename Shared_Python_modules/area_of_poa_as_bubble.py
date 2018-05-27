from Distance_from_6000 import POSTCODEPROCESSING
##simple class that gets the closest postcode and then draws a radius between them
##it then draws a bubble that approximates that postcodes area. 
class BUBBLEPOAAREA:
    def __init__(self, CENSUS_DATA_DIR, COORD_OUTPUT_DIR, DISTANCE_OUTPUT_DIR, BUBBLE_OUTPUT_DIR, CSV_DIR):
        #if a CSV_DIR is not provided, then run the POSTCODEPROCESSING class with the output distance
        #function and the specified paramaters shown in the class-call for this calss
        '''x = POSTCODEPROCESSING(CENSUS_DATA_DIR, COORD_OUTPUT_DIR, DISTANCE_OUTPUT_DIR)
        if CSV_DIR == 0:
            self.distance = x.outputting_distances()'''
        #now define var distance, with a valye for func locally

        '''
        F I L E I/O >
        '''
        ### GAINING DISTANCE IN FLOAT FORM FROM DATA ###
        ##opening file with distance data within it
        print("\n\tAttempting to open file ", CSV_DIR, "From system")
        try:    DATA_FILE_D.close()
        except:    print("\n\tData file already open, not closing")
        try:    DATA_FILE_D = open(str(CSV_DIR), 'r+')
        except:    print("\n\tData file not found")
        try:     DATA_FILE_D.seek(0)
        except: print("Error in seeking")
        ##extracting data from file
        print("\n\tData file @: ", DATA_FILE_D)
        DATA = ','.join(DATA_FILE_D.readlines())
        print("\n\tData from file: ", DATA)
        #plitting data into distance list
        DISTANCE = [(DATA.split(','))[i] for i in range(len(DATA.split(',')))]
        print("\n\tDistance data: ", DISTANCE)
        #turning distance list into floats from strings
        for i in range(len(DISTANCE)-1):
            try:
                  DISTANCE[i] = float(DISTANCE[i]) 
            except:
                print("\n\tError in data obtained from file!")
        '''
        F I L E I/O !>
        '''

        #defining local class var distance as DISTANCE
        self.distance = DISTANCE[0:-1:1]
        #now define var poa with a valye for func from POSTCODEPROCESSING
        self.poa = open("../Processing_Data/postcodes.csv").read().split(',')

    #this function returns the poa_distances. This is just the relation (DICT) between
    #poa and distance from 6000
    def distance_poa_relation(self):
        self.poa_dist = dict(zip(self.poa, self.distance))
        return self.poa_dist

    #this calculated the bubble size
    def bubble_size(self, BUBBLE_OUTPUT_DIR):
        sorted_dist = sorted(self.distance)
        print(self.distance)
        bubble = [0 for i in range(len(self.distance))]
        print(bubble)
       
        print("\n\tAttempting to open file ", BUBBLE_OUTPUT_DIR, "From system")
        try:    BUBBLEIO.close()
        except:    print("\n\tData file already open, not closing")
        try:    BUBBLEIO = open(str(BUBBLE_OUTPUT_DIR), 'w+')
        except:    print("\n\tData file not found")
        try:     BUBBLEIO.seek(0)
        except: print("Error in seeking")

        #get radius
        for i in range(len(bubble)):
            try:
                bubble[i] = 3.14 * (abs(self.distance[i]-self.distance[i-1])/2)**2
            except:
                bubble[i] = 3.14 * (abs(self.distance[i]-self.distance[i+1])/2)**2

            if bubble[i]<1:
                try:
                    bubble[i] = 3.14 * (abs(self.distance[i]-self.distance[i-5])/2)**2
                except:
                    bubble[i] = 3.14 * (abs(self.distance[i]-self.distance[i+5])/2)**2

            print(bubble[i])
            BUBBLEIO.write(str(bubble[i])+',')
        # BUBBLE OUT WRITE BUBBLE SIZE TO OUTPUT
        BUBBLEIO.flush()
        BUBBLEIO.close()

        return bubble



#will be in code
CENSUS_DATA_DIR = "../Processing_Data/2016_Census_POA.csv"
COORD_OUTPUT_DIR = '../Processing_Data/Coordinates_of_Postcodes.csv'
DISTANCE_OUTPUT_DIR = "../Processing_Data/POA_Distance_from_6000.csv"
BUBBLE_OUTPUT_DIR = "../Processing_Data/Bubble.csv"
CSV_DIR = DISTANCE_OUTPUT_DIR

x = BUBBLEPOAAREA(CENSUS_DATA_DIR, COORD_OUTPUT_DIR, DISTANCE_OUTPUT_DIR, BUBBLE_OUTPUT_DIR, CSV_DIR)
x.bubble_size(BUBBLE_OUTPUT_DIR)