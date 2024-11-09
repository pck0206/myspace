a = list(map(int,input().split()))
max = 2
b = 0
m = []
for i in a:
    k = a.count(i)
    if k > max:
        m.append(i)
        max = k
        b = i
        for l in range(a.count(i)):
            a.remove(i)
    elif k == max:
        m.append(i)
        for l in range(a.count(i)):
            a.remove(i)
    else:
        for l in range(a.count(i)):
            a.remove(i)

for h in m:
    print(h,end = " ")


