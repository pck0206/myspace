def do(n):
    h = str()
    for i in range(len(n)):
        for j in range(i,len(n)):
            for k in range(j,len(n)):
                for l in range(k,len(n)):
                    h = n[i:j] + n[k:l]
                    if h[::-1] == h:
                        if len(h) > 2:
                            return h
    return "0"
n = input()
print(do(n))