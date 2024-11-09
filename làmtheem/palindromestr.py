def do(s):
    a = ""
    max_len = 0
    left = 0
    right = len(s)
    while left < right:
        a = s[left:right]
        if a[::-1] == a and len(a) > max_len:
            max_len = len(a)
            b = a
        left += 1
        if left == right:
            left = 0
            right -= 1
    return b
str = "babad"
print(do(str))