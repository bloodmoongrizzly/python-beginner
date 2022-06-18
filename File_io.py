import csv
shipCap=[] #list
with open("captains.csv","r") as csvfile:
    csvreader = csv.reader (csvfile)

        for row in csvreader:
            shipCap.append(row)

for row in shipCap:
    print(row)
print(shipCap [2] [1])

inShip=input("ship? ")##adding to file
inCap=input("Captain? ")
shipcCap.append([inShip,inCap])

print (shipCap)

with open ("captains.csv","w",newline='')as csvfile:## outputs back to file.
    csvwriter=csv.writer(csvfile)
    csvwriter=writerows(shipCap)
