class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        d = {}
        for x in descriptions:
            d[x[0]] = (TreeNode(x[0]), 0)
            d[x[1]] = (TreeNode(x[1]), 0)
        for x in descriptions:
            if x[2]:
                d[x[0]][0].left = d[x[1]][0]
            else:
                d[x[0]][0].right = d[x[1]][0]
            d[x[1]][1] += 1

        for x in d.values():
            if x[1] == 0:
                return x[0]