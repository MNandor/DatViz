#this script shows the extremes of the coordinates (for the purpose of cropping the map)

ifs = open("result.txt", "rt")
left = 99
right = 0
top = 0
bot = 99
lines = ifs.readlines()
ifs.close()
for line in lines:
    l = line.split()
    left = min(left, float(l[1]))
    right = max(right, float(l[1]))
    bot = min(bot, float(l[2]))
    top = max(top, float(l[2]))

print(left, right, bot, top)
