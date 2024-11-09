lst = list(map(int,input().split()))
k = int(input())
min = max(lst)
m = len(lst) - 1
for i in range(k):
    if k == 1:
        break
    elif lst[m] < min:
        min = lst[m]
    m -= 1
print(min)