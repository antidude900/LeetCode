"""
Approach: Given a binary tree, we havve to validate if that tre is binary search tree or not. 
To be a BST, every node should be greater than any node towards its left and small than towards its right. 
So we cant only check with its direct children and have to compare with every other node towards its left and towards its right
(We dont have to do for nodes at the other branch of its parent node as we will do the same comparision process for the parent node)
Doing this recursively for every node is alot expensive so we rather make boundary for the next left and right nodes according to the past nodes
(The boundary is passed on updated for each recursion stack so dont need to worry about calculating the boundary each time from scratch)
Say we move on to the left branch from any node. The right boundary(max boundary) is set as the parent node itself as no node in the left branch can be greater than it.
Say we move on to the right branch from any node. The left boundary(min boundary) is set as the parent node itself as node node in the right branch can be lesser than it.
In this way, we make a universal checker to validify that the left nodes are always lesser than the right nodes.
"""

def isValidBST(root: Optional[TreeNode]) -> bool:
    def valid(root,left,right):
        if not root:
            return True
        
        if not left<root.val<right:
            return False
        
        return valid(root.left,left,root.val) and valid(root.right,root.val,right)
    return valid(root,float("-inf"),float("inf"))
