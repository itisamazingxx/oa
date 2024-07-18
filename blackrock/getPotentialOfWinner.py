'''
The city of Hackerland organized a chess tournament for its citizens.

There are n participants numbered 1 to n where the ith participant has potential denoted by potential[i]. 
The potential of each player is distinct. Initially, all players stand in a queue in order from the 1st to the nth player. 
In each game, the first 2 participants of the queue compete and the participant with a higher potential wins the game. 
After each game, the winner remains at the beginning of the queue and plays with the next person from the queue, and the losing player goes to the end of the queue. 
The game continues until a player wins k consecutive games.

Given the potential of the participants and the deciding factor k, find the potential of the winning player.

Example
Consider n = 4 participants have potential = [3, 2, 1, 4], and k = 2.

Initial position of participants: [1, 2, 3, 4].
Participants 1 and 2 compete. Their potentials are 3 and 2. Player 1 wins due to the higher potential. Player 1 stays at the front of the queue and player 2 moves to the back. Now their positions are [1, 3, 4, 2].
Participants 1 and 3 compete. Their potentials are 3 and 1. Player 1 wins a second consecutive game. Since k = 2, player 1 has won enough consecutive games.
Return player 1's potential, 3.

Function Description
Complete the function getPotentialOfWinner in the editor below.

getPotentialOfWinner has the following parameters:
int potential[n]: the potentials of participants
long_int k: the number of consecutive matches the winning participant must win

Returns
int: the potential of the winning player
'''
from collections import deque
class Solution:
    def getPotentialOfWinner(self, potentials, k):
        queue = deque(potentials)
        win = 0
        curWinner = queue.popleft()
        
        while win < k:
            challenger = queue.popleft()
            if curWinner > challenger:
                queue.append(challenger)
                win += 1
            else:
                queue.append(curWinner)
                win = 1
                curWinner = challenger
        return curWinner


solution = Solution()

# 测试用例 1
potentials = [3, 2, 1, 4]
k = 2
print(solution.getPotentialOfWinner(potentials, k))  # 输出: 3

# 测试用例 2
potentials = [1, 3, 2, 4]
k = 3
print(solution.getPotentialOfWinner(potentials, k))  # 输出: 4

# 测试用例 3
potentials = [2, 1, 3, 4, 5]
k = 2
print(solution.getPotentialOfWinner(potentials, k))  # 输出: 5

# 测试用例 4
potentials = [5, 3, 1, 2, 4]
k = 4
print(solution.getPotentialOfWinner(potentials, k))  # 输出: 5

# 测试用例 5
potentials = [1, 5, 3, 4, 2]
k = 1
print(solution.getPotentialOfWinner(potentials, k))  # 输出: 5
