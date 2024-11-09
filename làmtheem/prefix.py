def check(strs):
    left = 0
    right = 1
    prefix = ""
    b = min(strs, key=len)
    if len(strs) == 1:
        return strs[0]
    while right <= len(min(strs,key = len)):

        a = b[left:right]
        for i in strs:
            if i.startswith(a):
                prefix = a
            else:
                prefix = b[left:right - 1]
                return prefix
        right += 1
    return prefix
strs = ["flower","flow","flight"]
print(check(strs))
