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

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_ll(arr):
    """Convert a list to a linked list, return head."""
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def ll_to_list(head):
    """Convert a linked list to a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    TODO: Implement your solution here

    Args:
        list1: Head of the first sorted linked list
        list2: Head of the second sorted linked list

    Returns:
        Head of the merged sorted linked list
    """
    pass


# Test Cases
def test_merge_two_sorted_lists():
    """Test cases for merge_two_sorted_lists"""

    test_cases = [
        {
            "name": "Test case 1: Standard merge",
            "list1": [1, 2, 4],
            "list2": [1, 3, 4],
            "expected": [1, 1, 2, 3, 4, 4]
        },
        {
            "name": "Test case 2: Both empty",
            "list1": [],
            "list2": [],
            "expected": []
        },
        {
            "name": "Test case 3: One empty list",
            "list1": [],
            "list2": [0],
            "expected": [0]
        },
        {
            "name": "Edge case: First list empty",
            "list1": [],
            "list2": [1, 2, 3],
            "expected": [1, 2, 3]
        },
        {
            "name": "Edge case: Second list empty",
            "list1": [1, 2, 3],
            "list2": [],
            "expected": [1, 2, 3]
        },
        {
            "name": "Edge case: All same values",
            "list1": [2, 2, 2],
            "list2": [2, 2, 2],
            "expected": [2, 2, 2, 2, 2, 2]
        },
        {
            "name": "Edge case: Non-overlapping ranges",
            "list1": [1, 2, 3],
            "list2": [4, 5, 6],
            "expected": [1, 2, 3, 4, 5, 6]
        },
        {
            "name": "Edge case: Negative values",
            "list1": [-3, -1, 2],
            "list2": [-2, 0, 4],
            "expected": [-3, -2, -1, 0, 2, 4]
        },
        {
            "name": "Edge case: Single element each",
            "list1": [1],
            "list2": [2],
            "expected": [1, 2]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: list1={test['list1']}, list2={test['list2']}")
        print(f"  Expected: {test['expected']}")

        try:
            l1 = list_to_ll(test['list1'])
            l2 = list_to_ll(test['list2'])
            result_head = merge_two_sorted_lists(l1, l2)
            result = ll_to_list(result_head)

            if test['expected'] and result_head is None:
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
    test_merge_two_sorted_lists()
