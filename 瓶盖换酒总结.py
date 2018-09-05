ping = 0
gai = 0
empty_jiu = 0
jiu = 0


def drink(i):
    global ping, gai, empty_jiu
    ping = ping + i
    gai = gai + i
    empty_jiu = empty_jiu + i


def swap_jiu():
    global ping, gai, jiu
    jiu = ping//2
    jiu = jiu + gai//4
    ping = ping % 2
    gai = gai % 4
    return jiu


def fun(i):
    global jiu, ping, gai, empty_jiu
    drink(i)
    if gai >= 4 or ping >= 2:
        jiu = swap_jiu()
        fun(jiu)
    else:
        print(empty_jiu)
 #       return empty_jiu#错误，返回None************醒目*********醒目**********************
        return #可以


fun(5)
#总结：fun函数一开始没有达到else语句要求，所以没有返回值，而执行fun的时候又将fun的返回值赋给了a，
#故a为None
