def find_winner(n,k):
    lst = [i for i in range(1 , n + 1)]
    a = lst.copy()
    i = 0
    count = 0
    while len(lst) > 1:
        if i + 1 == k and k <= len(lst):
            lst.remove(lst[i])
            lst = lst[i:]
            lst.extend(a[0:k - 1])
            a = lst.copy()
            i = -1
        elif k > len(lst):
            i = 0
            while len(lst) > 1:
                if count == k - 1:
                    lst.remove(lst[i])
                    lst = lst[i:]
                    lst.extend(a[0:i])
                    a = lst.copy()
                    i = 0
                    count = 0
                i += 1
                count += 1
                if i >= len(lst):
                    i = 0


        i += 1
    return lst[0]
n = 6
k = 5
print(find_winner(n,k))
        

