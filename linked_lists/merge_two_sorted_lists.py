"""
Problem: Merge Two Sorted Lists (LeetCode #21)
Difficulty: Easy
Category: Linked Lists

Description:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Examples:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Constraints:
- The number of nodes in both lists is in range [0, 50]
- -100 <= Node.val <= 100
- Both lists are sorted in non-decreasing order

Time Complexity Target: O(n+m)
Space Complexity Target: O(1)
"""

from typing import List, Optional


def merge_two_sorted_lists(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    TODO: Implement your solution here

    Args:
        head: Head of the linked list

    Returns:
        Modified or new linked list head
    """
    pass


# Test Cases
def test_merge_two_sorted_lists():
    """Test cases for merge_two_sorted_lists"""

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
    test_merge_two_sorted_lists()
