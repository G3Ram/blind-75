"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal (LeetCode #105)
Difficulty: Medium
Category: Trees

Description:
Given two integer arrays preorder and inorder, construct and return the binary tree.

Examples:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- All values are unique

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def construct_binary_tree_from_preorder_and_inorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    TODO: Implement your solution here

    Args:
        preorder: Preorder traversal of the binary tree
        inorder: Inorder traversal of the binary tree

    Returns:
        Root of the reconstructed binary tree
    """
    pass


# Test Cases
def test_construct_binary_tree_from_preorder_and_inorder():
    """Test cases for construct_binary_tree_from_preorder_and_inorder"""

    test_cases = [
        {
            "name": "Test case 1: Three-level tree",
            "preorder": [3, 9, 20, 15, 7],
            "inorder": [9, 3, 15, 20, 7],
            "expected": [3, 9, 20, None, None, 15, 7]
        },
        {
            "name": "Test case 2: Single node",
            "preorder": [1],
            "inorder": [1],
            "expected": [1]
        },
        {
            "name": "Test case 3: Balanced three-node tree",
            "preorder": [3, 1, 2],
            "inorder": [1, 3, 2],
            "expected": [3, 1, 2]
        },
        {
            "name": "Edge case: Left-skewed tree",
            "preorder": [1, 2, 3],
            "inorder": [3, 2, 1],
            "expected": [1, 2, None, 3]
        },
        {
            "name": "Edge case: Right-skewed tree",
            "preorder": [1, 2, 3],
            "inorder": [1, 2, 3],
            "expected": [1, None, 2, None, 3]
        },
        {
            "name": "Edge case: Two-node tree (root with left child)",
            "preorder": [2, 1],
            "inorder": [1, 2],
            "expected": [2, 1]
        },
        {
            "name": "Edge case: Two-node tree (root with right child)",
            "preorder": [1, 2],
            "inorder": [1, 2],
            "expected": [1, None, 2]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: preorder={test['preorder']}, inorder={test['inorder']}")
        print(f"  Expected: {test['expected']}")

        try:
            result_root = construct_binary_tree_from_preorder_and_inorder(
                test['preorder'], test['inorder']
            )
            result = tree_to_list(result_root)

            if test['preorder'] and result_root is None:
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
    test_construct_binary_tree_from_preorder_and_inorder()
