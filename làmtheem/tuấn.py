def do(n):
    k = 0
    if n[0] == -1: n[0] = n[1]-(n[2]-n[1])
    if n[1] == -1: n[1] = (n[0] + n[2]) // 2
    if n[2] == -1: n[2] = n[1] + (n[1] - n[0])
    for i in range(len(n)):
        if n[i] > 100:
            n[i] = -1
            k=0
        else:
            k = 1
    print(k,"-",n,end="")
    return
n = list(map(int,input().split()))
do(n)
