"""
Problem: Subtree of Another Tree (LeetCode #572)
Difficulty: Easy
Category: Trees

Description:
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values as subRoot, false otherwise.

Examples:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Constraints:
- The number of nodes in root is in range [1, 2000]
- The number of nodes in subRoot is in range [1, 1000]
- -10^4 <= root.val <= 10^4

Time Complexity Target: O(m*n)
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


def subtree_of_another_tree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        root: Root of the main binary tree
        subRoot: Root of the candidate subtree

    Returns:
        True if subRoot is a subtree of root, False otherwise
    """
    pass


# Test Cases
def test_subtree_of_another_tree():
    """Test cases for subtree_of_another_tree"""

    test_cases = [
        {
            "name": "Test case 1: subRoot is a left subtree",
            "input_root": [3, 4, 5, 1, 2],
            "input_subRoot": [4, 1, 2],
            "expected": True
        },
        {
            "name": "Test case 2: subRoot not present (extra node breaks match)",
            "input_root": [3, 4, 5, 1, 2, None, None, None, None, 0],
            "input_subRoot": [4, 1, 2],
            "expected": False
        },
        {
            "name": "Test case 3: Single node trees, same value",
            "input_root": [1],
            "input_subRoot": [1],
            "expected": True
        },
        {
            "name": "Test case 4: subRoot is entire root tree",
            "input_root": [1, 2, 3],
            "input_subRoot": [1, 2, 3],
            "expected": True
        },
        {
            "name": "Edge case: subRoot has no children, root node has children",
            "input_root": [1, 2],
            "input_subRoot": [1],
            "expected": False
        },
        {
            "name": "Edge case: subRoot found in right subtree",
            "input_root": [3, 4, 5, 1, 2],
            "input_subRoot": [5],
            "expected": True
        },
        {
            "name": "Edge case: No matching subtree",
            "input_root": [1, 2, 3],
            "input_subRoot": [4],
            "expected": False
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: root={test['input_root']}, subRoot={test['input_subRoot']}")
        print(f"  Expected: {test['expected']}")

        try:
            root = build_tree(test['input_root'])
            sub_root = build_tree(test['input_subRoot'])
            result = subtree_of_another_tree(root, sub_root)

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
    test_subtree_of_another_tree()
