import numpy as np
def removeElem(inputList, ElementIndex):
    a = list(np.delete(inputList,ElementIndex))
    return a


def LayeredPerm(RemainList,PermList=[0]):
    if not RemainList:
        return PermList
    else:
        return np.hstack([   LayeredPerm(removeElem(RemainList,NextNumIndex),[x*10+NextNumber for x in PermList])
                 for NextNumIndex,NextNumber in enumerate(RemainList)])

print LayeredPerm([0,1,2,3])[1e1-1]
print LayeredPerm([0,1,2,3])
print 1e6-1
print LayeredPerm([0,1,2,3,4,5,6,7,8,9])[1e6-1]

