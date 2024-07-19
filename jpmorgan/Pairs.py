'''
Consider two arrays of integers, a[n] and b[n]. 
What is the maximum number of pairs that can be formed where a[i] > b[j]? 
Each element can be in no more than one pair.

Find the maximum number of such possible pairs.

Function Description

Complete the function findNumOfPairs in the editor below.

findNumOfPairs has the following parameters:

int a[n]: an array of integers
int b[n]: an array of integers

Returns
int: the maximum number of pairs possible

Example 1:
Input:  a = [1, 2, 3], b = [1, 2, 1]
Output: 2 
'''

class Solution:
  def findNumOfPairs(self, a, b):
    ans = 0
    n = len(a)
    usedA = [False] * n
    usedB = [False] * n
    for i in range(n):
      for j in range(n):
        if a[i] > b[j] and not usedA[i] and not usedB[j]:
          usedA[i] = True
          usedB[j] = True
          ans += 1
    return ans
  
  def findNumOfPairs2(self, a, b):
    # 方法2: 排序 + 双指针
    a.sort()
    b.sort()
    i = 0
    j = 0
    n = len(a)
    ans = 0
    while i < n and j < n:
      if a[i] > b[j]:
        j += 1
        ans += 1
      i += 1
    return ans
  
# 示例测试
solution = Solution()

# 测试用例 1
a = [1, 2, 3]
b = [1, 2, 1]
print(solution.findNumOfPairs2(a, b))  # 输出: 2

# 测试用例 2
a = [1, 2, 3, 4, 5]
b = [6, 6, 1, 1, 1]
print(solution.findNumOfPairs2(a, b))  # 输出: 3