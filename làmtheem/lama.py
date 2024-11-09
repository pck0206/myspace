# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
def convert(num):
    roman = ""
    if 1 <= num // 1000 <= 9:
        roman += "M" * (num // 1000)
        num -= (num // 1000) * 1000
    if num // 100 == 9:
        roman += "CM"
        num -= 900
    elif 5 <= num // 100 < 9:
        roman += "D" + "C" * ((num - 500) // 100)
        num = num - 500 - 100 * ((num - 500) // 100)
    elif num // 100 == 4:
        roman += "CD"
        num -= 400
    elif 1 <= num // 100 < 4:
        roman += "C" * (num // 100)
        num -= 100 * (num // 100)
    if num // 10 == 9:
        roman += "XC"
        num -= 90
    elif 5 <= num // 10 < 9:
        roman += "L" + "X" * ((num - 50) // 10 )
        num = num - 50 -((num - 50) // 10) * 10
    elif num // 10 == 4:
        roman += "XL"
        num -= 40
    elif 1 <= num // 10 < 4:
        roman += "X" * (num // 10)
        num -= 10 * (num // 10)
    if num == 9:
        roman += "IX"
    elif 5 <= num < 9:
        roman += "V" + "I" * (num - 5)
    elif num == 4:
        roman += "IV"
    elif 1 <= num < 4:
        roman += "I" * num
    return roman
num = 3749
print(convert(num))

