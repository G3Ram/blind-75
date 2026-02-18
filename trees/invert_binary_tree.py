"""
Problem: Invert Binary Tree (LeetCode #226)
Difficulty: Easy
Category: Trees

Description:
Given the root of a binary tree, invert the tree and return its root.

Examples:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Constraints:
- The number of nodes is in range [0, 100]
- -100 <= Node.val <= 100

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


def tree_to_list(root):
    """Convert a binary tree to a level-order list representation."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def invert_binary_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    TODO: Implement your solution here

    Args:
        root: Root of the binary tree

    Returns:
        Root of the inverted binary tree
    """
    pass


# Test Cases
def test_invert_binary_tree():
    """Test cases for invert_binary_tree"""

    test_cases = [
        {
            "name": "Test case 1: Full binary tree",
            "input": [4, 2, 7, 1, 3, 6, 9],
            "expected": [4, 7, 2, 9, 6, 3, 1]
        },
        {
            "name": "Test case 2: Small three-node tree",
            "input": [2, 1, 3],
            "expected": [2, 3, 1]
        },
        {
            "name": "Edge case: Single node",
            "input": [1],
            "expected": [1]
        },
        {
            "name": "Edge case: Empty tree",
            "input": [],
            "expected": []
        },
        {
            "name": "Edge case: Left-skewed tree",
            "input": [1, 2, None, 3],
            "expected": [1, None, 2, None, 3]
        },
        {
            "name": "Edge case: Right-skewed tree",
            "input": [1, None, 2, None, 3],
            "expected": [1, 2, None, 3]
        },
        {
            "name": "Edge case: Two-level complete tree",
            "input": [1, 2, 3, 4, 5, 6, 7],
            "expected": [1, 3, 2, 7, 6, 5, 4]
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
            result_root = invert_binary_tree(root)
            result = tree_to_list(result_root)

            if test['input'] and result_root is None:
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
    test_invert_binary_tree()
