# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        self.k = k
        self.ans = None

        def inorder(root):
            if root is None:
                return None
            inorder(root.left, k)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
            inorder(root.right, k)

        inorder(root)

        return self.ans
