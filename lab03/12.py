def count_word(filename,a,b):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        c = file.read()
        c = c.split()
        d = []
        p = []
        for i in c :
            i = i.lower()
            if "." in i or "," in i:
                d.append(i[:-1])
            else:
                d.append(i)
            if i not in p:
                p.append(i)
        for i in p:
            if a < d.count(i) < b:
                print(i)
a,b =   map(int,input().split())
count_word('text.txt' , a , b)