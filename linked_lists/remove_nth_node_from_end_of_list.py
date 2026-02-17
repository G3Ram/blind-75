"""
Problem: Remove Nth Node From End of List (LeetCode #19)
Difficulty: Medium
Category: Linked Lists

Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Examples:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Constraints:
- The number of nodes is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

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


def remove_nth_node_from_end_of_list(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    TODO: Implement your solution here

    Args:
        head: Head of the linked list
        n: Position from the end to remove (1-indexed)

    Returns:
        Head of the modified linked list
    """
    pass


# Test Cases
def test_remove_nth_node_from_end_of_list():
    """Test cases for remove_nth_node_from_end_of_list"""

    test_cases = [
        {
            "name": "Test case 1: Remove 2nd from end of 5-node list",
            "head": [1, 2, 3, 4, 5],
            "n": 2,
            "expected": [1, 2, 3, 5]
        },
        {
            "name": "Test case 2: Remove only node (single element)",
            "head": [1],
            "n": 1,
            "expected": []
        },
        {
            "name": "Test case 3: Remove last node",
            "head": [1, 2],
            "n": 1,
            "expected": [1]
        },
        {
            "name": "Edge case: Remove first node (nth = sz)",
            "head": [1, 2, 3, 4, 5],
            "n": 5,
            "expected": [2, 3, 4, 5]
        },
        {
            "name": "Edge case: Remove last node from 5-element list",
            "head": [1, 2, 3, 4, 5],
            "n": 1,
            "expected": [1, 2, 3, 4]
        },
        {
            "name": "Edge case: Remove middle node",
            "head": [1, 2, 3, 4, 5],
            "n": 3,
            "expected": [1, 2, 4, 5]
        },
        {
            "name": "Edge case: Two nodes, remove first",
            "head": [1, 2],
            "n": 2,
            "expected": [2]
        },
        {
            "name": "Edge case: All same values",
            "head": [5, 5, 5, 5],
            "n": 2,
            "expected": [5, 5, 5]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: head={test['head']}, n={test['n']}")
        print(f"  Expected: {test['expected']}")

        try:
            head = list_to_ll(test['head'])
            result_head = remove_nth_node_from_end_of_list(head, test['n'])
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
    test_remove_nth_node_from_end_of_list()
