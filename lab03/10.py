def count(filename,k):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        contents = file.read()
        a = contents.split()
        b = []
        for i in a:
            if i[-1] == k:
                if i not in b:
                    b.append(i)
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        for i in b:
            print(i,end=" ")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
count('text.txt','r')