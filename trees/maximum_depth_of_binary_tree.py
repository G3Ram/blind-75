"""
Problem: Maximum Depth of Binary Tree (LeetCode #104)
Difficulty: Easy
Category: Trees

Description:
Given the root of a binary tree, return its maximum depth. Maximum depth is the number of nodes along the longest path from root to the farthest leaf.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Constraints:
- The number of nodes is in range [0, 10^4]
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


def maximum_depth_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    TODO: Implement your solution here

    Args:
        root: Root of the binary tree

    Returns:
        Maximum depth of the binary tree
    """
    pass


# Test Cases
def test_maximum_depth_of_binary_tree():
    """Test cases for maximum_depth_of_binary_tree"""

    test_cases = [
        {
            "name": "Test case 1: Three-level tree",
            "input": [3, 9, 20, None, None, 15, 7],
            "expected": 3
        },
        {
            "name": "Test case 2: Right-skewed two levels",
            "input": [1, None, 2],
            "expected": 2
        },
        {
            "name": "Edge case: Single node",
            "input": [1],
            "expected": 1
        },
        {
            "name": "Edge case: Empty tree",
            "input": [],
            "expected": 0
        },
        {
            "name": "Edge case: Right-skewed four levels",
            "input": [1, None, 2, None, 3, None, 4],
            "expected": 4
        },
        {
            "name": "Edge case: Balanced four-level tree",
            "input": [1, 2, 3, 4, 5, 6, 7],
            "expected": 3
        },
        {
            "name": "Edge case: Left-heavy unbalanced",
            "input": [1, 2, 3, 4, None, None, None, 5],
            "expected": 4
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
            result = maximum_depth_of_binary_tree(root)

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
    test_maximum_depth_of_binary_tree()
