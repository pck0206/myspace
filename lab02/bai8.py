n = int(input())
lst = []
while n:
    k = list(map(int,input().split()))
    k.reverse()
    lst.append(k)
    n -= 1

for i in range(len(lst)):
    for k in range(len(lst[i])):
        if lst[i][k] == 0:
            lst[i][k] = 1
        else:
            lst[i][k] = 0
print(lst)