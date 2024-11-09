def biggest(height):
    b = False
    c = False
    max = 0
    left = 0
    right = len(height) - 1
    while left < right:
        a = min(height[left], height[right]) * (right - left)
        if a > max:
            max = a
        if b == False:
            right -= 1
        if right == left:
            right = len(height) - 1
            left += 1
    return max

height = [2,3,4,5,18,17,6]
print(biggest(height))