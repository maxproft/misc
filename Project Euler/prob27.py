import numpy as np
def PrimeTest(number):
  if number<0:
      return False
  else:
      a=0
      
      for factortest in np.arange(2,1+int(np.sqrt(number))):
        if number%factortest==0:
            a=1
            break
      if a==0:
        return True
      else:
        return False


MaxAB=0
MaxN=0
MaxA=0
MaxB=0
for a in np.arange(-1000,1001):
    for b in np.arange(-1000,1001):
#if 1:
 #       a=-79
#        b=1601
        n=0
        while PrimeTest(n*n+a*n+b):
            #print n^2+a*n+b
            n+=1

        if MaxN<n:
            MaxN=n
            MaxAB=a*b
            MaxB=b
            MaxA=a
print MaxN
print MaxA
print MaxB
print MaxAB

        
