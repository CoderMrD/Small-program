import time
s = """[ti:蓝莲花]
[ar:许巍]
[al:留声十年绝版青春北京演唱会]
[00:-01.70]蓝莲花
[00:-00.70]演唱：许巍
[00:00.00]
[00:00.70]没有什么能够阻挡
[00:06.01]你对自由的向往
[00:11.43]天马行空的生涯
[00:16.99]你的心了无牵挂
[00:21.20]
[02:11.55][01:50.60][00:22.63]穿过幽暗的岁月
[02:16.93][01:55.60][00:27.81]也曾感到彷徨
[02:22.21][02:01.09][00:33.13]当你低头的瞬间
[02:27.62][02:06.33][00:38.32]才发觉脚下的路
[02:31.64][02:10.23][00:42.37]
[02:32.97][00:43.79]心中那自由的世界
[02:38.23][00:49.50]如此的清澈高远
[02:43.30][00:54.31]盛开着永不凋零
[02:47.70][00:58.50]蓝莲花
[02:53.95][03:00.06][01:05.41]"""
dict0 = {} #定义一个空字典,存放歌词信息
dict1 = {} #存放歌曲信息
c = 0
b = 0
l = s.splitlines()#按行分割后，得到一个列表
for i in l:#对得到的列表进行遍历，i是l列表的元素，是一个个新的列表
    if i[1].isdecimal():#不写下标则默认为0，i[0]
        l0 = i.split(']')#对新列表按照右中括号分割，歌词与时间分开
        l1 = l0[-1]#提取歌词到列表
        l2 = l0[:-1]#提取时间到列表
        for j in l2:#对时间列表进行遍历,列表分成了字符串(对每一个l2进行遍历，
            # 多个时间的多遍历几次，从而歌词与时间匹配时多个相同歌词进行匹配)
            l3 = j.strip('[')#去左框，得到字符串
            l4 = l3.split(':')#字符串分割成列表
            time = float(l4[0]) * 60 + float(l4[1])
            dict0[time] = l1
    else:
# [ti:蓝莲花]
# 去掉两边的[]
        i = i.strip('[]')
        i = i.split(':')#冒号分割
        if i[0] == 'ti':
            dict1['标题'] = i[1]
        elif i[0] == 'ar':
            dict1['艺术家'] = i[1]
        elif i[0] == 'al':
            dict1['专辑'] = i[1]

time_list = list(dict0.keys())#提取时间信息
time_list.sort(reverse=True)
#time_list = time_list[::-1]#倒序，-1为步进值

# 封装函数显示歌曲信息
def show_song_info(info_dict):
    for key in info_dict:
        print(key, ':', info_dict[key])


import time
import os

t = 0

while True:
    for i in time_list:
        if i < t:
            os.system('cls')
            show_song_info(dict1)
            print(dict0[i])
            break
    t += 0.5
    time.sleep(0.5)
