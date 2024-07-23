'''
接雨水问题本地test
四种方法: Brute Force; DP; stack; two pointers
'''
class Solution:
    def trap(self, height):
        # 接雨水问题 Brute-Force

        # note: dp/双指针法都是此穷举法的升级

        n = len(height)
        ans = 0
        for i in range(n):
            leftMax = 0
            rightMax = 0
            for l in range(i + 1):
                leftMax = max(leftMax, height[l])
            for r in range(i, n):
                rightMax = max(rightMax, height[r])
            ans += min(leftMax, rightMax) - height[i]
        return ans
    
    def trap2(self, height):
        # 动态规划的目的在于: 消除原暴力求解里重复子问题的计算
        # 我们依然按照原先的思路, focus on每一个单独的柱子
        # 对于当前柱子i能存储的水量就是:
        # water[i] = min(
        # 左边最高的柱子
        # max(height[0..i]),  
        # 右边最高的柱子
        # max(height[i..end]) 
        # ) - height[i]

        # 在之前遍历每个柱子的过程中, 我们都要重新遍历一次找当前i柱左侧右侧最大值
        # 可以提前初始化数组存储这个过程O(n), 遍历柱子0(n), 整体时间复杂度0(n)
        # 保存最大值就是重复子问题, 已经将暴力搜索转换成了dp问题

        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        # dp
        dp = [0] * n
        for i in range(n):
            # 针对当前柱子i, 状态转移公式
            dp[i] = min(leftMax[i], rightMax[i]) - height[i]
        
        return sum(dp)

    def trap3(self, height):
        # 双指针解法相当于用了滚动数组(初始化两个变量)
        # 节省了额外O(n)空间的使用

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0

        ans = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax < rightMax:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans
    
solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution.trap2(height))  # 输出: 6

height = [4,2,0,3,2,5]
print(solution.trap2(height))  # 输出: 9