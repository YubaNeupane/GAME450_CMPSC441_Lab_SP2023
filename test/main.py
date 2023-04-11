import json
import time

from tabulate import tabulate
 
table_data = []
iteration = 0

while True:
    with open("test\log.json",'r') as my_file:
        i = json.load(my_file)
        # Extract the values for time, unit, range, magnitude, and speed
        dectedObject = i.get('DectedObject',False)
        if(dectedObject):
            table_data.append(["Object", dectedObject])
            print(tabulate(table_data, headers=['Time', 'Unit', 'Range', 'Magnitude', 'Speed']))

        time_data = i.get('time',None)
        unit = i.get('units',None)
        ranges = i.get('range',None)
        magnitude = i.get('mangitude',None)
        speed = i.get('speed',None)
        table_data.append([time_data, unit, ranges, magnitude,speed])

        print(tabulate(table_data, headers=['Time', 'Unit', 'Range', 'Magnitude', 'Speed']))

    iteration += 1
    if iteration % 2 == 0:
        time.sleep(0.5)
