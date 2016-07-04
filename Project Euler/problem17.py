import numpy as np


#for x in range(1000):




SNL={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}#Single Number Length, number:length of number

#Teens difference list
TDL={0:2,1:2,2:2,3:2,4:1,5:2,6:1,7:1,8:2,9:1}

HundredWordLength=10
TensWordLength=2



def NumToLength(CurrentNumber,SNL=SNL,TDL=TDL):
    TotalNumChar=0
    NumHund = int(CurrentNumber/100)
    NumTens = int(CurrentNumber/10)%10
    NumUnits = CurrentNumber%10
    
    TotalNumChar+= SNL[NumHund]+HundredWordLength+SNL[NumTens]+TensWordLength+SNL[NumUnits]

    if NumHund==0:
        TotalNumChar-=HundredWordLength
    if NumTens==0:
        TotalNumChar-=TensWordLength
        if NumHund!=0:
            if NumUnits==0:
                TotalNumChar-=3
    if NumTens==1:
        TotalNumChar-=TDL[NumUnits]
    if NumTens==2:
        TotalNumChar+=1
    if NumTens==3:
        TotalNumChar-=1
    if NumTens==4:
        TotalNumChar-=1
    if NumTens==5:
        TotalNumChar-=1
    if NumTens==8:
        TotalNumChar-=1
    return TotalNumChar
    

print NumToLength(100)
    


TotalNumChar=0
for CurrentNumber in range(1000):
    TotalNumChar+=NumToLength(CurrentNumber)
#Adding in a thousand
TotalNumChar+=11
print TotalNumChar


#Zero Hundred
#Zero tens
#twenty
#thirty
#forty
#fifty


#10 3 5
#11 6 8
#12 6 8
#13 8 10
#14 8 9
#15 7 9
#16 7 8
#17 9 10
#18 8 10
#19 8 9



