"""
Approach: Here we need to validate a BST. The first solution that will come in all of our mind will be to check for each node if left.val<node.val<right.val
But heres the flaw. What if the parent node of a node say curr(where curr is the right node of its parent and is greater than its parent) is greater than the left node of curr?(curr is > left node)
For the parent node and curr, it will validate and for the curr and its left node it will validate. But still its node a BST as parent node>left node of its right node
where to be validated every nodes in the right subtree of the parent node should be greater. To fix this, we implement a boundary for each subtree based on its parent node.

Suppose we had a root node x . For its left subtree, they dont have any lower boundary but have a upper boundary i.e the value of x.
Similarly for the right subtree, they dont have any upper boundary but have a lower boundary i.e the value of x
Then for that root node of the subtree, we check if its value is within the boundary. Then we take another subtree from the current subtree and update the boundary for the new subtree same like before
"""

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(node,leftBound,rightBound):
        if not node:  #if we get to the end without any failure(i.e the condition returning false), then then that whole subtree of the main root is validated BST
            return True
          
        if not leftBound<node.val<rightBound:  #but it any of the node doesn't pass the test, then the whole tree is not BST
            return False
          
        return (dfs(node.left,leftBound,node.val) and  
                dfs(node.right,node.val,rightBound))
        #both the left and right subtree should be BST for the whole tree to be BST
        #if we go to the left subtree, a new upper boundary will be set for that subtree i.e value of the parent node of the subtree
        #if we go to the right suubtree, a new lower boundary will be set for that subtree  i.e value of the parent node of the subtree
  
    return dfs(root,float("-inf"),float("inf"))  #the main root will have no boundary at all. so starting the recursion with no boundary
