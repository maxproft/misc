
text_file = open("words", "r")
lines = text_file.readlines()
text_file.close()

totwords = len(lines)


maxnum = 3 #maximum number allowed not on homerow


def testword(word):
    test="'pyfgcrlqjkxbmwvz"#dvorak
    #test="'qwertyuiopzxcvbnm" #qwerty
    a=0
    for let in test:
        if let in word:
            if a==maxnum:
                return False
            a+=1
            
    return True

print "beginning test"
homewords = [word[:-1]for word in lines if testword(word)]

print totwords, len(homewords)

wordlen = [len(word)-1 for word in lines if "'" not in word]

import matplotlib.pyplot as plt
plt.xkcd() 
plt.hist(wordlen,bins=max(wordlen))
plt.title("")
plt.xlabel("word length")
plt.ylabel("Frequency")
plt.show()
