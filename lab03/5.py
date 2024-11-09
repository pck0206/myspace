def shortest_word(filename):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        l = 100
        lines = file.readlines()
        lines = [line for line in lines if line != '\n']
        for i in lines:
            a = i.split()
            for k in a:
                if len(k) < l:
                    l = len(k)
                    b = k
    print(b)
shortest_word('text.txt')