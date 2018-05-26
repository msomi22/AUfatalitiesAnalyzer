

import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns 
'''
Crash ID,State,Month,Year,Dayweek,Time,Crash_Type,Bus_Involvement,
  Rigid_Truck_Involvement,Articulated_Truck_Involvement ,Speed_Limit,Road_User,Gender,Age


  CiD,State,MM,YYYY,DD,T,CT,BusI,RTruckI,ATruckI,SLimit,RoadU,G,A
'''
class Analyzer():

	def __init__(self):
		return None  


	def fatalitiesPerYear(self, df): 
		#df = df[df['YYYY'] == 1990]  
		df['YYYY'].plot(kind='hist', bins=8, title='Fatalities per year', facecolor='blue', alpha=0.5, density=1) 
		#plt.show()
		#plt.savefig('data/fatalitiesPerYear')  

	def fatalitiesPerAstate(self, df):
		df = df.groupby(['State']).size().reset_index(name='Fatalities per Australian state')
		df.plot(kind='pie', y='Fatalities per Australian state', ax=None, autopct='%1.1f%%', startangle=90, shadow=False, labels=df['State'], legend = False, fontsize=14)  
		plt.savefig('data/fatalitiesPerAstate')  
		

	def fatalitiesInstantenous(self, data):
		print 'fi' 

	def crashImpact(self, data):
		print 'ci'

	def fatalitiesComparation(self, data): 
		print 'fc'

	def impactOfSpeedLimit(self, data):
		print 'iosl'
	 

	def impactOfRoadUser(self, data):
		print 'ioru'

	def impactOfGender(self, data):
		print 'iog'

	def impactOfAge(self, data): 
		print 'ioa' 


