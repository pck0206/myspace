def do(n):
    lst = []
    a = n.lower()
    for i in range(len(n)):
        if a[i] in lst:
            continue
        else:
            print(f"{a[i]}:{a.count(a[i])}",end = " ")
            lst.append(a[i])
n = input()
do(n)