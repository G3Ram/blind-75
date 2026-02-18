"""
Problem: Kth Smallest Element in a BST (LeetCode #230)
Difficulty: Medium
Category: Trees

Description:
Given the root of a binary search tree and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Examples:
Input: root = [3,1,4,null,2], k = 1
Output: 1
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
- The number of nodes is n
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

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


def kth_smallest_element_in_bst(root: Optional[TreeNode], k: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        root: Root of the binary search tree
        k: 1-indexed position of the smallest element to find

    Returns:
        The kth smallest value in the BST
    """
    pass


# Test Cases
def test_kth_smallest_element_in_bst():
    """Test cases for kth_smallest_element_in_bst"""

    test_cases = [
        {
            "name": "Test case 1: k=1 (smallest element)",
            "input_root": [3, 1, 4, None, 2],
            "k": 1,
            "expected": 1
        },
        {
            "name": "Test case 2: k=3 in larger BST",
            "input_root": [5, 3, 6, 2, 4, None, None, 1],
            "k": 3,
            "expected": 3
        },
        {
            "name": "Test case 3: Single node, k=1",
            "input_root": [5],
            "k": 1,
            "expected": 5
        },
        {
            "name": "Edge case: k equals n (largest element)",
            "input_root": [3, 1, 4, None, 2],
            "k": 4,
            "expected": 4
        },
        {
            "name": "Edge case: k=1 in larger BST",
            "input_root": [5, 3, 6, 2, 4, None, None, 1],
            "k": 1,
            "expected": 1
        },
        {
            "name": "Edge case: Right-skewed BST, k=2",
            "input_root": [1, None, 2, None, 3],
            "k": 2,
            "expected": 2
        },
        {
            "name": "Edge case: Left-skewed BST, k=3",
            "input_root": [3, 2, None, 1],
            "k": 3,
            "expected": 3
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: root={test['input_root']}, k={test['k']}")
        print(f"  Expected: {test['expected']}")

        try:
            root = build_tree(test['input_root'])
            result = kth_smallest_element_in_bst(root, test['k'])

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
    test_kth_smallest_element_in_bst()
