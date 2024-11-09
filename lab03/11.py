def count_letter(filename):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        contents = file.read()
        contents = contents.lower()
        lst = []
        for i in contents:
            if i not in lst:
                lst.append(i)
        for k in lst:
            if k.isalpha():
                print(f"{k}:{contents.count(k)}",end = " ")
count_letter('text.txt')