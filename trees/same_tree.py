"""
Problem: Same Tree (LeetCode #100)
Difficulty: Easy
Category: Trees

Description:
Given the roots of two binary trees p and q, check if they are the same or not. Two trees are same if they are structurally identical and nodes have the same value.

Examples:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Constraints:
- The number of nodes in both trees is in range [0, 100]
- -10^4 <= Node.val <= 10^4

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


def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        p: Root of the first binary tree
        q: Root of the second binary tree

    Returns:
        True if the trees are identical in structure and values, False otherwise
    """
    pass


# Test Cases
def test_same_tree():
    """Test cases for same_tree"""

    test_cases = [
        {
            "name": "Test case 1: Identical trees",
            "input_p": [1, 2, 3],
            "input_q": [1, 2, 3],
            "expected": True
        },
        {
            "name": "Test case 2: Different structure",
            "input_p": [1, 2],
            "input_q": [1, None, 2],
            "expected": False
        },
        {
            "name": "Test case 3: Same structure, different values",
            "input_p": [1, 2, 1],
            "input_q": [1, 1, 2],
            "expected": False
        },
        {
            "name": "Edge case: Both empty",
            "input_p": [],
            "input_q": [],
            "expected": True
        },
        {
            "name": "Edge case: One empty, one not",
            "input_p": [1],
            "input_q": [],
            "expected": False
        },
        {
            "name": "Edge case: Both single same node",
            "input_p": [1],
            "input_q": [1],
            "expected": True
        },
        {
            "name": "Edge case: Both single different nodes",
            "input_p": [1],
            "input_q": [2],
            "expected": False
        },
        {
            "name": "Edge case: Deep identical trees",
            "input_p": [1, 2, 3, 4, 5, 6, 7],
            "input_q": [1, 2, 3, 4, 5, 6, 7],
            "expected": True
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: p={test['input_p']}, q={test['input_q']}")
        print(f"  Expected: {test['expected']}")

        try:
            p = build_tree(test['input_p'])
            q = build_tree(test['input_q'])
            result = same_tree(p, q)

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
    test_same_tree()
