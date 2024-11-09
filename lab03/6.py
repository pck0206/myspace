def count_num(filename):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        count = 0
        lines = file.read()
        for i in lines:
            if i.isdigit():
                count += 1
    print(count)
count_num('text.txt')