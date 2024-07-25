'''
0/1背包问题:
给定一个可装载重量为W的背包和N个物品, 每个物品有重量和价值两个属性
其中第i个物品的重量为wt[i], 价值为val[i]
现在让你用这个背包装物品 每个物品只能用一次, 在不超过被包容量的前提下, 最多能装的价值是多少？
'''
class Solution:
    def knapsack(self, w, n, wt, val):

        # 动态规划题目中重要的两点: 状态; 选择
        # 伪代码如下:
        # for 状态1 in 所有状态1取值:
        #       for 状态2 in 所有状态2取值:
        #           dp[状态1][状态2] = 择优(选择1)(选择2)

        dp = [[0] * (w + 1) for _ in range(n + 1)] # dp[i]代表容量i下可以承载的最大值

        for i in range(1, n + 1): # 遍历物品
            for j in range(1, w + 1): # 遍历背包容量
                if j - wt[i - 1] >= 0:
                    dp[i][j] = max(
                        dp[i - 1][j - wt[i - 1]] + val[i - 1],
                        dp[i - 1][j]
                    )
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][w]

solution = Solution()
n = 3
w = 4
wt = [2, 1, 3]
val = [4, 2, 3]
print(solution.knapsack(w, n, wt, val))  # 输出: 6




