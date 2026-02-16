"""
Problem: Merge k Sorted Lists (LeetCode #23)
Difficulty: Hard
Category: Linked Lists

Description:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Examples:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4

Time Complexity Target: O(N log k)
Space Complexity Target: O(k)
"""

from typing import List, Optional


def merge_k_sorted_lists(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    TODO: Implement your solution here

    Args:
        head: Head of the linked list

    Returns:
        Modified or new linked list head
    """
    pass


# Test Cases
def test_merge_k_sorted_lists():
    """Test cases for merge_k_sorted_lists"""

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
    test_merge_k_sorted_lists()
