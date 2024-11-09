# #0079
# s = input()
# lst = []
# count = []
# p = 0
# a = 0
# for i in s:
#     if i != " ":
#         lst.append(i.lower())
# for k in lst:
#     count.append(int(lst.count(k)))
# for h in lst:
#     if lst.count(h) > p:
#         p = lst.count(h)
#         a = h
#         if p == max(count):
#             break
# b = int(max(count))
# print(f"{a}:{b}")
#
#
# 1102
# N = int(input())
# b = []
# lst = ['in','input','out','output','one','puton']
# boool = True
# while N != 0:
#     a = input()
#     b.append(a)
#     N -= 1
#
# for i in range(len(b)):
#     for j in lst:
#         if j in b[i]:
#             if 'input' in b[i] and j == 'in':
#                 b[i].replace('input',"")
#             elif 'output' in b[i] and j == 'out':
#                 b[i].replace('output',"")
#             else:
#                 b[i].replace(j,"")
#         else:
#             break
#
# for i in range(len(b)):
#     if b[i] == "":
#         print("Yes")
#     else:
#         print("No")



k = int(input())
b=[]
for i in range(k):
    chat = input()
    b.append(chat)
lst = ['input','in','output','out','one','puton']
for i in range(len(b)):
    h = b[i]
    for j in lst:
        if j in h:
             h = h.replace(j,'')
    if len(h) != 0:
        print('NO')
    else:
        print('YES')





