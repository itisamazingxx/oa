from collections import defaultdict
'''
给定一组产品ID对 按照它们的关系对它们进行分组 并返回包含分组后产品ID的新列表

一个产品ID对的列表。例如:
[(1, 2), (2, 5), (3, 4), (4, 6), (6, 8), (5, 7), (5, 2), (5, 2)]
每个对表示这两个产品ID之间存在某种连接或关系

输出
一个列表，列表中的每个元素是一个产品ID的集合，这些ID互相连接形成一个组。例如:
[[1, 2, 5, 7], [3, 4, 6, 8]]
'''
class Solution:
    def groupProductIdPairsIntoCategories(self, productPairs):
        # 方法: dfs
        # 求联通分量的个数
        # (example中)每个产品都只有另一个产品作为邻接产品, 用dfs比较合适

        # 1. 构建邻接表
        graph = defaultdict(list)
        for a, b in productPairs:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(visited, group, productId):
            visited.add(productId)
            group.append(productId)

            for neighbor in graph[productId]:
                if neighbor not in visited:
                    dfs(visited, group, neighbor)
        
        n = len(productPairs)
        visited = set()
        ans = []
        for productId in graph:
            if productId not in visited:
                group = []
                dfs(visited, group, productId)
                ans.append(sorted(group))
        return ans


solution = Solution()
productPairs = [(1, 2), (2, 5), (3, 4), (4, 6), (6, 8), (5, 7), (5, 2), (5, 2)]
print(solution.groupProductIdPairsIntoCategories(productPairs))  
# 输出: [[1, 2, 5, 7], [3, 4, 6, 8]]