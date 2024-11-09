def give_lines(filename,word):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        lines = file.readlines()
        lst_lines = []
        for line in lines:
            if line != '\n':
                line = line.strip(f'\n')
                lst_lines.append(line)
        for line in lst_lines:
            a = line.lower()
            b = a.split()
            if word in b:
                print(line)
give_lines('text.txt','the')