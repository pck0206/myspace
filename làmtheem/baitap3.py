def do(n):
    a = n.copy()
    a.sort()
    if n != a:
        return False
    return True
def lam(n):
    a = n[1] - n[0]
    k = 0
    while True:
        b = n[2+k] - n[1+k]
        k += 1
        if b == a:
            pass
        elif b != a:
            return False
        if k > len(n) - 3:
            break
    return True

n = list(map(int,input().split()))
if lam(n):
    print("ham nay la ham tang dan deu")
else:
    print("ham nay khong phai ham tang dan deu")