def check(lst,oder):
    a = False

    for i in range(len(lst) - 1):
        for k in range(len(min(lst,key=len))):
            if oder.index(lst[i][k]) < oder.index(lst[i + 1][k]):
                a = True
                break
            elif oder.index(lst[i][k]) == oder.index(lst[i + 1][k]):
                continue
            elif oder.index(lst[i][k]) > oder.index(lst[i + 1][k]):
                return False
    return a
lst = ["mesaldo", "messi", "heymar"]
oder = "hlabcidofgjkepqrmstuvwxnyz"
print(check(lst,oder))