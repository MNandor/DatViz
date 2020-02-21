#only keeps data in selected time and stations

ifs = open("selectedStations.txt", "rt")
lines = ifs.readlines()
ifs.close()
good = [x.strip() for x in lines]

ifs = open("months.txt", "rt")
lines = ifs.readlines()
ifs.close()


result = [0 for x in range(5)]
ofs = open("filMonths.txt", "wt")
for line in lines:
    parts = [x.strip() for x in line.split()]
          
    if parts[0] not in good:
          result[1] += 1
          continue
    if int(parts[1]) < 1973:
          result[2] += 1
          continue
    if int(parts[3]) < -36:
          result[3] += 1
          continue
    if int(parts[5]) > 112:
          result[4] += 1
          continue


    result[0] += 1
    ofs.write(line)


ofs.close()

print(result)
print("good station year cold hot")
#1973
#-36 112
