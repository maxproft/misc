import numpy


MonthLength={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

CurrentDay=-29 #0 is sunday
NumSundays=0

for AlmostYear in range(99):
    Year=AlmostYear+1
    for AlmostMonth in range(12):
        Month=AlmostMonth+1
        if int(Year/4)*4==Year and Month==3:#if leap year
            CurrentDay=(CurrentDay+MonthLength[Month]+1)%7
        else:
            CurrentDay=(CurrentDay+MonthLength[Month])%7
        if CurrentDay==0:
            print Year,Month
            NumSundays+=1

print NumSundays
            
                        
        
