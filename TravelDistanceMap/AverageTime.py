import csv
import os

coords = {}
with open("cities.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        coords[row["Name"]] = (row["Lng"], row["Lat"])

cities = {}
for name in os.listdir("times"):
    with open("times/" + name) as file:
        reader = csv.DictReader(file)
        tmp = []
        for row in reader:
            tmp.append((float(row["Duration"]), float(row["Density"])))
        cities[name[:name.index(".")]] = tmp

with open("average_times.csv", "w+") as file:
    file.write("City,AvgDuration,Lng,Lat\n")
    for city in cities.items():
        average = sum([x[0]*x[1] for x in city[1]])/sum([x[1] for x in city[1]])
        print(city[0])
        file.write(city[0] + "," + str(average) + "," + coords[city[0]][0] + "," + coords[city[0]][1] + "\n")