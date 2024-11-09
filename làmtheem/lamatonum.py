def convert(s):
    num = 0
    while s != "":
        if "CM" in s:
            num += 900
            s = s.replace("CM","",1)
        if "M" in s :
            num += 1000
            s = s.replace("M","",1)
        if "CD" in s:
            num += 400
            s = s.replace("CD","",1)
        if "D" in s:
            num += 500
            s = s.replace("D","",1)
        if "XC" in s:
            num += 90
            s = s.replace("XC","",1)
        if "C" in s:
            num += 100
            s = s.replace("C","",1)
        if "XL" in s:
            num += 40
            s = s.replace("XL","",1)
        if "L" in s:
            num += 50
            s = s.replace("L","",1)
        if "IX" in s:
            num += 9
            s = s.replace("IX","",1)
        if "X" in s:
            num += 10
            s = s.replace("X","",1)
        if "IV" in s:
            num += 4
            s = s.replace("IV","",1)
        if "V" in s:
            num += 5
            s = s.replace("V","",1)
        if "I" in s:
            num += 1
            s = s.replace("I","",1)
    return num
s = "CMLII"
print(convert(s))