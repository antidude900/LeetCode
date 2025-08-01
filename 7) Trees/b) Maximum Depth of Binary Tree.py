"""
Approach:
We are given a binary tree and we have to find the max depth of the tree(here we assume depth of a node to be 1 in its onw level)
[Note: A tree's max depth and height will be the same]
We can use recursion to simplify the process. We first take 1 as the depth of its own self and add the depth of its left or right sub tree either one who is the biggest
hence we apply the same search for the maxdepth for tits lef and right sub tree
"""

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: #if there's no node, we cant add anything to the depth
        return 0
    
    return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
