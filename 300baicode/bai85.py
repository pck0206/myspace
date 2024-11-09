def do(n):
    a = n.split()
    b = len(a)
    for i in range(b - 1):
        print(a[i],end = " ")
n = input()
do(n)