# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None
        parents = {}
        stack = [root]
        while stack:
            node = stack.pop()

            if node.left:
                stack.append(node.left)
                parents[node.left] = node

            if node.right:
                stack.append(node.right)
                parents[node.right] = node

            if p in parents and q in parents:
                break

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]
        return q
