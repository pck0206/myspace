def sum_lst_lst(lst_lst):
    a = 0
    for i in range(len(lst_lst)):
        a += sum(lst_lst[i])
    return a
lst_lst = []
while True:

    n = list(map(int,input().split()))
    if n == []:
        break
    lst_lst.append(n)
print(sum_lst_lst(lst_lst))