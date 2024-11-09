# def split_square(n):
#     s = 0
#     while n != 0:
#         temp = n% 10
#         s = s + temp**2
#         n= n // 10
#     return s
# def is_happy(n):
#     old_states = [n]
#     while True :
#         n = split_square(n)
#         if n == 1:
#             return True
#         if n in old_states: return False
#         old_states.append(n)
# n = int(input())
# print(is_happy(n))





def check(n):
    s = 0
    while n:
        temp = n % 10
        s += (temp ** 2)
        n //= 10
    return s
def is_happy(n):
    lst = []
    while True:
        n = check(n)
        if n == 1:
            return True
        if n in lst:
            return False
        lst.append(n)
n = int(input())
print(is_happy(n))
