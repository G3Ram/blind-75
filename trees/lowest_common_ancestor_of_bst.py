"""
Problem: Lowest Common Ancestor of a Binary Search Tree (LeetCode #235)
Difficulty: Easy
Category: Trees

Description:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. The LCA is the lowest node that has both nodes as descendants.

Examples:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

Constraints:
- The number of nodes is in range [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q

Time Complexity Target: O(h)
Space Complexity Target: O(h)
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a binary tree from a level-order list (None represents missing nodes)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def find_node(root, val):
    """Find and return the node with the given value in a BST."""
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return find_node(root.left, val)
    return find_node(root.right, val)


def lowest_common_ancestor_of_bst(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    TODO: Implement your solution here

    Args:
        root: Root of the binary search tree
        p: First node
        q: Second node

    Returns:
        The lowest common ancestor node
    """
    pass


# Test Cases
def test_lowest_common_ancestor_of_bst():
    """Test cases for lowest_common_ancestor_of_bst"""

    test_cases = [
        {
            "name": "Test case 1: LCA is the root",
            "input_root": [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
            "p_val": 2,
            "q_val": 8,
            "expected": 6
        },
        {
            "name": "Test case 2: p is ancestor of q",
            "input_root": [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
            "p_val": 2,
            "q_val": 4,
            "expected": 2
        },
        {
            "name": "Test case 3: Minimal BST, root is LCA",
            "input_root": [2, 1],
            "p_val": 2,
            "q_val": 1,
            "expected": 2
        },
        {
            "name": "Edge case: Both nodes in left subtree",
            "input_root": [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
            "p_val": 0,
            "q_val": 5,
            "expected": 2
        },
        {
            "name": "Edge case: Both nodes in right subtree",
            "input_root": [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
            "p_val": 7,
            "q_val": 9,
            "expected": 8
        },
        {
            "name": "Edge case: Adjacent nodes",
            "input_root": [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
            "p_val": 3,
            "q_val": 5,
            "expected": 4
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: root={test['input_root']}, p={test['p_val']}, q={test['q_val']}")
        print(f"  Expected: {test['expected']}")

        try:
            root = build_tree(test['input_root'])
            p = find_node(root, test['p_val'])
            q = find_node(root, test['q_val'])
            result_node = lowest_common_ancestor_of_bst(root, p, q)

            if result_node is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            elif result_node.val == test['expected']:
                print(f"  ✓ PASSED: {result_node.val}")
                passed += 1
            else:
                print(f"  ✗ FAILED: Got {result_node.val}")
                failed += 1

        except Exception as e:
            print(f"  ✗ FAILED: {type(e).__name__}: {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")

    if failed == 0:
        print("✓ All test cases passed!")
    else:
        print("✗ Some test cases failed. Please review the implementation.")


if __name__ == "__main__":
    test_lowest_common_ancestor_of_bst()
