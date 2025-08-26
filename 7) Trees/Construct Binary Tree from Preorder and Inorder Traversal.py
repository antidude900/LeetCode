"""
Approach: Given the inorder and preorder traversal of a tree(each are arrays containing only values and are unique i.e they dont contain duplicates), we have to construct a binary tree from that.
For this let's take an example to be clear of how we will be traversing through the arrays.
Preorder (Root, Left, Right): 1 2 4 5 7 3 6 8 9 10 
Inorder (Left, Root, Right): 4 2 7 5 1 6 8 3 10 9

The tree is like this:
         1
       /   \
      2     3
     / \   / \
    4   5 6   9
       /    \ /
      7      8 10

From the preorder, first we get the root of the current tree, then finding its place in the inorder the left side to it becomes its left subtree and right side to it becomes the right subtree.
thus the left sude of it is the inorder of the left subtree and the right side of it is the inorder of the rught subtree
Also the index at which it is at inorder is the place in preorder upto which(from the root to that place) we need elements for the left subtree as the preorder of the left subtree
And the remaning part of the preorder will be the preorder of the right subtree

In this way we make subarrays of preorder and inorder for each subtree to get the preorder and inorder of the current subtree and thus make tree based on that 
(we make a node for root of the tree and then for its left, we find the preorder and inoder for the left subtree of it. then we give those to find the left subtree and as it gives back the 
node of the root of the left subtree we assign that left of our root. similarly for the right)

Also for finding out the index of root in inorder, we can use inorder.index() but using it for each node will result a time complexity of O(n^2)
(as for each node, we have to search through the inorder array to find the index where root is int)
So we can create a hashmap where we precompute the index of each root. and as we only take O(1) time to search value in hasmap, we get a overall time complexity of O(n)
"""

"""O(n^2)"""
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:    #If there is no preorder or inorder left, then we are at the end of the tree. so return None
        return None
      
    root = TreeNode(preorder[0])    #making node for the root of the current subtree
    idx = inorder.index(root.val)    #finding the index of the root at inorder arrray
  
    root.left = buildTree(preorder[1:idx+1],inorder[:idx])    #giving the preorder and inorder subtree to make the left subtree(will return the node of the root of the left subtree)
    root.right = buildTree(preorder[idx+1:],inorder[idx+1:])    #giving the preorder and inorder subtree to make the right subtree(will return the node of the root of the right subtree)
    
    return root

"""O(n)"""
def buildTree(self, preorder, inorder):
    inorderMap = {val: i for i, val in enumerate(inorder)} #make a hashmap connecting each value with their index in inorder map for O(1) checkup
    self.rootIdx = 0    
    """to keep track of the index of root(you can see from the preorder array and tree that the array gives root for each subtree in sequential order if we go on making subtree in order of 
    root, left, right. so yeah we will be making subtree in that order and thus increment our root index value by 1 at each subtree to get the index of the root of the upcoming tree"""
                        
    def buildSubTree(start, end):    
        if start > end:
            return None
            
        root_val = preorder[self.rootIdx]
        self.rootIdx += 1    
        
        root = TreeNode(root_val)
        idx = inorderMap[root_val]
        
        root.left = buildSubTree(start, idx - 1)    #note there the start and end are only here to know when our subtree is fully built
                                                    #the main tree building is done by the rootIdx which gives the root of the current subtree for which we will be making a node
        root.right = buildSubTree(idx + 1, end)
        
        return root
        
    return buildSubTree(0, len(inorder) - 1)



    

