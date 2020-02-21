import random
from utilities import *
import drawer
import interpret

drawer.SQSIZE = 51


for day in range(31):
	for hour in range(24):
		time = str(day+1)+". "+str(hour)+":00"
		print("Making", time)
		points = interpret.getPoints(day, hour)
		print(len(points))
		drawer.makeFrame(points, time)




drawer.programEnd()