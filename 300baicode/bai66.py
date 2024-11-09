def do(n):
    for i in n:
        if i != " ":
            print(n[n.index(i):])
            break
n = input()
do(n)