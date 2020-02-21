#displays data (and lack of data), shows useful stations/years

import pygame
import random

def getYear(pair):
    year = pair[0]//12+1931
    month = pair[0]%12
    s = str(year)+" "+str(month)
    s += " "+str(pair[1])
    return s

def valToColor(val):
    small = 32#-36
    big = 112
    mid = (big-small)/2+small

    if val < small:
        return (0,255,255)
    if val > big:
        return (255,255,0)

    if val > mid:
        return (255*(val-mid)/(big-mid), 255-255*(val-mid)/(big-mid), 0)
    else:
        return (0, 255*(val-small)/(mid-small), 255-255*(val-small)/(mid-small))

ifs = open("unique.txt", "rt")
lines = ifs.readlines()
ifs.close()
stations = [int(x.split()[0]) for x in lines]

stations.sort()
    

width = 1066
height = len(stations)
screen = pygame.display.set_mode((width, height))

ifs = open("months.txt", "rt")
lines = ifs.readlines()
ifs.close()
data = [x.split() for x in lines]

mCount = {i:0 for i in stations}
for line in data:

    if int(line[1]) < 1973:
        continue
    
    stat = int(line[0])
    mCount[stat] += 1

stations = [[mCount[i], i] for i in mCount]
stations.sort()


counts = [i[0] for i in stations[-300:]]
print(counts[-50:])
ofs = open("selectedStations.txt", "wt")
for wl in stations[-50:]:
    ofs.write(str(wl[1]))
    ofs.write("\n")
ofs.close()
stations = [i[1] for i in stations]




counter = 0
for line in data:
    stat = stations.index(int(line[0]))

    if int(line[1]) < 1973:
        pass#continue

    if mCount[stations[stat]] < 488:
        pass#continue
    
    time = (int(line[1])-1931)*12+int(line[2])

    temp = float(line[5])
    if temp > 112 or temp < -36:
        continue
    color = valToColor(temp)
    #print(color, temp)
    
    screen.set_at((time, stat), color)

    counter += 1
    if counter % 1000 == 0:
        print(stat)

pygame.display.flip()

clock = pygame.time.Clock()
pygame.image.save(screen,"selection.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    s = getYear(pygame.mouse.get_pos())
    
    pygame.display.set_caption(s)
    clock.tick(60)


#data matters after 1973 and top 50
