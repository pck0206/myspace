def read_first(filename,n):
    with (open(filename , 'r' , encoding = 'utf-8') as file):
        lines = file.readlines()
        lines = [line for line in lines if line != '\n']
        for i in range(n):
            print(lines[i].strip())
n = int(input())
read_first('text.txt',n)