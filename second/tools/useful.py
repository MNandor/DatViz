#removes unusued information, just station, timecode, and temperature

ifs = open("goodcoords.txt", "rt")
slines = ifs.readlines()
ifs.close()
stations = [x.split()[0] for x in slines]
print(stations)

startDate = "199810010000"
endDate = "199810319900"

ofs = open("sum.txt", "wt")
for i in range(1, 10):
	ifs = open(" ("+str(i)+").txt", "rt")
	ifs.readline()
	print(i)
	while True:
		line = ifs.readline()
		if line == "":
			break;
			
		stat = line[:6]
		time = line[13:25]
		temp = line[83:87]
		
		if stat not in stations or time > endDate or time < startDate or "*" in temp:
			continue

		ofs.write(stat+" "+time+" "+temp+"\n")

	ifs.close()
	
ofs.close()
