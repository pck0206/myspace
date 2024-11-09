# def check(nums1,nums2):
#     nums1.extend(nums2)
#     nums = nums1
#     nums.sort()
#     if len(nums) % 2 == 0:
#         med = (nums[(len(nums) // 2) - 1] + nums[(len(nums) // 2)]) / 2
#     elif len(nums) % 2 != 0:
#         med = nums[len(nums) // 2]
#     return float(med)
# nums1 = [1,2]
# nums2 = [3,4]
# print(check(nums1,nums2))


# nums = [1,1,2]
# a = []
# for i in nums:
#     for k in range(nums.count(i) - 1):
#         nums.remove(i)
#         nums.append("_")
# for i in nums:
#     if type(i) == int:
#         a.append(i)
# print(len(a),nums)


# nums = [3,2,2,3]
# val = 2
# for i in range(nums.count(val) - 1):
#     nums.remove(val)
# print(len(nums))
#


n = 2
a = str(n)
c = 0
bool = False
if n > 1:
    while c < n:
        if bool:
            for i in a:
                b = str(a.count(i)) + i
                a = a.replace(i * a.count(i),b,1)
                c += 1
                if c == n:
                    break
        if len(a) == 1:
            a = a.replace(a[0],"1")
            bool = True
    print(a)
else:
    print(a)



