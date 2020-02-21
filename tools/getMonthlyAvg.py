#gets the average temperature for each month, regardless of year

ifs = open("filMonths.txt", "rt")
ar = [[0,0] for i in range(12)]

lines = ifs.readlines()
ifs.close()
for line in lines:
	line = line.split()
	if line[0] == "152800" or line[0] == "151080": #these are always cold, don't draw
		continue
	month = int(line[2])-1
	ar[month][0]+=1
	ar[month][1]+=float(float(line[4]))


for a in ar:
	print(a[1]/a[0])


'''
29.920347358644456
33.142523340126694
41.73391878405072
51.376233981580064
60.79101611580026
67.07533987301206
70.4074524399573
69.7498061922208
61.59895586469652
51.563409217239226
40.79359635834878
32.615422195384674
'''