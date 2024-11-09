def CV(a,b,c):
    k = a + b + c
    return float(k)
def s(a,b,c):
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return f"{s:.3f}"
a,b,c = map(int,input().split())
print(CV(a,b,c),end = " ")
print(s(a,b,c))