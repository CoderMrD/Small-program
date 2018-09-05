capCount = 0#瓶盖数
bottleCount = 0#瓶子数
count = 0#已喝瓶子总数
count2 = 0#未喝瓶子总数


#喝酒
def drink(i):
    global capCount,count,bottleCount
    capCount = capCount + i
    bottleCount = bottleCount + i
    count = count+i


#用瓶盖换
def swapCap():
    global capCount
    temp = capCount//4
    capCount = capCount%4
    return temp



#用瓶子换
def swapBottle():
    global bottleCount
    temp = bottleCount//2
    bottleCount = bottleCount%2
    return temp


def fun(i):
    drink(i)
    if capCount < 4 and bottleCount < 2:
        return
    else:
        count2 = swapCap()
        count2 = count2 +swapBottle()
        fun(count2)
fun(5)#喝五瓶,相当于十块钱
print(count)
