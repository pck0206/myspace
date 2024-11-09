# def sum(nums):
#    lst1 = []
#    lst2 = []
#    for i in range(len(nums)):
#       for k in range(i + 1,len(nums)):
#          for j in range(k + 1,len(nums)):
#             if nums[i] + nums[k] + nums[j] == 0:
#                lst1.append(nums[i])
#                lst1.append(nums[k])
#                lst1.append(nums[j])
#                lst1.sort()
#                lst2.append(lst1)
#                lst1 = []
#    for l in lst2:
#       for i in range(lst2.count(l) - 1):
#          lst2.remove(l)
#    return lst2
# nums = [0,0,0,0,0,0,0]
# print(sum(nums))

# def letter_combination(n):
#    lst = []
#    alpha = [['a','b','c'],['d','e','f'],
#             ['g','h','i'],['j','k','l'],['m','n','o'],
#             ['p','q','r','s'],['t','u','v'],['w','x','y','z']]
#    if len(n) == 2:
#       for i in range(len(n) - 1):
#          for k in alpha[int(n[i]) - 2]:
#             for j in alpha[int(n[i + 1]) - 2]:
#                lst.append(k + j)
#    elif len(n) == 1:
#       for i in range(len(n)):
#          for k in alpha[int(n[i]) - 2]:
#             lst.append(k)
#    elif len(n) == 3:
#       for i in range(len(n) - 2):
#          for k in alpha[int(n[i]) - 2]:
#             for j in alpha[int(n[i + 1]) - 2]:
#                for m in alpha[int(n[i + 2]) - 2] :
#                   lst.append(k + m + j)
#    elif len(n) == 4:
#       for i in range(len(n) - 2):
#          for k in alpha[int(n[i]) - 2]:
#             for j in alpha[int(n[i + 1]) - 2]:
#                for m in alpha[int(n[i + 2]) - 2] :
#                   for l in alpha[int(n[i + 3])-2]:
#                      lst.append(k + j + m + l)
#    return lst

#
#
#
# def letterCombinations(digits: str) -> List[str]:
#    if not digits:
#       return []
#
#    # Bản đồ các số với các ký tự tương ứng trên bàn phím
#    phone_map = {
#       "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
#       "7": "pqrs", "8": "tuv", "9": "wxyz"
#    }
#
#    def backtrack(index, path):
#       # Nếu đã tạo được tổ hợp cho tất cả các chữ số
#       if index == len(digits):
#          combinations.append("".join(path))
#          return
#       # Lấy các chữ cái tương ứng với chữ số hiện tại
#       possible_letters = phone_map[digits[index]]
#       for letter in possible_letters:
#          path.append(letter)  # Thêm chữ cái vào tổ hợp hiện tại
#          backtrack(index + 1, path)  # Tiếp tục cho chữ số tiếp theo
#          path.pop()  # Loại bỏ chữ cái để thử tổ hợp khác
#
#    combinations = []
#    backtrack(0, [])
#    return combinations
#
#
# n = '223'
# print(letterCombinations(n))



# def sum(nums,target):
#    lst = []
#    lst1 = []
#    a = set()
#    for i in range(len(nums)):
#       for k in range(i + 1,len(nums)):
#          for j in range(k + 1,len(nums)):
#             for h in range(j + 1,len(nums)):
#                if nums[i] + nums[j] + nums[k] + nums[h] == target:
#                   lst.append(nums[i])
#                   lst.append(nums[j])
#                   lst.append(nums[k])
#                   lst.append(nums[h])
#                   lst.sort()
#                   a.add(tuple(lst))
#                   lst = []
#    for i in a:
#       lst1.append(list(i))
#    return lst1
# nums = [1,0,-1,0,-2,2]
# target = 0
# print(sum(nums,target))

# i = 0
#
#
# def isValid(s):
#     i = 0
#     a = len(s)
#     while s != "":
#         if "()" in s:
#             s = s.replace('()', "")
#         if '[]' in s:
#             s = s.replace("[]", "")
#         if "{}" in s:
#             s = s.replace("{}", "")
#         if s.startswith("(") and s.endswith(")"):
#             s = s.replace("(", "", 1)
#             s = s[::-1].replace(")", "", 1)[::-1]
#         elif s.startswith("[") and s.endswith("]"):
#             s = s.replace("[", "", 1)
#             s = s[::-1].replace("]", "", 1)[::-1]
#         elif s.startswith("{") and s.endswith("}"):
#             s = s.replace("{", "", 1)
#             s = s[::-1].replace("}", "", 1)[::-1]
#         if s == "":
#             return True
#         i += 1
#         if i == a:
#             break
#     return False
# s = "([[][]{({}({}))}])"
# print(isValid(s))


# def exist(board, word):
#     a = 0
#     st = ""
#     k = word
#     for i in range(len(board)):
#         lst = board[i]
#         word1 = str("".join(lst))
#         while a < len(word):
#             if word[a] in word1:
#                 word1 = word1.replace(word[a]," ",1)
#                 st += word[a]
#                 a += 1
#                 continue
#             if word[a] in word1 and word1.index(word[a]) == board[i].index(word[a - 1]):
#                 word1.replace(word[a]," ")
#                 st += word[a]
#                 a += 1
#                 continue
#             else:
#                 break
#     if st == k:
#         return True
#     return False
# board = [["a","b"],["c","d"]]
# word = "acdb"
#
# print(exist(board,word))'
# s = input()
# a = 0
# for i in s:
#     if s.count(i) == 1:
#         a += 1
#         b = s.index(i)
#     if a == 2:
#         break
# if a == 2:
#     print(b)
# else:
#     print(-1)


# def check(s):
#     a = []
#     b = 0
#     if s[::-1] == s:
#         return "YES"
#     for i in s:
#         a.append(s.count(i))
#     if len(s) % 2 == 0:
#         for k in a:
#             if k % 2 != 0:
#                 return "NO"
#     elif len(s) % 2 != 0:
#         for k in a:
#             if k % 2 != 0:
#                 b += 1
#         if b == 1:
#             return "YES"
#         else:
#             return "NO"
# s = input()
# print(check(s))



# def check(matrix):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i + 1, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     for i in range(n):
#         matrix[i].reverse()
#     return matrix
# n = int(input())
# matrix = []
# for m in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# for row in check(matrix):
#     print(' '.join(map(str, row)))



# n = 5
# a = "Alice Bob Charlie David Eve"
# score = [80 ,90 ,90 ,70 ,60]
# student = a.split()
# dc = {}
# lst = []
# for i in range(len(student)):
#     dc[student[i]] = score[i]
# for value in dc.values():
#     lst.append(value)
# lst.sort()
# lst.reverse()
# for i in range(len(lst)):
#     for key in dc.keys():
#         if dc[key] == lst[i]:
#             if lst.count(lst[i]) > 1:
#                 dc[key] = i + 1
#                 boooll = True
#             else:
#                 dc[key] = i + 1
# print(dc)

# n = 3
# def climbStairs( n: int) -> int:
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     f = [0] * n
#     f[0] = 1
#     f[1] = 2
#     for i in range(2 , n):
#         f[i] = f[i - 1] + f[i - 2]
#     return f[-1]
# print(climbStairs(n))

import collections
counter = collections.Counter()
print(counter)


























































