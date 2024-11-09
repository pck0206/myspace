def longest_word(filename):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        l = 0
        lines = file.readlines()
        lines = [line for line in lines if line != '\n']
        for i in lines:
            a = i.split()
            for p in a:
                if len(p) > l:
                    l = len(p)
                    b = p
    print(b[:-1])
longest_word('text.txt')
