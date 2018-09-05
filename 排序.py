# 选择排序
def select_sort(l):
    n = len(l)
    for i in range(n - 1):
        # 内层循环用来比较大小交换元素，一圈确定一个元素
        for j in range(i + 1, n):
            # 如果不合适
            if l[i] > l[j]:
                # 交换两个变量
                l[i], l[j] = l[j], l[i]
    return l
 
# 冒泡排序
def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
