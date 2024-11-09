def most_word(filename):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        count = 100
        lines = file.read()
        b = lines.split()
        for i in b:
            if b.count(i) < count:
                count = b.count(i)
                a = i
    print(a)
    print(count)

most_word('text.txt')

