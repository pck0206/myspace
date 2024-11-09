def shift(x,n):
    while n :
        b = x.pop()
        x.insert(0,b)
        n -= 1
    return x
x = list(map(int,input().split()))
n = int(input())
print(shift(x,n))