def fourSum( nums, target):
        lst = set()
        nums.sort()
        for i in range(len(nums) - 2):
            for k in range(i + 1 , len(nums) - 1):
                left = k + 1
                right = len(nums) - 1
                while left < right:
                    total = nums[i] + nums[k] + nums[left] + nums[right]
                    if total == target:
                        lst.add((nums[i],nums[k],nums[left],nums[right]))
                    if target < total:
                        right -= 1
                    elif target > total:
                        left += 1
                    else:
                        break
        lst = [list(i) for i in lst]
        return lst
nums = [-3,-2,-1,0,0,1,2,3]
target = 0
print(fourSum(nums,target))