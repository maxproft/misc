import numpy as np
import matplotlib.pyplot as plt

def commonFactor(aFacters,b):
    common=True
    for x in aFacters:
        if b%x==0:
            common=False
            break
    return common

primes=[2,3,5,7,11,13,17,19]#,23]#,29,31,37,41]
def prodfunc(primes,index):
    tot=1
    for x in primes[:index+1]:
        tot=tot*x
    return tot
prodprime=[prodfunc(primes,index) for index in range(len(primes))]

def Res(denom):
    propnum=1
    aaaaaFacters=[x for x in np.arange(2,1+int(np.sqrt(denom))) if denom%x==0]
    bbbbbFacters=[denom/x for x in aaaaaFacters]
    aFacters=np.concatenate([aaaaaFacters,bbbbbFacters])

    for numer in np.arange(2,denom):
        if commonFactor(aFacters,numer):
            propnum+=1
    return propnum/(denom-1.)

print Res(210)
print Res(44100)
print Res(120)

#plotdata=[Res(x) for x in np.arange(2,100)]
plotdata=[Res(x) for x in prodprime]
print plotdata
upper=1
plt.plot([x if x<upper else upper for x in plotdata],'ro')
plt.show()

#denom=60
denom=12252240
dddd=denom
limit=15499/94744.
#limit=4/10.
print limit
#while Res(denom)>=limit:
for a in range(10):
    #print denom,Res(denom)
    resres=Res(dddd)
    print dddd,resres
    dddd+=denom
print denom,Res(denom)
