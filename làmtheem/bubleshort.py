my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array)
for i in range(n-1):
    min_index = i
    for k in range(i + 1,n):
        if my_array[k] < my_array[min_index]:
            min_index = k
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
print(my_array)