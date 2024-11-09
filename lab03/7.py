def count_letter(filename):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        a = file.read()
        b = a.lower()
        c = b.split()
        lst = []
        for i in c:
            if i not in lst :
                if "." in i or "," in i:
                    lst.append(i[:-1])
                else:
                    lst.append(i)
        for i in lst:
            print(f"{i}:{lst.count(i)}",end = " ")
count_letter('text.txt')