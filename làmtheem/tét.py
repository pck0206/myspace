def closest(nums,target):
    min = 4
    lst = []
    for i in range(len(nums)):
        for k in range(i + 1,len(nums)):
            lst.append(nums[i] + nums[k])
    while True:
        if target + i in lst:
            return target - 1
        else:
            i += 1
nums = [-1,2,1,-4]
target = 1
print(closest(nums,target))