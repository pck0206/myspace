
def do(n):
    i = 0
    max = 0
    while n:
        a = n % 10
        n //= 10
        if a > max:
            max = a
    return max
def do1(n):
    so = n
    count = 0
    hieu = 1
    while hieu:
        hieu = n - do(n)
        count += 1
        n = hieu
    return count
n = int(input())
print(do1(n))

