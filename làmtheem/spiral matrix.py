def spiralmatrix(matrix):
    ln = len(matrix[0]) * len(matrix)
    x = len(matrix)
    r = 0
    c = len(matrix[0]) - 1
    bit = -1
    lst = matrix[0]
    m = len(matrix)
    n = len(matrix[0])
    while len(lst) < ln:
        bit *= -1
        m -= 1
        n -= 1
        for _ in range(m):
            r += bit
            lst.append(matrix[r][c])
            if len(lst) == ln: break
        for _ in range(n):
            c -= bit
            lst.append(matrix[r][c])

            if len(lst) == ln: break
    return lst
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
print(spiralmatrix(matrix))