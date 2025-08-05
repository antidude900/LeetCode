"""
Approach: Given a tree, find if its balanced or not.
For this, we have to find the depth of both nodes at the same level and then check if their difference is atmost 1 or not for finding the balance of the above node
"""

def isBalanced(root: Optional[TreeNode]) -> bool:  
    def dfs(root): 
        if not root:
            return [True,0]    #for checking for it the past left or right subtree was balanced or not and also sending its depth
      
        left = dfs(root.left)    #finding the depth of left subtree
        right = dfs(root.right)    #finding the depth of right subtree
        balanced = left[0] and right[0] and abs(left[1]-right[1])<=1    #if one of the left or right subtree is unbalanced(meaning the left and right node below then result in height diff >1)
                                                                        #then doesnt matter if for the current node its balanced, the whole tree is already unbalanced
        return [balanced,1+max(left[1],right[1])]    #returning the greaterst depth for that node from either its left part or right part(+1 for its own depth)
    return dfs(root)[0]
