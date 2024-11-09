def copy_text(lst):
    with open('output2.txt', 'w' , encoding = 'utf-8') as file:
        for i in lst:
            if i == lst[-1]:
                file.write(i)
            else:
                file.write(i + " ")
lst = list(map(str,input().split()))
copy_text(lst)
