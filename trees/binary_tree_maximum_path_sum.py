"""
Problem: Binary Tree Maximum Path Sum (LeetCode #124)
Difficulty: Hard
Category: Trees

Description:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge. A path does not need to pass through the root. Return the maximum path sum of any non-empty path.

Examples:
Input: root = [1,2,3]
Output: 6
Explanation: Path is 2 -> 1 -> 3
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: Path is 15 -> 20 -> 7

Constraints:
- The number of nodes is in range [1, 3*10^4]
- -1000 <= Node.val <= 1000

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


def binary_tree_maximum_path_sum(root: Optional[TreeNode]) -> int:
    """
    TODO: Implement your solution here

    Args:
        root: Root of the binary tree

    Returns:
        Maximum path sum of any non-empty path in the tree
    """
    pass


# Test Cases
def test_binary_tree_maximum_path_sum():
    """Test cases for binary_tree_maximum_path_sum"""

    test_cases = [
        {
            "name": "Test case 1: Path through root",
            "input": [1, 2, 3],
            "expected": 6
        },
        {
            "name": "Test case 2: Path in right subtree",
            "input": [-10, 9, 20, None, None, 15, 7],
            "expected": 42
        },
        {
            "name": "Edge case: Single positive node",
            "input": [5],
            "expected": 5
        },
        {
            "name": "Edge case: Single negative node",
            "input": [-3],
            "expected": -3
        },
        {
            "name": "Edge case: All negative values (best is single root node)",
            "input": [-1, -2, -3],
            "expected": -1
        },
        {
            "name": "Edge case: Mix of positive and negative",
            "input": [2, -1, 3],
            "expected": 5
        },
        {
            "name": "Edge case: Left-heavy path",
            "input": [5, 4, None, 3],
            "expected": 12
        },
        {
            "name": "Edge case: Ignore negative branch",
            "input": [1, -2, 3],
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
            result = binary_tree_maximum_path_sum(root)

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
    test_binary_tree_maximum_path_sum()
