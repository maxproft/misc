import numpy as np

InputArray = np.loadtxt('p067_triangle.csv',delimiter=',')
XDimArray,YDimArray=np.shape(InputArray)

print InputArray

def MaxPrevOpt(ElementPosition,RowLen,PreviousRow):
        if ElementPosition==0:
            return PreviousRow[0]
        elif ElementPosition==RowLen-1:
            return PreviousRow[ElementPosition-1]
        elif ElementPosition>RowLen-1:
            return 0
        else:
            return max(PreviousRow[ElementPosition],PreviousRow[ElementPosition-1])

def ReduceRow(RowLen,CurrentRow,PreviousRow):
    return [MaxPrevOpt(ElementPosition,RowLen,PreviousRow)+CurrentRow[ElementPosition]
               for ElementPosition in range(len(CurrentRow))]


PreviousRow=InputArray[0,]

for CurrentRow in range(XDimArray-1):
    PreviousRow = ReduceRow(CurrentRow+2, InputArray[CurrentRow+1,:],PreviousRow)

print max(PreviousRow)
        

