'''
0/1背包求总方案
给定i个正整数nums[i], 使得和为target
求总共有多少总选择方案
'''
class Solution:

    def pick(self, nums, target):

        # dp[i]表示在当前容量下的方案数
        # 可以选当前整数
        dp = [0] * (target + 1)
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i - num]
        return dp[-1]