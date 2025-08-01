"""
Approach:
We are given a tree and we need to invert it meaning we have to swap the left and right nodes at each level
Thus we first recurse towards left subtree and swap all of its left and right nodes and each level
and do the same for the right
"""

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return 
    
    root.left , root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
