def isValidSudoku(board):
        cot1 =0
        hang1 = 0
        lst_ngang = []
        lst_doc = []
        lst_3x3 = []
        j = 0
        lst = board.copy()
        ct1 = True
        ct2 = False
        ct3 = False
        if board.count([".",".",".",".",".",".",".",".","."]) == 9:
            return True
        for i in range(len(board)):
            while cot1 < len(board):
                if board[i][cot1].isdigit():
                    lst_ngang.append(board[i][cot1])
                    cot1 += 1
                else:
                    cot1 += 1
            for k in lst_ngang:
                if lst_ngang.count(k) > 1:
                    return False
            cot1 = 0
            lst_ngang = []
        for i in range(len(board)):
            while hang1 < len(board):
                if board[hang1][i].isdigit():
                    lst_doc.append(board[hang1][i])
                    hang1 += 1
                else:
                    hang1 += 1
            for i in lst_doc:
                if lst_doc.count(i) > 1:
                    return False
            lst_doc = []
            hang1 = 0
        i = 0
        count = 0
        count1 = 0
        while ct1 or ct2 or ct3:
            while ct1:
                if board[i][j].isdigit():
                    lst_3x3.append(board[i][j])
                j += 1
                if j == 3:
                    board.remove(board[i])
                    count += 1
                    j = 0
                if count == 3:
                    for l in lst_3x3:
                        if lst_3x3.count(l) > 1:
                            return False
                    count = 0
                    count1 +=1
                    lst_3x3 = []
                if count1 == 3:
                    lst_3x3 = lst.copy()
                    ct1 = False
                    ct2 = True
            j = 3
            count = 0
            count1 = 0
            board = lst.copy()
            lst_3x3 = []
            while ct2:
                if board[i][j].isdigit():
                    lst_3x3.append(board[i][j])
                j += 1
                if j == 6:
                    board.remove(board[0])
                    j = 3
                    count += 1
                if count == 3:
                    for p in lst_3x3:
                        if lst_3x3.count(p) > 1:
                            return False
                    count = 0
                    count1 += 1
                    lst_3x3 = []
                if count1 == 3:
                    board = lst.copy()
                    ct2 = False
                    ct3 = True
            j = 6
            count = 0
            count1 = 0   
            board = lst.copy()
            lst_3x3 = []
            while ct3:
                if board[i][j].isdigit():
                    lst_3x3.append(board[i][j])
                j += 1
                if j == 9:
                    board.remove(board[0])
                    j = 6
                    count += 1
                if count == 3:
                    for p in lst_3x3:
                        if lst_3x3.count(p) > 1:
                            return False
                    count = 0
                    count1 += 1
                    lst_3x3 = []
                if count1 == 3:
                    board = lst.copy()
                    ct3 = False
        return True
board = [["1","2",".",".",".",".","6",".","7"],
         [".",".",".",".",".",".",".",".","5"],
         [".",".","9",".","6",".","4",".","."],
         [".","6",".",".",".",".",".",".","."],
         [".",".",".",".","4",".",".","7","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","2"],
         [".","9",".",".",".",".",".",".","7"]]
print(isValidSudoku(board))
