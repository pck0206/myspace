def longest_str(s):
    left = 0
    a = set()
    max_lenght = 0
    for right in range(len(s)):
        if s[right] not in a:
            a.add(s[right])
            max_lenght = max(max_lenght,right - left + 1)
        else:
            while s[right] in a:
                a.remove(s[left])
                left += 1
            a.add(s[right])
    return max_lenght
str = "abcabcbb"
print(longest_str(str))

