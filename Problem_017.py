#Number letter counts
import math
tot = 0
def digitval(j):
    valone = 0
    if j == 4 or j == 5 or j == 9:
        valone = 4
    elif j == 1 or j == 2 or j == 6:
        valone = 3
    elif j == 3 or j == 7 or j == 8:
        valone = 5
    return valone
def tensval(j):
    valten = 0
    if j == 1:
        valten = 3
    elif j == 4 or j == 5 or j == 6:
        valten = 5
    elif j == 2 or j == 3 or j == 8 or j == 9:
        valten = 6
    elif j == 7:
        valten = 7  
    return valten
n = 1000
for i in range(1,n + 1):
    #Hundreds place
    if i == 1000:
        tot = tot + 11
    else:
        if i > 99 and i < 1000 and i % 100 == 0:
            tot = tot + 7 #"hundred"
            j = i // 100 #find hundreds place
            tot = tot + digitval(j)
        elif i > 99 and i < 1000 and i % 100 != 0:
            tot = tot + 10 #"hundred and"
            j = i // 100 #find hundreds place
            tot = tot + digitval(j)
        #Tens place
        if i % 100 > 10 and i % 100 < 20:
            j = i % 100
            #11-19
            if j == 11 or j == 12:
                tot = tot + 6
            elif j == 15 or j == 16:
                tot = tot + 7
            elif j == 13 or j == 14 or j == 18 or j == 19:
                tot = tot + 8
            elif j == 17:
                tot = tot + 9
        else: #number is not between 11-19 inclusive
            j = (i % 100)//10
            tot = tot + tensval(j)
            #Ones place
            j = i % 10
            tot = tot + digitval(j)
print(tot)


