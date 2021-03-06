题目：在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至
// 少有一个数字是重复的。请找出数组中任意一个重复的数字，
// 例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的
// 输出是重复的数字2或者3。

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

2. 查找数组中的任意一个重复元素，但不能修改这个数组

方法一:
    把数组复制到另一个数组中，数字是几就复制到下标是几的位置，如果复制中间发现某个下标已经有元素了，那这个就是重复元素
    时间复杂度是O(n),空间复杂度是O(n)
方法二：
    把数组复制到字典中，即哈希，复制过程中并查找，查找到了就是重复元素。
    时间复杂度是O(n),空间复杂度是O(n)
方法三：
    类似于二分法，把1到n范围内的数字从中间数m分成两部分，查找数组中在1到m位置的元素个数，如果大于m，则重复数字在1到m范围内，否则在m+1到n的范围内，逐渐缩小范围查找
l = [2, 3, 1, 0, 2, 5, 3]

时间复杂度O(nlogn),空间复杂度O(1)
