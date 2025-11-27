"""
Approach:
Given a BST, we have to find the kth smallest node.
For this, we first have to go to the smallest node and start climbing up from there upto k time.
The climb will be simple, first its right subtree if exists(as all the nodes in its right subtree will be smaller than its parent node)
"""

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    res = None
  
    def dfs(root): 
        if not root:
            return None
            
        dfs(root.left)
        #after going to the most left node, i.e the most smallest node we start searching for the kth smallest
        
        nonlocal res,k    #nested function always creates a locat variable for itself. so to avoid that, we use give it nonlocal scope    
        k-=1    #the current node is of the smallest.  so deduct the value of k
        if k == 0:    #if k = 0, this is the node we are looking for (If it was 0-indexed, we have to set k=k+1 to bring the count back to 1 indexed
            res = root.val    #if we update it oustide, then it gets replaced by the right of its parent node as k-=1 makes it k=-1 and thus k!=0 so will go towards dfs(root.right)
                              #then you might think of fix of k<=0 but still it will get replaced by its parent node as "if k <= 0: return" stops the execution after it 
                              #but still the update of res before "if k <= 0: return" will run. so res will be replaced by its parent node though the node rn is the answer
            return 
            
        dfs(root.right)    #else we go to its right subtree
    
    dfs(root)
    return res
