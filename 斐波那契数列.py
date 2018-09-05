#Fibonacci sequence斐波那契数列
def fab(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fab(n-1)+fab(n-2)
def feibo(i):
    for a in range(1,i+1):
        print(fab(a),end=',')
feibo(9)
