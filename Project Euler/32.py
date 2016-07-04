import numpy as np

numbers=np.arange(1,4)

def remove(inlist,value):
    return inlist.remove(value)

def perm(remain,current=[0]):
    out = [perm(np.remove(remain,R),[C*10+R]) for C in current for R in remain]

print numbers
print perm(numbers)
        
