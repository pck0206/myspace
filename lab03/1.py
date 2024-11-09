def read(filename):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        contents = file.read()
        print(contents)
read('text.txt')