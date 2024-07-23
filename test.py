class Solution:
    def trap(self, height):
        # 接雨水问题 Brute-Force
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
    
solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution.trap(height))  # 输出: 6

height = [4,2,0,3,2,5]
print(solution.trap(height))  # 输出: 9

