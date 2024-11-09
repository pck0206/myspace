# def zigzag(strike,numrows):
#     a = numrows * 2 - 2
#     res = ""
#     for i in range(numrows):
#         ct = numrows * 2 - 2
#         for k in range(i,len(strike),ct):
#             res += strike[k]
#             if i > 0 and i < numrows - 1 and k + a - 2 * i < len(strike):
#                 res += strike[k + a - 2 * i]
#     return res
# strike = "ABCD"
# numrows = 3
# print(zigzag(strike,numrows))




# s = input()
# numRows = int(input())
# lst = [[] for _ in range(numRows)]
# idx = 0
# i = 0
# while i < len(s):
#   if idx == 0:
#     down = True
#     up = False
#   elif idx == numRows - 1:
#     up = True
#     down = False
#   if down:
#     lst[idx].append(s[i])
#     i += 1
#     idx += 1
#   if up:
#     lst[idx].append(s[i])
#     i += 1
#     idx -= 1
# ans = ""
# for i in lst:
#   ans += ''.join(i)
# print(ans)


string = input()
n = int(input())
lst = [[] for i in range(n)]
idx = 0
down = True
a = ""
for i in string:
    lst[idx].append(i)
    if idx == n - 1:
        down = False
    if idx == 0:
        down = True
    idx += 1 if down else -1
for i in lst:
    for k in i:
        a += k
print(a)







