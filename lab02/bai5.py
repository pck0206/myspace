lst = list(map(int,input().split()))
for i in range(len(lst)):
    for j in range(i,len(lst)):
        if i + 2 <= len(lst):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
print(lst)
lst[-1] = lst[-1] + 1
for i in lst:
    print(i,end="")