from collections import defaultdict, deque
'''
给定起点start place和终点end place以及一串网络连接的列表network connections
每个网络连接表示为一个三元组(start place, end place, price), 表示从start place到end place的连接价格
要求输出从起点到终点价格最低的所有路径
'''
class Solution:
    def findCheapestPaths(self, connections, start, end):
        # Dijkstra
        # 用于加权图中的单源最短路径问题
        # 不能用普通bfs, 因为价格是有权重
        pass
        
    


solution = Solution()
start_place = "A"
end_place = "D"
network_connections = [("A", "B", 1), ("B", "C", 2), ("A", "C", 2), ("C", "D", 1)]
print(solution.findCheapestPaths(start_place, end_place, network_connections))  # 输出: [['A', 'C', 'D']]







