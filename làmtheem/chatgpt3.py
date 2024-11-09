def check(n):
    if n.isupper() :
        return True
    return False
def do(n):
    upper = 0
    lower = 0
    for i in n:
        if check(i):
            upper += 1
        else:
            lower += 1
    return upper, lower
n = input()
print(do(n))