'''
Amazon Web Services (AWS) has millions of servers that provide on-demand cloud computing platforms to the customers.

In one AWS center, there are n processes to be executed and m processors to execute them. 
The ith process requires power[i] for execution. A processor can provide power within its range minPower through maxPower[i].
Process i can be executed on processor j if minPower[j] ≤ power[i] ≤ maxPower[j].

Given the power consumption of n processes, the range of processor power in m processors, find:

the number of processes which can be executed on the processor
the sum of power consumed by the processes that it can serve
Function Description

Complete the function processExecution in the editor.

amazon-process-executionm processExecution has the following parameters:

int power[n]: the power consumption of processes
int minPower[m]: the minimum bounds of the ranges of processor power
int maxPower[m]: the maximum bounds of the ranges of processor power

Returns
long_int[m][2]: the #th element of this array consists of 2 integers - the number of processes that lie within the range of the #th processor, and the sum of the power consumption of those processes.

Input:  power = [7, 6, 8, 10], minPower = [6, 3, 4], maxPower = [10, 7, 9]
Output: [[4, 31], [2, 13], [3, 21]] 
'''

class Solution:
    def processExecution(self, power, minPower, maxPower):
        n = len(power) # 线程数
        m = len(minPower) # 处理器数量
        ans = []
        # 遍历每一个处理器, 看其能处理的线程情况
        for i in range(m):
            count = 0
            result = 0
            for j in range(n):
                if minPower[i] <= power[j] <= maxPower[i]:
                    count += 1
                    result += power[j]
            ans.append([count, result])
        return ans
    
# 示例测试
solution = Solution()
power = [7, 6, 8, 10]
minPower = [6, 3, 4]
maxPower = [10, 7, 9]
print(solution.processExecution(power, minPower, maxPower))  # 输出: [[4, 31], [2, 13], [3, 21]]

power = [11, 11, 11]
minPower = [8, 13]
maxPower = [11, 100]
print(solution.processExecution(power, minPower, maxPower))  # 输出: [[4, 31], [2, 13], [3, 21]]

            

