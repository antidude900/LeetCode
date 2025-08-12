"""
Approach: Given two trees of main root say root and subRoot we need to find if the subRoot tree is the subtree of the root tree.
For this, we need to first discuss what things are considered as subTree.
1) if both the whole trees are same.
2) if one of the subtree of the root tree is same as the subRoot tree
2) if the whole subtree is null
3) if both the whole trees are null
(but the root tree cant be null when the subtree is not null)

So, to find out subtree we have to find sameTree on each of the nodes of the rootTree. so, we take the isSameTree(which we have done already before) as the helper function fpr that.
"""


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot: return True    #if subRoot is null, its subtree no matter what(this is only imp for the first inital check)
    if not root: return False    #if root is null and subRoot isnt null(if we come to this line after the upper line, it means subRoot isnt null), then its not subTree 
    if isSameTree(root,subRoot): return True    #checking if the current root of the tree satistifes the sametree condition with the subroot
        
    return (isSubtree(root.left,subRoot) or    #if not, we check for its left and right subtree for the subtree
    isSubtree(root.right,subRoot))    #we cant only recursre on isSameTree because though one node may not be same but the other can be. 
                                      #so we have to recurse isSubTree to go through each node
  
def isSameTree(p,q):
    if not p and not q: return True
    
    if p and q and p.val == q.val:
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else: 
        return False
    
