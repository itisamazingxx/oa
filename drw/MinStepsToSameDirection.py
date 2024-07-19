class Solution:
    def minStepsToSameDirection(self, s):
        directions = ["^", ">", "v", "<"]
        minStep = float('inf')

        '''
        当前元素(单一)与想要的方向之间差几步能达到
        '''
        def getDistance(arrow, target):
            targetIndex = directions.index(target)
            arrowIndex = directions.index(arrow)
            distance = abs(targetIndex - arrowIndex)
            return distance


        # 对于每一个方向, 检测将s中其他元素全部变为此方向需要几步
        # 总共比较四次
        for d in directions:
            step = sum(getDistance(arrow, d) for arrow in s)
            minStep = min(minStep, step)
        
        return minStep if minStep != float('inf')else -1


# 示例测试
solution = Solution()

# # 测试用例 1
# s = ["^", ">", "v", "<"]
# print(solution.minStepsToSameDirection(s))  # 输出: 4

# 测试用例 2
s = ["^", "^", "<", "<"]
print(solution.minStepsToSameDirection(s))  # 输出: 2

# 测试用例 3
s = [">", ">", ">", ">"]
print(solution.minStepsToSameDirection(s))  # 输出: 0

# 测试用例 4
s = ["<", ">", "^", "v"]
print(solution.minStepsToSameDirection(s))  # 输出: 3

# 测试用例 5
s = ["<", "<", "<", "<"]
print(solution.minStepsToSameDirection(s))  # 输出: 0
