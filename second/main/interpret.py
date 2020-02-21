startDate = "199810010000"
endDate = "199810319900"
dayCount = 31

midPoint = 51.563409217239226

class Station:
	def linData(self):
		for day in range(dayCount):
			for hour in range(24):
				#print("#", day, hour, self.getTemp(day, hour), self.id)
				if self.getTemp(day, hour) == -999:
					rightPush = 0
					leftPush = 0
					rVal = 0
					lVal = 0
					while True:
						rightPush += 1
						rVal = self.getTempOne(day*24+hour+rightPush)
						if rVal != -999:
							break
					
					while True:
						leftPush += 1
						lVal = self.getTempOne(day*24+hour-leftPush)
						if lVal != -999:
							break
					
					if rVal == -69:
						self.gettable[day][hour] = lVal
						#print("left")
					elif lVal == -69:
						self.gettable[day][hour] = rVal
						#print("right", rVal, rightPush)
					else:
						total = rightPush+leftPush
						left = lVal*rightPush/total
						right = rVal*leftPush/total
						self.gettable[day][hour] = left + right
						
						#print(day*24+hour, day, hour, leftPush, rightPush, lVal, rVal, left, right)
						
						
						
	def __init__(self, id, data):
		self.id = id
		mydata = [x for x in data if x[0] == id]
		mydata.sort(key=lambda x: x[1])
		
		self.gettable = [[-999 for i in range(24)] for j in range(dayCount)]
		
		for d in mydata:
			act = int(d[1])-int(startDate)
			if act % 100 != 0:
				print(act)
				continue #todo handle
			act = act//100
			hour = (act%100)-1
			
			act = act//100
			day = (act%100)-1
			
			self.gettable[day][hour] = d[2]
			
		self.linData()
		
		for day in range(dayCount):
			for hour in range(24):
				self.gettable[day][hour] = float(self.gettable[day][hour])
		
	def getTempOne(self, dh):
		if dh<0 or dh >= 24*dayCount:
			return -69
		return float(self.getTemp(dh//24, dh%24))
	
	def getTemp(self, day, hour):
		return float(self.gettable[day][hour])

ifs = open("goodcoords.txt", "rt")
slines = ifs.readlines()
ifs.close()
stations = [x.split()[0] for x in slines]
orstats = [x.split() for x in slines]

ifs = open("sum.txt", "rt")
data = ifs.readlines()
ifs.close()
data = [x.split() for x in data]


dict = {}
for stat in stations:
	dict[stat] = Station(stat, data)
	ch = dict[stat].getTempOne(0)
	if ch == -999 or ch == -69:
		del dict[stat]
		stations = [x for x in stations if stat not in x]
		orstats = [x for x in orstats if stat not in x]
		print(stat)
		
	
def test():
	for i in range(24):
		print(dict['150100'].getTemp(0,i))


def tempToVal(a):
	small = midPoint-25#0#-36
	big = midPoint+25#100#112
	if a < small: return 0#small
	if a > big: return 1#big


	return (a-small)/(big-small)

def getPoints(day, hour):
	p = []
	for stat in orstats:
		#x y temp id
		id = int(stat[0])
		myP = [float(stat[1]), float(stat[2]), -999, id]
		myP[2] = dict[str(id)].getTemp(day, hour)
		myP[2] = tempToVal(myP[2])
		p += [myP]
	
	return p