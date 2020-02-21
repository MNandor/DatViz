#merges stations into one file, filters for useful columns

ofs = open("result.txt", "wt")

for i in range(1, 10):
    ifs = open(" ("+str(i)+").txt", "rt") #station data files
    lines = ifs.readlines()
    ifs.close()
    lines = lines[2:]
    for line in lines:
        ofs.write(line[:6]+" "+line[128:134]+" "+line[138:144]+"\n")
ofs.close()
