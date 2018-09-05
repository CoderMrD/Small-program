#Method1利于计数函数count
mylist = [2, 1, 2, 2]
myset = set(mylist)  #强制转换成没有重复元素的集合
for i in myset:
  a = d.count(i)
  if a > 1:
    print(a)
    
#Method2求列表与集合的差
mylist = [2, 1, 2, 2]
myset = set(mylist)
print(mylist - myset + 1)

#Methon3利用字典
List=[1,2,2,2,2,3,3,3,4,4,4,4]
a = {}
for i in List:
  if List.count(i)>1:
    a[i] = List.count(i)
print(a)
