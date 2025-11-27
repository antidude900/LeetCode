count = 0
def goodNodes(self, root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return
        if node.val >= max_val:
            self.count += 1
            max_val = node.val
        dfs(node.left, max_val)
        dfs(node.right, max_val)
        
    dfs(root, root.val)
    return self.count
            
