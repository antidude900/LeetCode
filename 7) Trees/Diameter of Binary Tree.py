def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    res = 0 
    def dfs(node):
        nonlocal res
        if not node:
            return 0
        
        left = dfs(node.left)  #first going to the lefmost node
        right = dfs(node.right)  #the node might have some more children node to its right
        res = max(res,left+right)  #the sum of the height of the left and right subtree of a node is its diameter
        
        return 1+max(left,right)  #passing the node's height as the maximum height of its from either left or right subtree + 1(including itself)
      
    dfs(root)
    return res
    
