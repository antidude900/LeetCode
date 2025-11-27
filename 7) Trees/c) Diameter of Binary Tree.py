"""
Approach: The diameter of a tree is the longet height of the left subtree + longest subtree. So in this question, we have to find the diameter of the whole tree
i.e the biggest diameter of the whole tree(can be of any subtree). For this we go the deepest node and start finding diamter from that place. 
And we return its longest height of either the left or right subtree to its parent node for calculating the parent's node subtree diameter.
(Note: You maybe thinking that obviously the upper node with have the higher diameter than lower node as it is being built on top of the lower node.
But think of this: the left subtree of the root node has a diamter of 13 because the the left subtree's left subtree has a height of 5 and right subtree has a height of 8
Now for the root node, its left subtree has a height of 9(max(8,5)+1) and say the right subtree has only a height of 2.
Thus for the root node of the whole tree, we get a diameter of 11. Hence its not always the case that upper node will always have the higher diameter)
"""


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
    
