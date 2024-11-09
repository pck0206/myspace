def do(n):
    a = n.split()
    a.reverse()
    for i in a:
        print(i,end = " ")
n = input()
do(n)