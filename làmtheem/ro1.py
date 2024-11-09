# s1 = "abcd"
# s2 = '1234'
# s = ("")
# i = 0
# check = 1
# while i < len(s1):
#     if check % 2 != 0:
#         s += s1[i] + s2[i:i+1]
#     else:
#         s += s2[i] + s1[i:i+1]
#     check += 1
#     i += 1
# print(s)

# s = 'I am 25 years and 10 month old'

# for i in s:
#     if i.isdigit():
#         print(i,end="")
# a = s.()
# print(a)

# a = ["Emma", "Jon",'' ,  "Kelly", None, 'Eric','']
# for i in a:
#     if i == '' or i == None:
#         a.remove(i)
# print(a)

file1 = open("New Text Document.txt","r")
read_content = file1.read()
print(read_content)