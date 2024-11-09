def check(n):
    if n[::-1] == n:
        return True
    return False
def do(n):

    k = []
    for i in range(len(n)):
        for j in range(i + 1,len(n)):
            b = n[i:j]
            if check(b) and len(b) > 1:
                k.append(b)

    return k
n = input()
print(do(n))
