def count_array(arrays):
    a = set()
    bool = False
    for i in arrays:
        for k in i:
            a.add(k)
    for i in a:
        for k in arrays:
            if i not in k:
                bool = False
                break
            else:
                bool = True
        if bool:
            print(i)
arrays = [[1,2,3],
          [2,3,5],
          [2,3,9]]
count_array(arrays)
