import pygame
from conversions import toPixels, dist, valToColor

width = 1280
height = 720#663
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
bg = pygame.image.load("newMap.png")
marker = pygame.image.load("marker.png")
pygame.font.init()
myfont = pygame.font.SysFont("Impact", 30)


def frameEnd(day):
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	#pygame.image.save(screen, "screenshot"+day+".png")
	pygame.display.set_caption(day)
	print(clock.tick(60))

def colorPixel(a, points):

	#mindist = 100
	cur = 0
	totalDist = 0
	for point in points:
		distance = dist(a, toPixels(point[0], point[1]))
		#mindist = min(distance, mindist)
		cur += (point[2]-0.5)/distance
		totalDist += 1/distance

	#print(cur, totalDist, cur/totalDist)
	cur = 0.5+ cur/totalDist
	
	return valToColor(cur, coldest, hottest)

def label(day):

	ocolor = valToColor(0.1,0,1)
	icolor = valToColor(0,0,1)
	tcolor = (130,150,150)
	
	pygame.draw.rect(screen, ocolor, (0,610,215,100))
	pygame.draw.rect(screen, ocolor, (0,663,1280,100))
	pygame.draw.rect(screen, icolor, (0,615,210,100))
	pygame.draw.rect(screen, icolor, (0,668,1280,100))
	
	textsurface = myfont.render(day.split()[0]+" "+textMonths[int(day.split()[1])-1], True, tcolor)
	textsurface2 = myfont.render("Temperature adjusted for season", True, tcolor)
	screen.blit(textsurface, (5,620))
	screen.blit(textsurface2, (5,673))


SQSIZE = 11 #larger SQSIZE means less accurate picture, but much faster to draw
coldest = 0
hottest = 1

textMonths=["January", "February","March", "April","May", "June","July", "August","September", "October","November", "December",]

def makeFrame(points, day):

	screen.blit(bg, (0,0))

	grad = pygame.Surface((width, height))
	for x in range(0, width, SQSIZE):
		for y in range(0, height, SQSIZE):
			cur = colorPixel((x+SQSIZE//2,y+SQSIZE//2), points)
			pygame.draw.rect(grad, cur, (x,y,SQSIZE,SQSIZE))
			grad.set_at((x,y), cur)
	
	grad.set_alpha(128)

	screen.blit(grad, (0,0))
	for point in points:
		place = toPixels(point[0], point[1])
		screen.blit(marker, place)

	label(day)

	frameEnd(day)


def programEnd():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()