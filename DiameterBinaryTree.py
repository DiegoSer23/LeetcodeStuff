class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = [0]
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return -1
            heightLeft = dfs(root.left)
            heightRight = dfs(root.right)
            d[0] = max(d[0], 2 + heightLeft + heightRight)
            return 1 + max(heightLeft, heightRight)
        dfs(root)
        return d[0]
