from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return None

        result = []
        q = deque([root])

        while q:
            n = len(q)
            current = []
            for i in range(n):
                node = q.popleft()
                current.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(current)
        return result
