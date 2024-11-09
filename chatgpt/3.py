def min_max(lst_lst):
    min = lst_lst[0][0]
    max = 0
    for i in range(len(lst_lst)):
        a,b = int(max(lst_lst[i])),int(min(lst_lst[i]))

        if a) z> max:
            max = max(a)
        if min(a) < min:
            min = min(a)
    return min,max
lst_lst = [[1,2,3],[4,5,6]]
print(min_max(lst_lst))