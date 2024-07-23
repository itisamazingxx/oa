'''
You are given a matrix of integers matrix, containing only zeros and ones.

Let's call an "x-shape" a figure with a center at some cell of matrix and 4 diagonal rays of equal length. 
The x-shape is called perfect if all its elements equal 1.

For example, there is one perfect x-shaped figure of size 2 with a center at [1, 1], 
and five perfect x-shaped figures of size 1 in the following matrix:

[[1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]]

At the same time, the following matrix has only four perfect x-shaped figures of size 1:
[[1, 1],
 [1, 1]]

Return the center coordinates [row, col] of the largest perfect x-shaped figure within the matrix. 
If there are multiple answers, then return the answer with the minimal row value first, and if there is still a tie, 
then minimal column value among them.
'''
class Solution:
    # 找到完美x型
    def codeWriting(self, matrix):
        pass