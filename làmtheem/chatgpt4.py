def do(nums,k):
    lst = []
    for i in nums:
        bool = True
        for n in lst:
            if n[0] == i:
                n[1] += 1
                bool = False
                break
        if bool :
            lst.append([i,1])
    lst.sort(key = lambda x: x[1], reverse = True)
    p = []
    for h in range(k):
        p.append(lst[h][0])
    return p
nums = list(map(int,input().split()))
k = int(input())
print(do(nums,k))

