import random
highest_num = 100
lowest_num = 1
num = int(input("the number you guess is :"))
b = random.randint(lowest_num,highest_num)
score = 0

while True:
    if num == b:
        print("|-------------|")
        print('|Wow ! correct|')
        print('|-------------|')
        break
    else:
        if num == -1:
            print('|---------|')
            print("|YOU LOSE |")
            print("|---------|")
            print("The correct number is :",b)
            break
        print('Wrong')
        if num < b:
            print("Bigger")
        if num > b:
            print("Smaller")
        num = int(input("the number you guess is :"))
    


