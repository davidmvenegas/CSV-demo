import csv

data = []
pos = []

store = {}

with open('./data/reads.csv') as mainData:
    next(mainData)
    csvreader = csv.reader(mainData)
    for row in csvreader:
        data.append(row)

with open('./data/loci.csv') as positions:
    next(positions)
    csvreader = csv.reader(positions)
    for row in csvreader:
        pos.append(row[0])

for i in pos:
    store[i] = 0

for read in data:
    pos = int(read[0])
    rg = int(read[0]) + int(read[1])
    for num in range(pos, rg):
        strNum = str(num)
        if strNum in store.keys():
            store[strNum] += 1
            break

print('we got here')

for key, value in store.items():
    print(key, ' : ', value)
