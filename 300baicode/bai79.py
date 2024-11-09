def do(n):
    n = n.lower()
    a = []
    b = []
    count = 0
    for i in n:
        if i != " ":
            if i in a:
                b.append(n.count(i))
                continue
            else:
                a.append(i)

    for k in a:
        if n.count(k) > count:

            count = n.count(k)
        if n.count(k) == max(b):
            print(f"{k}:{n.count(k)}")
            break
n = input()
do(n)