def do(n,k):
    if k not in n:
        return -1
    return n.index(k)
n = input()
k = input()
print(do(n,k))