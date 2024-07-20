from collections import defaultdict
import heapq
'''
给定起点start place和终点end place以及一串网络连接的列表network connections
每个网络连接表示为一个三元组(start place, end place, price), 表示从start place到end place的连接价格
要求输出从起点到终点价格最低的所有路径
'''
class Solution:
    def findCheapestPaths(self, connections, start, end):
        # Dijkstra
        # 用于加权图中的单源最短路径问题
        
        n = len(connections)
        # 构建邻接表
        graph = defaultdict(list)
        for s, e, price in connections:
            graph[s].append((e, price))
        
        # 将起点位置放入最小堆
        minHeap = [(0, start, [start])]
        # 初始化距离数组, 更新记录各个点到起点的总权重最低价格
        dist = defaultdict(lambda: float('inf'))
        dist[start] = 0
        # 初始化路径数组, 用来记录从起点到每个节点的最短路径
        # allPath[neighbor]记录的是从起点到neighbor的那条最短路径
        allPath = defaultdict(list)
        allPath[start] = [[start]]

        while minHeap:
            p, place, path = heapq.heappop(minHeap)

            if place == end or p > dist[place]:
                continue

            for neighbor, price in graph[place]:
                newPrice = p + price
                if newPrice < dist[neighbor]:
                    dist[neighbor] = newPrice
                    heapq.heappush(minHeap, (newPrice, neighbor, path + [neighbor]))
                    allPath[neighbor] = (path + [neighbor])
                elif newPrice == dist[neighbor]:
                    allPath[neighbor].append(path + [neighbor])

        return allPath[end]
#         a
#      1 / \ 2
#       b - c - d
#         2   1
        
    


solution = Solution()
start = "A"
end = "D"
connections = [("A", "B", 1), ("B", "C", 2), ("A", "C", 2), ("C", "D", 1)]
print(solution.findCheapestPaths(connections, start, end))  # 输出: [['A', 'C', 'D']]

start = "A"
end = "D"
connections = [("A", "B", 4), ("A", "C", 2), ("B", "C", 5), ("B", "D", 10), ("C", "D", 3)]
print(solution.findCheapestPaths(connections, start, end))  # 输出: [['A', 'C', 'D']]

solution = Solution()
start = "A"
end = "E"
connections = [("A", "B", 1), ("B", "C", 1), ("C", "D", 1), ("D", "E", 1), ("A", "E", 5)]
print(solution.findCheapestPaths(connections, start, end))  # 输出: [['A', 'B', 'C', 'D', 'E']]







