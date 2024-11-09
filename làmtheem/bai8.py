
def do(n):
    a = str(n)
    totalodd = 0
    totaleven = 0
    i = 0
    k = 1
    while i < len(a):
        h = a[i]
        b = int(h)
        i += 2
        totalodd += b
    while k < len(a):
        b = int(a[k])
        k += 2
        totaleven += b
    if totalodd > 0:
        print(totalodd)
    if totaleven > 0:
        print(totaleven)
n = int(input())
do(n)

