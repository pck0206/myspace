def do(n):
    a = n.split()
    b = []
    for i in range(len(a)):
        c = a[i]
        b.append(c[::-1])
    for i in b:
        print(i,end = " ")
n = input()
do(n)