total=1
n=1
delta=2

while delta<1001:
    for x in range(4):
        n+=delta
        total+=n
    delta+=2
        
print total
