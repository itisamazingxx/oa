from collections import defaultdict
'''
计算员工之间的层级数 例如给出：
Susan/John
John/Amy

实际上是在找需要进行多少次DFS调用才能找到对应值 即求从a到b的层级数

相似题目: leetcode 399
'''
class Solution:
    def employeeLayer(self, relations, queries):
        graph = self.buildGraph(relations)
        ans = []
        for a, b in queries:
            visited = set()
            ans.append(self.dfs(graph, a, b, visited))
        return ans


    def buildGraph(self, relations):
        graph = defaultdict(list)
        for relation in relations:
            a, b = relation.split("/")
            graph[a].append(b)
        return graph
    
    def dfs(self, graph, a, b, visited):
        if a == b:
            return 0
        
        visited.add(a)
        for neighbor in graph[a]:
            layer = self.dfs(graph, neighbor, b, visited)
            if layer != -1: # 有对应关系存在
                return layer + 1
        visited.remove(a)
        return -1
            

        
solution = Solution()
relations = ["Susan/John", "John/Amy", "Amy/Tom"]
queries = [["Susan", "Amy"], ["John", "Susan"], ["Susan", "Tom"], ["Tom", "Susan"]]
print(solution.employeeLayer(relations, queries)) 