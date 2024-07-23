class Solution:

    '''
    判断给定二叉树是否为平衡二叉树
    返回true/false
    '''
    def balancedBinaryTree(self, root):

        def dfs(node):
            if not node:
                return 0, True
            leftHeight, leftBalance = dfs(node.left)
            rightHeight, rightBalance= dfs(node.right)

            curHeight = max(leftHeight, rightHeight) + 1
            if leftBalance and rightBalance and abs(leftHeight - rightHeight) <= 1:
                return curHeight, True
            else:
                return curHeight, False
            
        _, ans = dfs(root)
        return ans

    '''
    判断给定二叉树是否为平衡二叉搜索树
    返回true/false
    '''
    def balancedBST(self, root):
        pass
    
    '''
    将一棵非平衡二叉树转换成平衡二叉树
    返回新平衡二叉树的根节点
    '''
    def convertBalancedBinaryTree(self, root):
        pass

    '''
    将一棵非平衡二叉搜索树转换成平衡二叉搜索树
    返回新平衡二叉搜索树的根节点
    '''
    def convertBalancedBST(self, root):
        pass