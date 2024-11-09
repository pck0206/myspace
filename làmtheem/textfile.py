def check(x) :
    m = x.lower()
    list = []
    for i in m :
        if i in list :
            continue
        else :
            k = m.count(i)
            list.append(i)
            print(f"{i}:{k}" , end = " ")

x = input()
check(x)