def do(n,k):
    if k not in n:
        return "-1"
    for i in n:
        if i == k:
            a = n.rindex(i)
    return a

n = input()
k = input()
print(do(n,k))