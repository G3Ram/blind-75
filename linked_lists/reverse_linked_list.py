"""
Problem: Reverse Linked List (LeetCode #206)
Difficulty: Easy
Category: Linked Lists

Description:
Given the head of a singly linked list, reverse the list and return the reversed list.

Examples:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Constraints:
- The number of nodes is in range [0, 5000]
- -5000 <= Node.val <= 5000

Time Complexity Target: O(n)
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


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    TODO: Implement your solution here

    Args:
        head: Head of the linked list

    Returns:
        Head of the reversed linked list
    """
    pass


# Test Cases
def test_reverse_linked_list():
    """Test cases for reverse_linked_list"""

    test_cases = [
        {
            "name": "Test case 1: Multiple nodes",
            "input": [1, 2, 3, 4, 5],
            "expected": [5, 4, 3, 2, 1]
        },
        {
            "name": "Test case 2: Two nodes",
            "input": [1, 2],
            "expected": [2, 1]
        },
        {
            "name": "Edge case: Single node",
            "input": [1],
            "expected": [1]
        },
        {
            "name": "Edge case: Empty list",
            "input": [],
            "expected": []
        },
        {
            "name": "Edge case: All same values",
            "input": [3, 3, 3],
            "expected": [3, 3, 3]
        },
        {
            "name": "Edge case: Negative values",
            "input": [-5, -3, -1, 0, 2],
            "expected": [2, 0, -1, -3, -5]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            head = list_to_ll(test['input'])
            result_head = reverse_linked_list(head)
            result = ll_to_list(result_head)

            if test['input'] and result_head is None:
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
    test_reverse_linked_list()
