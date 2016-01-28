import matplotlib.pyplot as plt 
import numpy as np
import itertools
from scipy.interpolate import interp1d
import pylab
from scipy import interpolate

def function(name):
  name = str(name)
  centre = np.array([100,100])
  points1 =np.asarray(pylab.loadtxt('Folder/'+name + ' data1.csv',delimiter=","))
  points2 =np.asarray(pylab.loadtxt('Folder/'+name + ' data2.csv',delimiter=","))
  arrlen1, width = np.shape(points1)
  arrlen2, width = np.shape(points2)

  points1 = [x-centre for x in points1] #this puts them in the best order
  points2 = [x-centre for x in points2] #this puts them in the best order

  def lstsqr(pointsA,pointsB):
     lstsqr = 0 
     for x in pointsA:
        lstsqr+= min([abs(x[0]-y[0])**2+abs(x[1]-y[1])**2 for y in pointsB])
     return lstsqr

  def rotate(points1,angle):
     rotMatrix = np.array([[np.cos(angle), -np.sin(angle)], 
                     [np.sin(angle),  np.cos(angle)]])
     return np.transpose(rotMatrix.dot(np.transpose(points1)))

  fitscore = 1e100
  fitangle = 1e100
  for x in np.arange(0,3.14159265*2,3.14159265*2/360):
     rot = rotate(points1,x)
     score = lstsqr(rot,points2)+lstsqr(points2,rot)
     if score<fitscore:
        fitscore = score
        fitangle = x 

  print "Preliminary fitscore = %.2f" %(fitscore)
  print("Preliminary fitangle (deg) = %.0f" %(min(fitangle*180/3.14159265,360-fitangle*180/3.14159265)))

  for x in np.arange(fitangle-3.14159265*2/360,fitangle+3.14159265*2/360,3.14159265*2/3600):
     rot = rotate(points1,x)
     score = lstsqr(rot,points2)+lstsqr(points2,rot)
     if score<fitscore:
        fitscore = score
        fitangle = x 
  print "Refined fitscore = %.2f" %(fitscore)
  print("Refined fitangle (deg) = %.1f" %(min(fitangle*180/3.14159265,360-fitangle*180/3.14159265)))

  rot = rotate(points1,fitangle)

  maxrange = 0
  for x in rot:
    for y in x:
      if abs(y)>maxrange:
        maxrange = abs(y)
  for x in points1:
    for y in x:
      if abs(y)>maxrange:
        maxrange = abs(y)
  for x in points2:
    for y in x:
      if abs(y)>maxrange:
        maxrange = abs(y)
  maxrange = maxrange*1.1

  plt.plot(np.array(points2)[:,0],np.array(points2)[:,1],'ro')
  plt.plot(np.array(points1)[:,0],np.array(points1)[:,1],'bx')
  plt.plot(np.array(rot)[:,0],np.array(rot)[:,1],'bo')
  plt.xlim(-maxrange,maxrange)
  plt.ylim(-maxrange,maxrange)
  plt.axes().set_aspect('equal')
  plt.show()


#function(22)
if 1:
  for x in range(97):
    if (x is not 0) and x%4==0:
       print x
       try:
         function(x)
       except:
         print "Nooooooo"
