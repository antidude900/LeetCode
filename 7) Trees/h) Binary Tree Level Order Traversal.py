"""
Approach: Given a binary tree, we have to append the nodes together grouped and sorted according to its level.
Whenever we get to a new level, we create a new nested array for itself (and only once for that level).
Also, we have to pass down the value of the depth so that we can easily add the value to the correct group
then we go to the left and right of the current node incrementing the value of its current depth
"""
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    def dfs(root,depth):
        if not root:
            return None
        
        if len(res) == depth:  #after adding a nested list to res at a new depth, len(res) will be greater than depth. this will avoid making new subarrays at the same depth
            res.append([])
          
        res[depth].append(root.val)
        dfs(root.left,depth+1)
        dfs(root.right,depth+1)
    
    dfs(root,0)
    return res
