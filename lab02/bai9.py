lst = list(map(int,input().split()))
lst.sort()
a = []
for i in range(len(lst)):
    if lst[i] == lst[i-1]:
        continue
    for j in range(i + 1,len(lst)):
        if lst[j] == lst[j - 1]:
            continue
        for k in range(j + 1,len(lst)):
            if lst[j] == lst[j -1]:
                continue
            if lst[i] + lst[j] + lst[k] == 0:
                a.append([lst[i],lst[j],lst[k]])
print(a)