'''leetcode 1572
'''

from typing import List

'''def diagonalSum_Brute( mat: List[List[int]]) -> int:
    n = len(mat)
    s = 0
    for i in range(n):
        for j in range(n):
            #diagonal-1
            if i == j:
                 s += mat[i][j]
            #diahonal-2
            if i + j == n-1:
                s += mat[i][j] 
    if n%2 == 1:
        s -= mat[n//2][n //2]
    return s                   

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum_Brute(mat))

'''

#optimized solution
'''

def diagonalSum_Brute( mat: List[List[int]]) -> int:
    n = len(mat)
    s = 0
    for i in range(n):
        s += mat[i][i]
        s += mat[i][n-1-i]
    if n%2 == 1:
        s -= mat[n//2][n //2]
    return s                   

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum_Brute(mat))

'''
