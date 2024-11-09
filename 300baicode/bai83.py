def do(n):
    count = 0
    for i in n:
        if i.islower():
            count += 1
    return count
n = input()
print(do(n))