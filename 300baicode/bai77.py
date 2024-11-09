def do(n):
    lst = []
    for i in n:
        if i not in lst:
            lst.append(i)
    print(len(lst))
n = input()
do(n)