'''
Implement a prototype of a friend recommendation system for a social media application.

There are n users indexed from 0 to n, and m friends represented as a 2d array, friendships, where the ith friendship is a connection between users friendships[i][0] and friendships[i][1].

User x is suggested as a friend to user y if x and y are not friends and have the maximum number of common friends, i.e. a friend of both x and y. If there are multiple possible such users x, the one with the minimum index is suggested.

Given n and friendships, for each of the n users, find the index of the friend that should be recommended to them. If there is no recommendation available, report -1.

Function Description

Complete the function getRecommendedFriends in the editor.

getRecommendedFriends has the following parameters:
int n: the number of users
int friendships[m][2]: the friendships between the users

Returns
int[]: an array of integers where the ith integer is the index of the recommended friend for the ith user, or -1 if no recommendation is available.

Example 1:

Input:  n = 5, friendships = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
Output: [3, 2, 1, 0, 1] 
'''
class Solution:
  def getRecommendedFriends(self, n, friendships):
    # 首先创建一个邻接表记录用户与其朋友圈关系
    graph = {i : set() for i in range(n)}
    for user, friend in friendships:
      graph[user].add(friend)
      graph[friend].add(user)

    # 为每位用户推荐其他用户
    recommandations = [-1] * n

    # 挨个比较两个用户的关系
    for i in range(n):
        maxCommonFriend = 0
        recommandFriend = -1
        for j in range(n):
            if i != j and j not in graph[i]:
                commonFriendsNum = len(graph[i].intersection(graph[j]))
                if (commonFriendsNum > maxCommonFriend) or \
                ((commonFriendsNum == maxCommonFriend and j < recommandFriend)):
                    maxCommonFriend = commonFriendsNum
                    recommandFriend = j
        recommandations[i] = recommandFriend
    return recommandations
  
solution = Solution()
n = 5
friendships = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
print(solution.getRecommendedFriends(n, friendships))  # 输出: [3, 2, 1, 0, 1]

n = 3
friendships = [[0, 1], [1, 2], [2, 0]]
print(solution.getRecommendedFriends(n, friendships))  # 输出: [-1, -1, -1]