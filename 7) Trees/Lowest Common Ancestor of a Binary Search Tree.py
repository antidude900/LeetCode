"""
Approach: Given a BST and two nodes say p and q, we have to find the lowest common ancestor between them.
If we have both p and q on the same subtree of a node, then the common ancestor lies in that subtree and so to find that ancestor we so go that subtree
But if they are both in different subtrees, then the node connecting those subtree will be the common ancestor.
So, we have to go on until we seperate them into seperate subtrees. 
But what if p is the ancestor of q. Then we can never get those as a seperate subtrees. But we do assume it to be in different subtrees as p doesnt lie in the subtree of q
Thus the common node connecting them will be p itself thus the common ancestor
"""

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    curr = root
    while True:    #p and q are guarenteed in the BST. Therefore its guarenteed to find the common ancestor and so we go on searching until we find one
        if p.val<curr.val and q.val<curr.val:    #if both lie in the left subtree of the current node, we go to the left subtree for further search
            curr = curr.left
        elif p.val>curr.val and q.val>curr.val:    #if both lie in the right subtree of the current node, we go to the right subtree for further search
            curr = curr.right
        else:    #if both lie in the different subtrees of the current node, then the current node is the common ancesetor
            return curr
