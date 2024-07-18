from collections import Counter
'''
There were a large number of orders placed on Amazon Prime Day. 
The orders are packed and are at the warehouse ready to be delivered. 
The delivery agent needs to deliver them in as few trips as possible.

In a single trip, the delivery agent can choose packages following either of two rules:

Choose two packages with the same weight
Choose three packages with the same weight
Determine the minimum number of trips required to deliver the packages. 
If it is not possible to deliver all of them, return -1.

packageweight = [2, 4, 6, 6, 4, 2, 4]
The agent needs a minimum of 3 trips as shown below. Return 3 as the answer.

'''
class Solution:
    def minTrip(self, packages):
        record = Counter(packages)
        ans = 0
        # 只能ship重量相同的商品
        for weight, count in record.items():
            while count > 0:
                if count % 3 == 0:
                    count -= 3
                elif count % 2 == 0:
                    count -= 2
                else:
                    return -1
                ans += 1
        return ans
    

# 示例测试
packageweight = [2, 4, 6, 6, 4, 2, 4] # 3
packageweight2 = [1, 8, 5, 8, 5, 1, 1] # 3
packageweight3 = [3, 4, 4, 4, 1] # -1
solution = Solution()
print(solution.minTrip(packageweight3))