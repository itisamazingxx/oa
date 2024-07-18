
'''
Some developers want to deploy their application on different servers with a load balancer in the front. 
There are n servers to choose from where the number of requests that can be handled by the jth server is server[i]. 
The number of requests served by any server is a power of 2 i.e. 1, 2, 4, 8, 16,...etc.

Given the array server and an integer expected_load, find the minimum number of servers that must be chosen such that the total sum of requests served by all the chosen servers is exactly equal to the expected_load. 
If there is no combination of servers that can serve exactly expected_load requests, report -1 as the answer.

Example
Suppose n = 4, servers = [1, 1, 2, 4], and expected_load = 3.

It is optimal to choose the first and the third or the second and the third servers serving a total of 1 + 2 = expected_load = 3 requests. Return the minimum number of servers needed, 2.

Function Description:
Complete the function getMinServers in the editor below.

The function getMinServers has the following parameter:
int expected_load: the number of requests to be served
int server[n]: the number of requests the servers can serve

Return:
int: the minimum number of servers such that the sum of the total requests they can serve is exactly expected_load

Constraints:
1 ≤ n ≤ 10^5
1 ≤ server[i] ≤ 10^9
It is guaranteed that server[i] is a power of 2.
1 ≤ expected_load ≤ 10^9
'''
class Solution:
    def serverSelection(self, servers, expect_loads):
        # 找到服务器数组中元素相加等于指定负载 (expected_load) 的最少服务器数量
        # 0/1背包问题, 数组中元素不可以重复使用

        # 方法1: 递归 brute-force
        self.minServer = float('inf')
        n = len(servers)

        # 元素不可以重复使用, 需要用index参数来控制起点位置
        # count - 当前已部署服务器数量
        def helper(index, count, curLoads):
            if curLoads == expect_loads:
                if count < self.minServer:
                    self.minServer = count
                return

            if curLoads > expect_loads or index > n:
                return

            for i in range(index, n):
                helper(i + 1, count + 1, curLoads + servers[i])

        helper(0, 0, 0)
        return self.minServer if self.minServer != float('inf') else -1
    
    def serverSelection2(self, servers, expect_loads):
        # 方法2: memo + 记忆化搜索
        n = len(servers)
        memo = {}
        
        # return值代替了参数count
        def helper(cur, index):
            if cur in memo:
                return memo[cur]
            
            if cur == expect_loads:
                return 0
            
            if cur > expect_loads:
                return float('inf')
            
            minCount = float('inf')

            for i in range(index, n):
                count = helper(cur + servers[i], i + 1) + 1
                minCount = min(minCount, count)
            
            memo[cur] = minCount
            return minCount
        
        result = helper(0, 0)
        return result if result != float('inf') else -1
    
    def serverSelection3(self, servers, expect_loads):
        dp = [float('inf')] * (expect_loads + 1)
        # dp数组代表满足i量的负载均衡需要配置多少个server
        dp[0] = 0

        for server in servers:
            for i in range(expect_loads, server - 1, -1):
                if dp[i - server] != float('inf'):
                    dp[i] = min(dp[i], dp[i - server] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
        


    
# 测试用例
solution = Solution()

# 测试用例 1
servers = [1, 1, 1]
expected_load = 4
print(solution.serverSelection2(servers, expected_load))  # 输出: -1

# 测试用例 2
servers = [1, 1, 2, 4, 4]
expected_load = 10
print(solution.serverSelection2(servers, expected_load))  # 输出: 3

# 测试用例 3
servers = [1, 1, 2, 4]
expected_load = 3
print(solution.serverSelection2(servers, expected_load))  # 输出: 2

# 测试用例 4
servers = [1, 2, 4]
expected_load = 8
print(solution.serverSelection2(servers, expected_load))  # 输出: -1

