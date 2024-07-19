'''
Amazon has multiple delivery centers and delivery warehouses all over the world! 
The world is represented by a number line from -109 to 109. 
There are n delivery centers, the ith one at location center[i]. 
A location x is called a suitable location for a warehouse if it is possible to bring all the products to that point by traveling a distance of no more than d. 
At any one time, products can be brought from one delivery center and placed at point x. 
Given the positions of n delivery centers, calculate the number of suitable locations in the world. 
That is, calculate the number of points x on the number line (-109 ≤ x ≤ 109) where the travel distance required to bring all the products to that point is less than or equal to d.

Note: The distance between point x and center[i] is |x - center[i]|, their absolute difference.

Input:  center = [-2, 1, 0], d = 8
Output: 3 
'''
class Solution:
    def numberOfSuitableLocations(self, centers, d):
        # 此题求解的是方案数

        # 初始化交集范围
        leftBound = -10**9
        rightBound = 10**9

        for center in centers:
            leftBound = max(leftBound, center - d)
            rightBound = min(rightBound, center + d)

        if leftBound > rightBound:
            return 0
        
        ans = 0
        # 遍历每一个可能的x位置
        for x in range(leftBound, rightBound + 1):
            # 针对每一个center计算往返的距离
            distance = sum(2 * abs(x - center) for center in centers)
            if distance <= d:
                ans += 1

        return ans
    
    def numberOfSuitableLocations2(self, centers, d):
        # 方法2: 二分查找
        # 比之前的方法更快
        start = -10**9
        end = 10**9

        lx, rx = float('inf'), float('-inf')
        l, r = start, end
        while l <= r:
            mid = (l + r) // 2
            distance = sum(2 * abs(mid - center) for center in centers)
            # 此点可以作为location之一
            if distance <= d:
                lx = mid
                r = mid - 1
            else:
                l = mid + 1

        l, r = start, end
        while l <= r:
            mid = (l + r) // 2
            distance = sum(2 * abs(mid - center) for center in centers)
            if distance <= d:
                rx = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return int(rx - lx + 1) if lx != float('inf') and rx != float('inf') else 0 

# 示例测试
solution = Solution()
centers = [-2, 1, 0]
d = 8
print(solution.numberOfSuitableLocations(centers, d)) # 输出: 3

centers = [2, 0, 3, -4]
d = 22
print(solution.numberOfSuitableLocations(centers, d)) # 输出: 5

centers = [-3, 2, 2]
d = 8
print(solution.numberOfSuitableLocations(centers, d)) # 输出: 0