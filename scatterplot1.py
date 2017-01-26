#import stuff for the weather api and for charting 
import requests
import pandas as pd
import csv

#create the url
endpoint = 'https://api.darksky.net/forecast/'
key = 'c4be34991425bf8b6c828a21288faefc'
lat = '40.6640'
lon = '74.2107'
year = int(input("pick a year "))
time = str(year) + '-06-19T15:00:00'


#assemble full url
url = endpoint + key + '/' + lat + ',' + lon + ',' + time

#call the url
r = requests.get(url)

weather = r.json()

#create the csv
csvfile = open('scatterplot1.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter = ',')
csvwriter.writerow(['Date', 'Temperature'])

#make the data
for x in range(year,2016):
    #assemble full url
    time = str(x) + '-06-19T15:00:00'
    url = endpoint + key + '/' + lat + ',' + lon + ',' + time
    r = requests.get(url)
    weather = r.json()
    Temperature = weather['currently']['temperature']
    csvwriter.writerow([x, Temperature])
#finish the csvfile
csvfile.close()    

#set up bokeh for the graph
import bokeh 
from bokeh.charts import Scatter, output_file, save
df = pd.read_csv('scatterplot1.csv')
p = Scatter(df, x = 'Date', y = 'Temperature', color = 'blue', title = "My Birthday Temperature", legend = 'top_right', xlabel = "Year", ylabel = "Temperature")

#save the file
output_file('scatterplot1.html')
save(p)