def threeSumClosest( nums, target):
    nums.sort()
    result = float("inf")
    for i in range(len(nums)- 1):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right] + nums[i]
            if abs(sum - target) < abs(result - target):
                result = sum
            if sum < target:
                left += 1
            elif target < sum:
                right -= 1
            else:
                return sum
    return result

    

        
nums = [0,3,97,102,200]
target = 300
print(threeSumClosest(nums,target))


