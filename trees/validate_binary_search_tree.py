"""
Problem: Validate Binary Search Tree (LeetCode #98)
Difficulty: Medium
Category: Trees

Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST has left subtree nodes < node < right subtree nodes for all nodes.

Examples:
Input: root = [2,1,3]
Output: true
Input: root = [5,1,4,null,null,3,6]
Output: false

Constraints:
- The number of nodes is in range [1, 10^4]
- -2^31 <= Node.val <= 2^31 - 1

Time Complexity Target: O(n)
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


def validate_binary_search_tree(root: Optional[TreeNode]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        root: Root of the binary tree

    Returns:
        True if the tree is a valid BST, False otherwise
    """
    pass


# Test Cases
def test_validate_binary_search_tree():
    """Test cases for validate_binary_search_tree"""

    test_cases = [
        {
            "name": "Test case 1: Valid BST",
            "input": [2, 1, 3],
            "expected": True
        },
        {
            "name": "Test case 2: Invalid BST (right child smaller than root)",
            "input": [5, 1, 4, None, None, 3, 6],
            "expected": False
        },
        {
            "name": "Edge case: Single node",
            "input": [1],
            "expected": True
        },
        {
            "name": "Edge case: Duplicate values (not allowed in BST)",
            "input": [1, 1],
            "expected": False
        },
        {
            "name": "Edge case: Right-skewed valid BST",
            "input": [1, None, 2, None, 3],
            "expected": True
        },
        {
            "name": "Edge case: Tricky invalid - locally valid but globally wrong",
            "input": [5, 4, 6, None, None, 3, 7],
            "expected": False
        },
        {
            "name": "Edge case: Left-skewed valid BST",
            "input": [3, 2, None, 1],
            "expected": True
        },
        {
            "name": "Edge case: All negative values, valid BST",
            "input": [-3, -5, -1],
            "expected": True
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            root = build_tree(test['input'])
            result = validate_binary_search_tree(root)

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            elif result == test['expected']:
                print(f"  ✓ PASSED: {result}")
                passed += 1
            else:
                print(f"  ✗ FAILED: Got {result}")
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
    test_validate_binary_search_tree()
