def do(n):
    if n[::-1] == n:
        return "Yes"
    return "No"
n = input()
print(do(n))