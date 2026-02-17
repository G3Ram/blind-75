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


def reorder_list(head: Optional[ListNode]) -> None:
    """
    TODO: Implement your solution here

    Modifies the list in-place. Does not return a value.

    Args:
        head: Head of the linked list
    """
    pass


# Test Cases
def test_reorder_list():
    """Test cases for reorder_list"""

    test_cases = [
        {
            "name": "Test case 1: Even-length list",
            "input": [1, 2, 3, 4],
            "expected": [1, 4, 2, 3]
        },
        {
            "name": "Test case 2: Odd-length list",
            "input": [1, 2, 3, 4, 5],
            "expected": [1, 5, 2, 4, 3]
        },
        {
            "name": "Edge case: Single node",
            "input": [1],
            "expected": [1]
        },
        {
            "name": "Edge case: Two nodes",
            "input": [1, 2],
            "expected": [1, 2]
        },
        {
            "name": "Edge case: Three nodes",
            "input": [1, 2, 3],
            "expected": [1, 3, 2]
        },
        {
            "name": "Edge case: All same values",
            "input": [5, 5, 5, 5, 5],
            "expected": [5, 5, 5, 5, 5]
        },
        {
            "name": "Edge case: Six nodes",
            "input": [1, 2, 3, 4, 5, 6],
            "expected": [1, 6, 2, 5, 3, 4]
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
            reorder_list(head)
            result = ll_to_list(head)

            if result == test['input'] and test['input'] != test['expected']:
                print(f"  ✗ FAILED: Function not yet implemented (list unchanged)")
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
    test_reorder_list()
