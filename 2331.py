# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        if root.val == 0 or root.val == 1:
            return bool(root.val)
        q = [root]
        while q:
            element = q.pop()
            if (element.left.val != 1 and element.left.val != 0) or (element.right.val != 1 and element.right.val != 0):
                q.append(element)
            if element.left.val != 1 and element.left.val != 0:
                q.append(element.left)
            if element.right.val != 1 and element.right.val != 0:
                q.append(element.right)
            if (element.right.val == 1 or element.right.val == 0) and (element.left.val == 1 or element.left.val == 0):
                if element.val == 3:
                    element.val = element.right.val and element.left.val
                if element.val == 2:
                    element.val = element.right.val or element.left.val

        return bool(root.val)


print(Solution().evaluateTree(TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))))

