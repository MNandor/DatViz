#finds extremes in data (time, temperature) and number of wrong/missing data points

ifs = open("sum.txt", "rt")
small = 999
big = -999
starcount = 0
ysmall = 9999999999999
ybig = -9999
wrongrecord = 0

while True:
    line = ifs.readline()
    if line == "":
        break
    
    line = line.split()
    if "*" in line[2]:
        starcount += 1
        continue
    
    val = float(line[2])

    if val >= 113 or val <= -38:
        wrongrecord += 1
        continue

    
    small = min(val, small)
    big = max(val, big)

    time = int(line[1])
    ysmall = min(ysmall, time)
    ybig = max(ybig, time)
ifs.close()

print("Coldest:",small, "Hottest:",big)

print("Oldest:",ysmall, "Newest:", ybig)

print("No data:",starcount, "Wrong:",wrongrecord)
