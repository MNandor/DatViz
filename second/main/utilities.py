from conversions import toPixels

monthlyAvg =[
29.920347358644456,
33.142523340126694,
41.73391878405072,
51.376233981580064,
60.79101611580026,
67.07533987301206,
70.4074524399573,
69.7498061922208,
61.59895586469652,
51.563409217239226,
40.79359635834878,
32.615422195384674,
]

midPoint = 50
def tempToVal(a):
	small = midPoint-15#0#-36
	big = midPoint+15#100#112
	if a < small: return 0#small
	if a > big: return 1#big


	return (a-small)/(big-small)

def loadPoints(date, skip = 0):
	global midPoint
	ifs = open("goodcoords.txt", "rt")
	stats = ifs.readlines()
	
	midPoint = monthlyAvg[int(date.split()[1])-1]

	p = []
	for stat in stats:
		#x y temp id
		myP = [float(stat.split()[1]), float(stat.split()[2]), -999, int(stat.split()[0])]
		if myP[3] == 152800 or myP[3] == 151080: #always cold, bad for drawing
			continue
		
		p += [myP]
		
	ifs.close()
	
	return subLoadPoints(date, p)

def subLoadPoints(date, points):

	hottest = 0
	coldest = 1
	
	date = " "+date
	ifs = open("filMonths.txt")
	lines = ifs.readlines()
	ifs.close()
	for line in lines:
		if date not in line: continue
		
		data = line.split()
		id = int(data[0].strip())

		temp = float(data[4].strip())
		for cur in range(len(points)):
			if points[cur][3] == id:
				points[cur][2]= temp


	for cur in range(len(points)):
		if points[cur][2] == -999:
			print("bad point")
			continue
		points[cur][2] = tempToVal(points[cur][2])
		hottest = max(hottest, points[cur][2])
		coldest = min(coldest, points[cur][2])

	points = [x for x in points if x[2] != -999]
	
	return points, coldest, hottest