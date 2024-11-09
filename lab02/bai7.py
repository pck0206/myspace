lst = list(map(int,input().split()))
max = 0
s = str()
a = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in lst:
            b = str(k)
            s += b
        a = int(s)
        if a > max:
            max =  a
        lst[i],lst[j] = lst[j],lst[i]
        s = ""
print(max)