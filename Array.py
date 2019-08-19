1. 查找列表中的任意一个重复元素
l = [2, 3, 1, 0, 2, 5, 3]
def duplicate(l: list):
    if not isinstance(l, list):
        return "Please input list"
    for i in range(len(l)):
        while i != l[i]:
            temp = l[i]
            if l[temp] != temp:
                l[i], l[temp] = l[temp], l[i]
            else:
                return temp
    return None
时间复杂度O(n),空间复杂度O(1)
