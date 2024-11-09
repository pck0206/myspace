def write(filename,target_filename,n,k):
    with open(filename,'r' , encoding = 'utf-8') as file:
        a = file.readlines()
        lines = [line for line in a if a != '\n']
    with open(target_filename , 'w' , encoding = 'utf-8') as f:
        for i in range(n,k + 1):
            f.write(lines[i])
write('text.txt','newtext.txt',3,7)