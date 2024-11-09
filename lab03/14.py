def print(filename,word):
    with open(filename , 'r' , encoding= 'utf-8') as file:
        lines = file.readlines()
        lines =[line for line in lines if lines != '\n']

        count = 0
        for i in lines:
            i = i.lower()
            a = i.split()
            for k in range(len(a)):
                if k + 2 <= len(a):
                    if a[k + 1] == word and lines.count(k) > count:
                        count = a.count(k)
                        b = a[k]
    print(b)
print('text.txt','pikachu')