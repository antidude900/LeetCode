"""
Approach: Given a binary tree, we have to insert the rightmost node for each depth in order.
For this, we can implement a rule such that we start adding from the righmost in a depth and only a node from a depth can be inserted
so while staring to adding from the right and we add a node, it will be our rightmost node and thus we dont have to care about the left nodes after that
"""

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node, depth):
        if not node:
            return None
        
        if len(res) == depth:  #this condition allows us to add only node per depth
            res.append(node.val) 
          
        dfs(node.right,depth+1)  #we will be starting to add nodes from the right. this line recurses until checking all the rightmost nodes(maybe null so wont give all the results from only this recursion)
        dfs(node.left,depth+1)  #then we check the latter nodes after the rightmost node. if the rightmost node was null in that depth, then it may have impact in that depth else wont for sure.
    dfs(root,0)
    return res
