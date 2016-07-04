
coins=[1,2,5,10,20,50,100,200]


num=0

for one in range(201):
    print one
    for two in range(int((200-one)/2)+1):
        for five in range(int((200-one-two*2)/5)+1):
            for ten in range(int((200-one-two*2-five*5)/10)+1):
              for twen in range(int((200-one-two*2-five*5-ten*10)/20)+1):
                for fifty in range(int((200-one-two*2-five*5-ten*10-twen*20)/50)+1):
                    for hund in range(int((200-one-two*2-five*5-ten*10-twen*20-fifty*50)/100)+1):
                        for twohund in range(int((200-one-two*2-five*5-ten*10-twen*20-fifty*50-hund*100)/200)+1):
                            total=one*1+two*2+five*5+ten*10+twen*20+fifty*50+hund*100+twohund*200
                            if total==200:
                                num+=1
print num
