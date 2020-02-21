import colorsys

def toPixels(x, y): #world coordinates to pixels
	width = 1280
	height = 663
	left = 43.667
	right = 48.483
	bot = 16.317
	top = 29.733
	
	48.483, 29.733
	43.667, 16.317

	x = (x-left)* width / (right-left)
	y = (y-bot)* height / (top-bot) 
	y = height-y
	return (int(x)-7, int(y)-7)


def dist(a, b):
	val = ((a[0]-b[0])**2+(a[1]-b[1])**2)
	if val == 0:
		val = 0.00000001

	return val

def valToColor(val, small, big):
	
	t = colorsys.hsv_to_rgb((1-(val-small)/(big-small))/2, 1, 1)
	return [255*x for x in t]
