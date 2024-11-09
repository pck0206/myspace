s = input()
k = str()
a = float(s)
b = int(a)
boool = True
if len(str(int(a))) <= 3:
    k = s
for i in range(len(s)):
    k += s[i]
    if len(str(b)) == 7 and  i == 0:
        k += ","
        boool = False
    elif i == 3:
        k += ","
if boool == True:
    k = str()
    for o in range(len(s)):
        k += s[o]
        if len(str(b)) == 6:
            if o == 2:
                k += ","
if "." in k and int(k[int(k.index("."))+1:]) == 0:
    k.remove(".")
    k.remove(k[int(k.index("."))+1:])
print(k)