'''
The developers at Amazon employ several algorithms for encrypting passwords. 
In one algorithm, the developers aim to encrypt palindromic passwords.
 Palindromic passwords are ones that read the same forward and backward.

The algorithm rearranges the characters to have the following characteristics:

It is a rearrangement of the original palindromic password.
It is also a palindrome.
Among all such palindromic rearrangements, it is the lexicographically smallest.
Given the original palindromic password that consists of lowercase English characters only, find the encrypted password.

A string s is considered to be lexicographically smaller than the string t of the same length if the first character in s that differs from that in t is smaller. 
For example, "abcd" is lexicographically smaller than "abdc" but larger than "abad".

Note that the encrypted password might be the same as the original password if it is already lexicographically smallest.

Example

Given s = "bbaabb"

The encrypted password is "aabbba"
'''
from collections import Counter
class Solution:
    # 生成可以用给定回文字符串的字符形成的字典序最小的回文
    def findEncryptedPassword(self, password):
        # 记录原回文字符串中的字符出现频率
        record = Counter(password)
        ans = []
        odd = None

        for char, count in sorted(record.items()):
            if count % 2 == 1:
                if odd:
                    return "" # 如果有多个字符出现奇数次 则无法形成回文
                odd = char
            ans.append(char * (count // 2))
        
        ans = "".join(ans)
        if odd:
            return ans + odd + ans[::-1]
        return ans + ans[::-1]
    

# 示例测试
solution = Solution()
password = "bbaabb"
print(solution.findEncryptedPassword(password))  # 输出: abbbbba

password2 = "aabbcc"
print(solution.findEncryptedPassword(password2))  # 输出: abccba

password3 = "aabb"
print(solution.findEncryptedPassword(password3))  # 输出: abba

password4 = "abc"
print(solution.findEncryptedPassword(password4))  # 输出: ""

            