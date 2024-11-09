# def determine(a):
#     lst = []
#     lst1 = []
#     count = 0
#     for i in a:
#         if i not in lst:
#             lst.append(i)
#     for i in lst:
#         if a.count(i) > count:
#             count = a.count(i)
#             b = i
#     lst1.append(b)
#     lst.remove(b)
#     for i in lst:
#         if a.count(i) == count:
#             lst1.append(i)
#     for i in lst1:
#         print(i,end=" ")
#     print()
#     c = []
#     d = []
#     for i in range(len(a)):
#         if a[i] >= 50:
#             c.append(a[i])
#         else:
#             c = []
#         if len(c) > len(d):
#             d = []
#             for k in c:
#                 d.append(k)
#
#         elif len(c) == len(d):
#             print(c)
#     print(d)
#
# a = list(map(int,input().split()))
# determine(a)






def do(n):
    count = 0
    lst = []
    list_maxcount = []
    for i in n:
        if i not in lst:
            lst.append(i)
    for k in lst:
        if n.count(k) > count:
            count = n.count(k)
    for h in lst:
        if n.count(h) == count:
            print(h,end = ' ')
def do1(n):
    list1 =[]
    list_fake = []
    for i in n:
        if i >= 50:
            list1.append(i)
        else:
            list_fake.append(list1)
            list1 = []
    for k in range(len(list_fake)





