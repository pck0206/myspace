def xap_sep (x) :
    s = []
    num = x[0]
    for i in range(len(x)) :
        if x[i] > num :
            num = x[i]
            s.append(num)
    return s
lst = list(map(int,input().split()))
xap_sep(lst)