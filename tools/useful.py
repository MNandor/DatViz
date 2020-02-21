#removes unusued information, just station, timecode, and temperature

ofs = open("sum.txt", "wt")
for i in range(1, 10):
    ifs = open(" ("+str(i)+").txt", "rt")
    ifs.readline()
    print(i)
    while True:
        line = ifs.readline()
        if line == "":
            break;

        ofs.write(line[:6]+" "+line[13:25]+" "+line[83:87]+"\n")

    ifs.close()
    
ofs.close()
