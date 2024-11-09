def check(nums):
    right = len(nums) - 1
    nums.sort()
    lst_sum = []
    for i in range(len(nums)) :
        if nums[i] == nums[i - 1] and i > 0:
            continue
        else:
            right = len(nums) - 1
            left = i + 1
            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    lst_sum.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
    return lst_sum
lst = [-1,0,1,2,-1,-4]
print(check(lst))