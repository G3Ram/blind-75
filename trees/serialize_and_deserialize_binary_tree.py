"""
Problem: Serialize and Deserialize Binary Tree (LeetCode #297)
Difficulty: Hard
Category: Trees

Description:
Design an algorithm to serialize and deserialize a binary tree. Serialization converts a tree to a string, deserialization converts the string back to the tree structure.

Examples:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Constraints:
- The number of nodes is in range [0, 10^4]
- -1000 <= Node.val <= 1000

Time Complexity Target: O(n)
Space Complexity Target: O(n)
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


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        TODO: Implement your solution here

        Encodes a tree to a single string.

        Args:
            root: Root of the binary tree

        Returns:
            String representation of the tree
        """
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        TODO: Implement your solution here

        Decodes a string to a binary tree.

        Args:
            data: String representation of the tree

        Returns:
            Root of the reconstructed binary tree
        """
        pass


# Test Cases
def test_serialize_and_deserialize_binary_tree():
    """Test cases for Codec serialize and deserialize"""

    test_cases = [
        {
            "name": "Test case 1: Standard tree",
            "input": [1, 2, 3, None, None, 4, 5],
            "expected": [1, 2, 3, None, None, 4, 5]
        },
        {
            "name": "Test case 2: Single node",
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
            "expected": [1, 2, None, 3]
        },
        {
            "name": "Edge case: Right-skewed tree",
            "input": [1, None, 2, None, 3],
            "expected": [1, None, 2, None, 3]
        },
        {
            "name": "Edge case: Negative values",
            "input": [-1, -2, -3],
            "expected": [-1, -2, -3]
        },
        {
            "name": "Edge case: Two-level complete tree",
            "input": [1, 2, 3, 4, 5, 6, 7],
            "expected": [1, 2, 3, 4, 5, 6, 7]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            codec = Codec()
            root = build_tree(test['input'])
            serialized = codec.serialize(root)

            if serialized is None:
                print(f"  ✗ FAILED: Function not yet implemented (serialize returned None)")
                failed += 1
                continue

            result_root = codec.deserialize(serialized)
            result = tree_to_list(result_root)

            if test['input'] and result_root is None:
                print(f"  ✗ FAILED: Function not yet implemented (deserialize returned None)")
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
    test_serialize_and_deserialize_binary_tree()
