import pylab, scipy, Image,PIL
import numpy as np

#filename: yes .png,  ;not .gif
name = "elephant.jpg"
#Lower => needs to be darker
threshold = 80
#number of points approx:
num = 10000


#image =  np.asarray(pylab.loadtxt('import.csv'delimiter=","))  #Import Points

from scipy import misc

#img = Image.open("elephant.jpg")

img = np.asarray(PIL.Image.open(name))

#img = misc.face()
#misc.imsave('elephant.jpg', img) # uses the Image module (PIL)


xdim,ydim,none = np.shape(img)

def black(x,y):
	global img
	for rgb in img[x,y]:
		if rgb>threshold:
			return False
	return True

points = [[x*1e-8/xdim,y*1e-8/xdim,0,1] for x in range(xdim) for y in range(ydim) if black(x,y)]

#reducing the number of points:
length = len(points)
if length>num:
	points = points[0::int(length/num)]

np.savetxt("import.csv", points, delimiter=",")

print len(points)
