import os,sys,pylab
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

name="gauss"

MC = pylab.loadtxt("MC"+name+"intensity.csv", delimiter=",")
an = pylab.loadtxt("an"+name+"intensity.csv", delimiter=",")



maximum = 10**-5 
minimum = 10**-8


def limit(x):
    def a(x):
	global maximum,minimum
        return max(min(x,maximum), minimum)
    return a(x)/maximum

limit = np.vectorize(limit)

def samediffscale(x,y):
	global MC, an, maximum, minimum	
	if x==1 and y==1:
		return 1
	elif x==1 and y==2:
		return minimum/maximum
	else:
		return max((MC-an)[x,y],minimum/maximum)

MC = limit(MC)
an = limit(an)

xshape,yshape = np.shape(MC-an)

diff = np.array([[samediffscale(x,y) for y in range(yshape)] for x in range(xshape)])
print np.min(diff)
print np.min(MC)



def plot(Intensity,title):
    pixels_row, pixels_col = np.array(Intensity).shape


    if 1: #For a 2D heat map
        fig = plt.figure()
        #ax = fig.add_subplot(111)
        ax = fig.add_subplot(111, aspect='equal')
        #CHANGE COLOUR MAP HERE!!
        #Pictures of the colour map are at: http://matplotlib.org/users/colormaps.html
        #put _r at the end to reverse the direction of the colour.
        #the ones below have been good.
        
        #cmap = cm.get_cmap('gist_gray_r')
        #cmap = cm.get_cmap('seismic_r')
        cmap = cm.get_cmap('hot_r')

        if 1:
            if 1: #bound with log scale
                #cs = plt.pcolor(np.log10(Intensity), cmap = cmap)
                cs = plt.pcolor(np.log10(Intensity), cmap = cmap)
    
        #This plots the colour bar.        
        cb = plt.colorbar(cs, orientation='vertical')

    plt.title(title)


plot(MC,"MC")
plot(an,"analytic")
plot(diff,"difference")

plt.show()
