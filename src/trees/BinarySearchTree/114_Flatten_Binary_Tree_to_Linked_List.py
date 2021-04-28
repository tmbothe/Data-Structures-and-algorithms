from typing import TreeNode


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode) -> None:

    stack = [root]
    current = None
    while current:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        if stack:
            current.right = stack[-1]
        current.left = None


if __name__ == '__main__':
    root = [1, 2, 5, 3, 4, null, 6]
    #Output: [1,null,2,null,3,null,4,null,5,null,6]
