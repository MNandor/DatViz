import random
from utilities import *
import drawer

drawer.SQSIZE = 25


for dYear in range(1973, 2019):
	for dMonth in range(1, 13):
		day = str(dYear)+" "+str(dMonth)
		print("Making", day)
		points, coldest, hottest = loadPoints(day)
		#drawer.hottest, drawer.coldest = hottest, coldest
		drawer.makeFrame(points, day)




drawer.programEnd()