"""
Approach: Given a binary tree, we need to deserialize(making tree into a list) and serialize(making list into a tree).
You might have already seen the deserialized form in the input section of the Tree questions.
If we have a tree like this:
         1
       /   \
      2     3
           / \
          6   9
It deserialize form will look like:
"1,2,none,none,3,6,none,none,9,none,none"

So for deserializing we go dfs through left and then right adding appending value of each node and none if no node in the list.
As we need it in form of string, we use ',' as a delimiter

Now for serializing, we first convert the string into a list. 
Then we go through the list making the parent node, its left node until we reach rock bottom(both the left and right children are none) of the subtree of the left node
and then the right node.
"""

def serialize(root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    res = []
    def dfs(root):
        if not root:
            res.append("null")
            return
        res.append(str(root.val))
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return ','.join(res)
    
def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    data = data.split(",")
    self.i = 0
    def dfs(): 
        if data[self.i] == "null":
            self.i+=1 #for each recursion of dfs, we have advanced one step in the list. so we have to increment the index
            return None
        
        node = TreeNode(int(data[self.i]))
        self.i+=1
        node.left = dfs()  #now doing the iteration of the list for the left sub tree until hit rock bottom
        node.right = dfs()  #then doing the right subtree
        return node  #after hitting rock bottom of that subtree, returning the root of the subtree
      
    return dfs()
