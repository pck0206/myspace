a = list(map(int,input().split()))
b = [0,1,2,3,4,5,6,7,8,9]
for i in b[0:a[-1]]:
    if not i in a:
        print(i, end = " ")