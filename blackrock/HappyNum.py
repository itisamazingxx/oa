'''
同lc202, 检查给定正整数n是否为快乐数
'''
class Solution:
    def isHappy(self, n):
        record = set()

        def getNextN(n):
            next = 0
            while n:
                digit = n % 10
                next += (digit * digit)
                n //= 10
            return next

        while n != 1:
            n = getNextN(n)
            if n not in record:
                record.add(n)
            else:
                return False
        return True

# 测试案例    
solution = Solution()
n = 19
print(solution.isHappy(n)) # true

n = 2
print(solution.isHappy(n)) # false

# Interview Note:
# In this question, we are given an integer n, and we need to write a function to determine if it is a happy number.
# By definition, a happy number is a number that, if we continually replace the number with the sum of the squares of its digits, we will eventually reach the number 1.
# It's important to note that the sum of the squares of the digits of any number does not increase indefinitely; 
# it will either eventually reach 1 or start repeating in a cycle.
# Thus, we can use a hashmap(set) to store numbers that have already been calculated.
# If we reach 1, the loop breaks and we return True. Otherwise indicates a cycle occurs, we return False.
