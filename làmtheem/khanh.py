def threeSumClosest( nums: list[int], target: int) -> int:
        nums.sort()
        print(nums)
        left = 0
        right = len(nums)-1
        min_value = float('inf')
        sum_dict = {}
        while left + 1 < right :
            if nums[left] + nums[right] + nums[left+1] < target < nums[right] + nums[left] + nums[right-1] :
                for i in range(left+1,right ) :
                    min_value = min(min_value, abs(nums[left] + nums[right] + nums[i] - target))
                    sum_dict[min_value] = nums[left] + nums[right] + nums[i]
                left += 1
                right -= 1
            elif nums[right] + nums[left] + nums[right-1] <= target :
                min_value = min(min_value, abs(nums[left] + nums[right] + nums[right-1] - target))
                sum_dict[min_value] = nums[left] + nums[right] + nums[right-1]
                left += 1
            elif nums[left] + nums[right] + nums[left+1] >= target :
                min_value = min(min_value, abs(nums[left] + nums[right] + nums[left+1] - target))
                sum_dict[min_value] = nums[left] + nums[right] + nums[left+1]
                right -= 1
            if min_value == 0 :
                break
                return sum_dict[0]

        return sum_dict[min_value]
nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2 
print(threeSumClosest(nums,target))