class Solution:
    def subarraySum(self, nums, k):
        # 方法1: Brute-Force
        # 双指针, 由于subarrays数组必须是连续的, i指针用来代表数组的长度
        # j指针在0-i之间遍历
        n = len(nums)
        ans = 0
        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                if curSum == k: # 统计到一个符合标准的答案
                    ans += 1
                elif curSum > k:
                    break
        return ans
    

e = Solution()
print(e.subarraySum([1,-1,0], 0))
