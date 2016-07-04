import numpy as np


def keyerr(dictionay,key):
    try:
        dictionay[key]
        return True
    except KeyError:
        return False

maxdiv=0
lendiv=0

for div in np.arange(1,10001):
    RemIndex={}
    index=0
    Remainder=1
    while keyerr(RemIndex,Remainder)==False:
        RemIndex[Remainder]=index
        index+=1
        Remainder=10*Remainder%div
    if lendiv < index-RemIndex[Remainder]:
        maxdiv=div
        lendiv=index-RemIndex[Remainder]
print maxdiv, lendiv
    
