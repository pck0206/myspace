def input_array():
    lst = []
    lst_lst = []
    for i in range(1,10):
        lst.append(i)
        if i % 3 == 0:
            lst_lst.append(lst)
            lst = []
    return lst_lst
print(input_array())