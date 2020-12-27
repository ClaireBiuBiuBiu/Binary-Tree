#First of all, here is the definistion of the TreeNode which we would use in the following implementation

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output


root = TreeNode(1)

root.right = TreeNode(2)
root.right.left = TreeNode(3)

root.preorderTraversal(root)

#如果是定义在一个class里面 直接用前面的. 后面的 def

# 以下如果分开写
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output


roo = TreeNode(1)

roo.right = TreeNode(2)
roo.right.left = TreeNode(3)

#Method 1
x = Solution()
x.preorderTraversal(roo)
#就是如果是另一个类 先 function弄出来 然后赋值第一个
#Method 2
Solution.preorderTraversal(Solution,roo)
#也就是如果直接用 要分开 solution 并且标明roo