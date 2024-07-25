from collections import defaultdict
'''
计算员工之间的层级数 例如给出:
Susan/John - Susan reports to John
John/Amy - John reports to Amy

求Susan到Amy之间的layer数

相似题目: leetcode 399
'''
class Solution:
    def employeeLayer(self, relations, queries):
        graph = self.buildGraph(relations)
        ans = []
        for a, b in queries:
            visited = set()
            ans.append(self.dfs(graph, a, b, visited, 0))
        return ans

    def buildGraph(self, relations):
        graph = defaultdict(list)
        for r in relations:
            a, b = r.split("/")
            graph[a].append(b)
        return graph
        
    def dfs(self, graph, a, b, visited, depth):
        visited.add(a)
        if a == b:
            return depth
        
        for neighbor in graph[a]:
            if neighbor not in visited:
                return self.dfs(graph, neighbor, b, visited, depth + 1)
        visited.remove(a)
        return -1
        
solution = Solution()
relations = ["Susan/John", "John/Amy", "Amy/Tom"]
queries = [["Susan", "Amy"], ["John", "Susan"], ["Susan", "Tom"], ["Tom", "Susan"]]
print(solution.employeeLayer(relations, queries))

# Interview Note:
# We are provided with an array that stores the relationships between employees;
# and we also have a series of queries that require checking the reporting layer between two specific employees
# Firstly, we need to convert the array of relationships into a graph where each node represents an employee;
# and edges represent direct reporting lines.
# Then Implement dfs algorithm to traverse the graph.
# the reporting layer equals the number of edges between the two nodes in the graph, which corresponds to the number of recursive calls in the dfs process.