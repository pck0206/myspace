a = list(map(str,input().split()))
b = list(map(int,input().split()))
for i in range(len(a)):
    for j in range(0,len(a)):
        if b[i] < b[j]:
            a[i],a[j] = a[j],a[i]
            b[i],b[j] = b[j],b[i]
print(a)
