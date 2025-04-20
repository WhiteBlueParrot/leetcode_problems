"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


"""
from typing import Optional


# https://leetcode.com/problems/same-tree/

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# The number of nodes in both trees is in the range [0, 100]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # If both nodes are None, they are identical
    if p is None and q is None:
        return True
    # If only one of the nodes is None, they are not identical
    if p is None or q is None:
        return False
    # Check if values are equal and recursively check left and right subtrees
    if p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    # Values are not equal, they are not identical
    return False


pp = TreeNode(1, TreeNode(2), TreeNode(3))
qq = TreeNode(1, TreeNode(2), TreeNode(3))
print(is_same_tree(pp, qq))

pp = TreeNode(1, TreeNode(2))
qq = TreeNode(1, None, TreeNode(2))
print(is_same_tree(pp, qq))

pp = TreeNode(1, TreeNode(2), TreeNode(1))
qq = TreeNode(1, TreeNode(1), TreeNode(2))
print(is_same_tree(pp, qq))
