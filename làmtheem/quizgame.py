questiones = [['1.Ronaldo mang áo số mấy'],
              ['Ronaldo nhà ở đâu'],
              ['Ronaldo có mấy quả bóng vàng'],
              ['Ronaldo và messi ai giỏi hơn']]
answers = ['D','B','A','B']
ques1 = [['A.10','B.3','C.9','D.7'],['A.Nhật Bản','B.Bồ Đào Nha','C.Việt Nam','D.Agretina'],['A.5','B.7','C.8','D.3'],['A.Messi','B.Ronaldo','C.Cả hai đều là goat','D.Không biết']]
a = []
num = 0
score = 0
num1 = 0
for questione in questiones:
    print("-------------------")
    print(questione)
    for ques in ques1[num]:

        print(ques,end = " ")
    num += 1
    print()
    b = input("Đáp án bạn chọn là:")
    b = b.upper()
    a.append(b)
for i in answers:
    if a[num1] == i:

        score += 1
    num1 += 1
print("       END        ")
print(f"YOUR SCORE IS {score}")
