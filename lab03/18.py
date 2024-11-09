def del_line(filename,n):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        lines = file.readlines()
        lst_lines = []
        for line in lines:
            if line != "\n":
                line = line.strip("\n")
                lst_lines.append(line)
        lst_lines.remove(lst_lines[n - 1])
        for line in lst_lines:
            print(line)
del_line('text.txt' , 5)