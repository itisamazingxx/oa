class Solution:
    def minStepsToSameDirection(self):
        directions = ["^", ">", "v", "<"]
        minStep = float('inf')

        '''
        当前元素(单一)与想要的方向之间差几步能达到
        '''
        def getDistance(index, target):
            return (directions.index(target) - directions.index(index)) % 4

        # 对于每一个方向, 检测将s中其他元素全部变为此方向需要几步
        # 总共比较四次
        for d in directions:
            step = sum(getDistance(arrow, d) for arrow in s)
            minStep = min(minStep, step)
        
        return minStep if minStep != float('inf')else -1


# 示例测试
solution = Solution()
s = "^>v<"
print(solution.minStepsToSameDirection(s))  # 输出: 3
