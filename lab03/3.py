def read_last(filename,n):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        a = []
        b = []
        lines = file.readlines()
        lines = [line for line in lines if line != '\n']
        lines.reverse()
        for k in range(n):
            b.append(lines[k])
        b.reverse()
        for h in b:
            print(h , end = "")
read_last('text.txt' , 4)
