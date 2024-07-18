'''
Amazon Web Services (AWS) stores grayscale images as an array of white and black pixels. 
The image is stored as a binary string where a white pixel is represented by '1', and a black pixel is represented by '0'. 
The reverse of the image is represented as the reverse of this binary representation. For example, the reverse of "11010" is "01011". 
They want to store the reverse of each image as a backup. 
In order to reproduce the reverse from the original, the following operation can be performed any number of times: 
remove any character from the string and append it to the end of the string, i.e., choose any pixel and shift it to the end of the string.

Given the binary representation of pixels denoted by image, find the minimum number of operations needed to produce its reverse.
'''
class Solution:
    def findMinimumOperations(self, image):
        left, right = 0, len(image) - 1
        ans = 0
        while left < right:
            if image[left] == image[right]:
                left += 1
                right -= 1
            else:
                ans += 1
                left += 1
        return ans
    
solution = Solution()
image = "0100110"
print(solution.findMinimumOperations(image))