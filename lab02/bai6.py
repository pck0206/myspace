a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = b + a
print(c)
for i in range(len(c)):
    for j in range(i,len(c)):
        if c[i] > c[j]:
            c[i], c[j] = c[j], c[i]
print(c)