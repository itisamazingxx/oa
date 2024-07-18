class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Find the maximum path sum between root and leaf node of a binary tree
'''
class Solution:
    def maxPathSum(self, root):
        # 方法1: dfs, 用额外数组储存结果值
        # 找二叉树中所有的pathSum, 选择最大的
        ans = []

        def dfs(node, sum):
            if not node:
                return
            
            sum += node.val

            if not node.left and not node.right:
                ans.append(sum)
                return
            
            dfs(node.left, sum)
            dfs(node.right, sum)

        dfs(root, 0)
        return max(ans) if ans else 0 # O(n)的时间复杂度
        # 整体时间复杂度O(n^2)

    def maxPathSum2(self, root):
        # 方法2: 递归过程中直接返回最大结果
        # 可以把时间复杂度降低到O(n)

        def dfs(node):
            if not node:
                return 0
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            return node.val + max(leftSum, rightSum)
        
        return dfs(root)
    
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

'''
  -10
 /   \
9    20
     / \
    15  7
'''

solution = Solution()
print(solution.maxPathSum(root))
print(solution.maxPathSum2(root))
