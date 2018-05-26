'''

1. Each web page should show a different aspect of road fatalities, 
   and how that aspect has changed over time. 

2. Some of your pages must have photos and graphs. 

    a. Fatalities per year, and how this rate is changing over time;
    b. Fatalities per Australian state;
    c. Fatalities at different times of the day (each hour);
    d. The impact of different types of crash (single vehicle, multiple vehicle, pedestrian, etc.);  
    e. The contribution of crashes involving buses and trucks, compared to other kinds of crashes; 
    f. The impact of different speed limit zones on road fatalities;
    g. The impact of different road-user roles (driver; passenger; motor cyclist; cyclist, pedestrian, etc.) on road fatalities;
    h. The impact of gender on road fatalities - note that the data shows the gender of the deceased person, not necessarily of the driver;
    i. The impact of age (of the deceased) on road fatalities. 


    NOTE
    1. display the change in these statistics over time, such as comparing 1989 against 2017, or the first 10 years against the most recent 10 years.
    2. it would be more meaningful if you could display the statistics relative to the total number of vehicles or vehicle-kilometres in that category.
     . For example, display the fatalities for buses and trucks relative to how many buses and trucks are on the roads, rather than just the absolute 
       numbers of fatalities
     . To generate some of these relative percentages, you will need to obtain additional data from other sources   
     . eg (http://www.abs.gov.au/ausstats/abs@.nsf/mf/9208.0). Make sure you clearly document all your data sources 
    3.    


'''
import pandas as pd 
import csv
from dataAnalyzer import Analyzer 
'''
read the cvs file, the file is not well structured  
'''
def readCsvFile():
	with open('data/Fatalities.csv', 'rb') as csvfile: 
		reader = csv.reader(csvfile, delimiter=',', quotechar='|') 
		header = reader.next()
		for item in header:
			item = str(item).replace('"', '') 
			#print item 
		toNewFile = [] 	
		for row in reader:
			item = ','.join(row)  
			item = str(item.replace('"', '')) 
			itemList = item.split(',')
			#print itemList
			toNewFile.append(itemList)   
		return toNewFile 

			
'''
generate a better csv file 
'''
def betterCSV():
	df = pd.DataFrame(readCsvFile(), columns=['CiD','State','MM','YYYY','DD','T','CT',
	'BusI','RTruckI','ATruckI','SLimit','RoadU','G','A']) 
	df.to_csv('data.csv', index=False)

#betterCSV()

'''
use the new csv file for data visualization 
'''
df = pd.read_csv('data/data.csv')


an = Analyzer()  
an.fatalitiesPerYear(df) 
an.fatalitiesPerAstate(df)
an.fatalitiesInstantenous(df)
an.crashImpact(df)
an.fatalitiesComparation(df)
an.impactOfSpeedLimit(df)
an.impactOfRoadUser(df)
an.impactOfGender(df)
an.impactOfAge(df)


