#summarizes temperature for each station/year/month

ifs = open("sum.txt", "rt")
dic = {}

count = 0
while True:
    line = ifs.readline()
    if line == "":
        break
    line = line.split()

    if "*" in line[2]:
        continue

    if line[0] not in dic:
        dic[line[0]] = {}

    year = int(line[1][:4])
    month = int(line[1][4:6])
    if year not in dic[line[0]]:
        dic[line[0]][year] = {}

    if month not in dic[line[0]][year]:
        dic[line[0]][year][month] = [999,0,-999,0]#min, total, max, count


    dic[line[0]][year][month][0] = min(int(line[2]), dic[line[0]][year][month][0])
    dic[line[0]][year][month][1] += int(line[2])
    dic[line[0]][year][month][2] = max(int(line[2]), dic[line[0]][year][month][2])
    dic[line[0]][year][month][3] += 1
    #Todo calculate average differently
    count += 1
    if count % 10000 == 0:
        print(count)


    if count > 100000:
        pass
        #break

ifs.close()

ofs = open("months.txt", "wt")
for station in dic:
    for year in dic[station]:
        for month in dic[station][year]:
            ref = dic[station][year][month]
            ofs.write(station+" "+str(year)+" "+str(month)+" ")
            ofs.write(str(ref[0])+" "+str(ref[1]/ref[3])+" "+str(ref[2])+"\n")

    print(station)

ofs.close()
