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


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    TODO: Implement your solution here

    Args:
        lists: Array of heads of k sorted linked lists

    Returns:
        Head of the merged sorted linked list
    """
    pass


# Test Cases
def test_merge_k_sorted_lists():
    """Test cases for merge_k_sorted_lists"""

    test_cases = [
        {
            "name": "Test case 1: Three lists",
            "lists": [[1, 4, 5], [1, 3, 4], [2, 6]],
            "expected": [1, 1, 2, 3, 4, 4, 5, 6]
        },
        {
            "name": "Test case 2: Empty input array",
            "lists": [],
            "expected": []
        },
        {
            "name": "Test case 3: Single empty list",
            "lists": [[]],
            "expected": []
        },
        {
            "name": "Edge case: Single list",
            "lists": [[1, 2, 3]],
            "expected": [1, 2, 3]
        },
        {
            "name": "Edge case: All empty lists",
            "lists": [[], [], []],
            "expected": []
        },
        {
            "name": "Edge case: All single-element lists",
            "lists": [[3], [1], [4], [1], [5]],
            "expected": [1, 1, 3, 4, 5]
        },
        {
            "name": "Edge case: Non-overlapping ranges",
            "lists": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9]
        },
        {
            "name": "Edge case: Negative values",
            "lists": [[-5, -3, 0], [-4, -1, 2]],
            "expected": [-5, -4, -3, -1, 0, 2]
        },
        {
            "name": "Edge case: All same values",
            "lists": [[2, 2], [2, 2], [2]],
            "expected": [2, 2, 2, 2, 2]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['lists']}")
        print(f"  Expected: {test['expected']}")

        try:
            linked_lists = [list_to_ll(arr) for arr in test['lists']]
            result_head = merge_k_sorted_lists(linked_lists)
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
    test_merge_k_sorted_lists()
