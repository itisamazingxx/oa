class Solution:
    def timeMachine(self, years):
        n = len(years)
        ans = 0
        for i in range(n - 1):
            if years[i] < years[i + 1]:
                ans += 1
            elif years[i] > years[i + 1]:
                ans += 2
        return ans
    
'''
Imagine that you have a time machine. 
You are given an array years. You start in the year years[0]. 
First, you want to travel to years[1], then to years[2], and so on. 
Your task is to calculate the time required to visit all the years from the list in order.

The time required to travel from the year A to the year B is calculated as follows:

0 hours if A == B
1 hour if A < B (going forwards in time)
2 hours if A > B (going backwards in time)

Example:

For years = [2000, 1990, 2005, 2050], the output should be solution(years) = 4.

First you go from 2000 to 1990, which requires 2 hours.
Then you go from 1990 to 2005, which requires 1 hour.
Then you go from 2005 to 2050, which requires 1 hour.
In total, you need 2 + 1 + 1 = 4 hours.
For years = [2000, 2021, 2005, 2050], the output should be solution(years) = 3.

First, you go from 2000 to 2021, which requires 1 hour.
Then you go from 2021 to 2005, which requires 2 hours.
In total, you need 1 + 2 = 3 hours.
For years = [2021, 2021, 2005], the output should be solution(years) = 2.

First, you go from 2021 to 2021, which requires 0 hours as the trip takes place within the same year.
Then you go from 2021 to 2005, which requires 2 hours.
In total, you need 0 + 2 = 2 hours.
'''