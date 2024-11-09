def reverse(x):
    if -2 ** 31 <= x <= (2 ** 31) - 1:
        if len(str(x).strip("-")) > 1:
            if x < 0:
                a = str(x).strip("-")
                a = "-" + a[::-1]
            elif x > 0:
                a = str(x)[::-1]
        else:
            a = x
        if -2 ** 31 <= int(a) <= (2 ** 31) - 1:
            return a
    else:
        return 0
x = 123
print(reverse(x))
