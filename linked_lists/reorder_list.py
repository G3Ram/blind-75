"""
Problem: Reorder List (LeetCode #143)
Difficulty: Medium
Category: Linked Lists

Description:
Given a singly linked list L: L0→L1→…→Ln-1→Ln, reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→… You may not modify the values, only nodes themselves may be changed.

Examples:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
- The number of nodes is in range [1, 5*10^4]
- 1 <= Node.val <= 1000

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List, Optional


def reorder_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    TODO: Implement your solution here

    Args:
        head: Head of the linked list

    Returns:
        Modified or new linked list head
    """
    pass


# Test Cases
def test_reorder_list():
    """Test cases for reorder_list"""

    # Test case 1
    print("Test case 1...")
    # TODO: Add test case implementation

    # Test case 2
    print("Test case 2...")
    # TODO: Add test case implementation

    # Edge cases
    print("Edge case tests...")
    # TODO: Add edge case tests

    print("✓ All test cases passed!")


if __name__ == "__main__":
    test_reorder_list()
