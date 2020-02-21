#stores the coordinates of top 50 stations from IDs

ifs = open("selectedStations.txt", "rt")
filter = ifs.readlines()
ifs.close()

ifs = open("unique.txt", "rt")
ofs = open("goodcoords.txt", "wt")

lines = ifs.readlines()
ifs.close()
for line in lines:
    if line.split()[0]+"\n" in filter:
        ofs.write(line)

ofs.close()
