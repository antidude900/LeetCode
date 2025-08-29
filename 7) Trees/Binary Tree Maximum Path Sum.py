"""
Approach: Given a binary tree, we have to return the maximum sum in a path. Note that in a path, we cannot split in two different directions.
So for getting the path sum for a root of a subarray, we can get the max path of its left subtree and the max path of its right subtree and add them both to the value of the node
You might be saying its a split but its not! Because the line is going in a single direction i.e left to right or right to left. 
Then we can check if its the max pathsum by comparing it with the current max pathsum
Then we can go to more upper subtrees and for the leftMax/rightMax of th roots of that subtree, we return the value of the previous root+maximum among the pathsum of its left or right branch
But why maximum among the left and right branch? well because the upper subtree's root will make its own split and thus we cant make further split and it will give the path more than one direction
So we can either include the pathsum of the lower root's left or right branch(the highest one).
Also, if we get a pathsum of negative from either its left or right, we dont even include that branch in the path as it just decreases and we have a option not to take it all.
But if the root itself is negative, still we take it as for its path, we have to take the root itself to connect with the left or right path or both.
"""
class Solution:
    maxSum = None
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val    #assuing the root val to be the max pathsum as the left or right pathsum may be negative. so the inital safest option is the main root
        
        def dfs(root):  
            if not root: 
                return 0
    
            leftMax = max(dfs(root.left),0)    #dfs(root.left) returns the max pathusm of its left branch. but if its <0 we dont include that in the root's pathsum at all
            rightMax = max(dfs(root.right),0)    #dfs(root.left) returns the max pathusm of its left branch. but if its <0 we dont include that in the root's pathsum at all

            self.maxSum = max(self.maxSum,root.val+leftMax+rightMax)    #finding the pathsum of the path which is bent at the current root and checking if its max pathsum or not

            return root.val+max(leftMax,rightMax)    #returning the max pathsum of current branch without any splits for the upper roots as the upper roots themselves split into left and right
                                                     #which is considered as a bend but any further splits will be considered as a split splitting the path into two different directions

        dfs(root)
        return self.maxSum
