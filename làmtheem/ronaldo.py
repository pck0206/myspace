def closest(nums,target):
    lst = []
    for i in range(len(nums)):
        for k in range(i + 1, len(nums)):
            for h in range(k + 1, len(nums)):
                lst.append(nums[i] + nums[k] + nums[h])
    a = lst.copy()
    for j in a:
        for n in range(a.count(j) - 1):
            a.remove(j)
        if len(a) == 1:
            return j
    for i in range((target + 1)** 100):
        if target in lst:
            return target
        elif target + i in lst:
            return target + i
        elif target - i in lst:
            return target - i
nums = [-1,2,1,-4]
target = 1
print(closest(nums,target))