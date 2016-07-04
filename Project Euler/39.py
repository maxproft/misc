
bestPerim=0
bestNum=0


for perim in range(1001):
    num=0
    for a in range(perim+1):
        for b in range(perim-a+1):
            c=perim-a-b
            if a*a+b*a==c*c:
                num+=1
    if bestNum<num:
        bestNum=num
        bestPerim=perim

print bestPerim,bestnum
                    
                
