import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"

#Get date and temperature readings
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Gives each header an index and prints the index and header. 
    #Gives the index position of each header
    for index,column_header in enumerate(header_row):
        print(index, column_header)
        
    dates,highs,lows = [], [], []

    for row in reader:
        try:
            high = int(row[1])
            high_celcius = int((high - 32)/1.8)
            
            low = int(row[3])
            low_celcius = int((low - 32)/1.8)
            
            date = datetime.strptime(row[0], "%Y-%m-%d")
       
        except:
            print("Missing data")
        else:
            highs.append(high_celcius)
            lows.append(low_celcius)
            dates.append(date)
        
    print(highs)

fig = plt.figure(dpi=128, figsize = (10,6))
plt.plot(dates,highs,c="red",alpha = 0.5)
plt.plot(dates,lows,c="blue",alpha = 0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha = 0.1)

#Format plot
plt.title("Daily temperature of Death Valley in 2014")
plt.xlabel("",fontsize = 10)
plt.ylabel("Temperature",fontsize = 14)
plt.tick_params(axis = "both", which = "major", labelsize = 16)

#Adjusting y scale. gca = get current axis
axes = plt.gca()
axes.set_ylim([-15,45])
fig.autofmt_xdate()

plt.show()

    
