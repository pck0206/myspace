def replace(filename,str_word,another_word_str):
    with open(filename , 'r' , encoding = 'utf-8') as file:
        a = file.read()
        b = a.replace(str_word,another_word_str)
        print(b)
replace('text.txt','Pikachu','ronaldo')