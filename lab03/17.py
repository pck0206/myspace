def insert_line(filename,str,n):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        lines = file.readlines()
        lst_lines = []
        for line in lines:
            if line != '\n':
                line = line.strip('\n')
                lst_lines.append(line)
        lst_lines.insert(n - 1,str)
        for new_line in lst_lines :
            print(new_line)
insert_line('text.txt' , 'messi la sati' , 4)
