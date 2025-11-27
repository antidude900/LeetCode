"""
Approach: Given two binary tree, we have to find if both are same or not.
So we first check if the root nodes are same or not. If yes, then we compare the left nodes and also the right nodes.
If same we go on continuing the search down and down else we return False saying the two trees are not the same.
If both the trees get no 'False' flag until we reach the end of both the subtrees, then we return True saying for that subtree, its completely same.
But say the left subtree satisfies the being 'same property' with the root node above it. But the right subtree also has to satisfy that property. 
So we have to check if botht the subtrees sastify the property.
"""

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    
    if p and q and p.val == q.val:
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    else:
        return False
