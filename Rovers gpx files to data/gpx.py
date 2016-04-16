import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import datetime



tree = ET.parse('20160416.gpx')
gpx = tree.getroot()

#print "gpx.tag"
#print gpx.tag
#print gpx.attrib

# get the following string by looking at the top,
# xmlns="http://www.topografix.com/GPX/1/1"
#put string inside curly brackets

string = "{http://www.topografix.com/GPX/1/1}"

for trk in gpx:
    for trkseg in trk:
        for trkpt in trkseg:
            lat = float(trkpt.attrib['lat'])
            lon = float(trkpt.attrib['lon'])
            #print lat,lon
            for eletime in trkpt:
                if eletime.tag == string+'time':
                    time = eletime.text
                if eletime.tag == string+'ele':
                    elevation = float(eletime.text)
            #print lat,lon,time,elevation
            try:
                data.append([lat,lon,time,elevation])
            except NameError:
                data=[[float(lat),float(lon),time,float(elevation)]]
data = np.array(data)

#Scatter Plot of position
if 1:
    plt.plot(data[:,0],data[:,1])
    plt.title("Where I Ran (lat/long)")
    plt.show()

#Convert date to a useable format
if 0:
    s=time
    print s
    print "%Y-%m-%dT%H:%M:%SZ"
    print datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").timetuple()

if 1:
    radearth=6371*1000 #in meters
    distance=[radearth*6.28/360*
              ((float(data[i,0])-float(data[i+1,0]))**2+(float(data[i,1])-float(data[i+1,1]))**2)**0.5
              for i in range(len(data[:,0])-1)]
    cumdist=np.cumsum(distance)
    speed=[min(x,5) for x in abs(cumdist[1:]-cumdist[:-1])/30.] #30s between measurements
    #ceiling is there, as GPS will jump when it gets a signal.
    
    FirstTime=int(datetime.datetime.strptime(data[0,2], "%Y-%m-%dT%H:%M:%SZ").strftime("%s"))
    times = [int(datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").strftime("%s"))-FirstTime for x in data[:-2,2]]
    

    plt.plot(times,speed)
    plt.title("Speed at different times")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (m/s)")
    plt.show()
    


#Plot cummulative distance against time:
if 1:
    radearth=6371*1000 #in meters
    distance=[radearth*6.28/360*
              ((float(data[i,0])-float(data[i+1,0]))**2+(float(data[i,1])-float(data[i+1,1]))**2)**0.5
              for i in range(len(data[:,0])-1)]
    cumdist=np.cumsum(distance)
    FirstTime=int(datetime.datetime.strptime(data[0,2], "%Y-%m-%dT%H:%M:%SZ").strftime("%s"))
    times = [int(datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").strftime("%s"))-FirstTime for x in data[:-1,2]]
    altitude = data[:-1,3]
    print "Distance Run: " + str(int(cumdist[-1]))+ "m"
    print "Time Running: " + str(int(times[-1]))+"s"
    print "Average Speed: "+str(round(cumdist[-1]/times[-1], 2))+"m/s"

    fig, ax1 = plt.subplots()
    
    ax1.plot(times,cumdist,'b-')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Distance (m)', color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
    
    ax2 = ax1.twinx()
    ax2.plot(times,altitude,'r-')
    ax2.set_ylabel('Altitude (m)', color='r')
    for tl in ax2.get_yticklabels():
        tl.set_color('r')
    plt.show()

    
    plt.plot(cumdist,altitude)
    plt.title("Altitude vs Distance")
    plt.show()



