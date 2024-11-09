def UCLN(a,b):
    if a == 1 and b == 1:
        return 1
    if a != 0 and b != 0:
        for i in range(a + 1 , 2 , -1):
            if a % i == 0 and b % i == 0:
                return f"{int(a/i)}/{int(b/i)}"

a,b = map(int,input().split())
print(UCLN(a,b))