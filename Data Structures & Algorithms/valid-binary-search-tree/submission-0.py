# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            output.append(root.val)
            helper(root.right)
        helper(root)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:   # strict: use >= to reject duplicates too
                return False
        return True