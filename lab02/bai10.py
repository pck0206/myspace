lst = list(map(int,input().split()))
k = int(input())
b = []
a = []
for i in range(len(lst)):
    for j in range(i + 1,len(lst)):
        b = []
        if lst[i] + lst[j] == k:
            b.append(lst[i])
            b.append(lst[j])
            a.append(b)

print(a)
