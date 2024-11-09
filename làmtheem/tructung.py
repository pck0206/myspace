a = {10:1,20:1,35:2,50:2,55:1,67:1}
tung = 3
truc = 2
left = 0
keys = []
values = []
minroad = float("inf")
i = 0
bl = False
for key,value in a.items():
    keys.append(key)
    values.append(value)
while i < len(a):
    b = values[left:i + 1]
    if b.count(1) >= tung and b.count(2) >= truc:
        if keys[i] - keys[left] < minroad:
            minroad = keys[i] - keys[left]
            bl = True
    else:
        bl = False
    if bl == False:
        i += 1
    elif bl :
        left += 1
print(minroad)
