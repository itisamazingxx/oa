'''
Amazon is developing a string matching library. 
You are to develop a service that finds the longest substring that matches a given regex.

More formally, you are given two strings, a text string text, and a regex expression regex. 
The string regex contains exactly one wildcard character *. A wildcard character * matches any sequence of zero or more lowercase English characters. 
A regex matches some string if it is possible to replace the wildcard character with some sequence of characters such that the regex expression becomes equal to the string.
No other character can be changed. For example, regex abc* matches "abccd", "abccbd", and "abcccd" whereas it does not match the strings "abcd", "abzcd", "abcdd".

Return the length of the longest substring of text that matches the regex expression regex. Return -1 if there is no such substring.

Note: A substring is a contiguous sequence of characters within a string.

Example
Given text = "hackerrank", regex = "ack*r", the following substrings match regex:

"acker", we can replace * with "e" and regex becomes equal to "acker". Length = 5.
"ackerr", we can replace * with "er" and regex becomes equal to "ackerr". Length = 6.
Return the length of the longest matching substring, which is 6.
'''
class Solution:
    def getLongestMatch(self):
        pass