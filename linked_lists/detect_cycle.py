"""
Problem: Linked List Cycle (LeetCode #141)
Difficulty: Easy
Category: Linked Lists

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it. Return true if there is a cycle, false otherwise.

Examples:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: Tail connects to 2nd node (index 1)

Constraints:
- The number of nodes is in range [0, 10^4]
- -10^5 <= Node.val <= 10^5

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_ll_with_cycle(arr, pos):
    """
    Convert a list to a linked list with an optional cycle.
    pos: index where the tail connects back to (-1 means no cycle).
    """
    if not arr:
        return None
    nodes = [ListNode(val) for val in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def detect_cycle(head: Optional[ListNode]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        head: Head of the linked list

    Returns:
        True if the linked list has a cycle, False otherwise
    """
    pass


# Test Cases
def test_detect_cycle():
    """Test cases for detect_cycle"""

    test_cases = [
        {
            "name": "Test case 1: Cycle at index 1",
            "arr": [3, 2, 0, -4],
            "pos": 1,
            "expected": True
        },
        {
            "name": "Test case 2: Cycle at index 0",
            "arr": [1, 2],
            "pos": 0,
            "expected": True
        },
        {
            "name": "Test case 3: No cycle",
            "arr": [1],
            "pos": -1,
            "expected": False
        },
        {
            "name": "Edge case: Empty list",
            "arr": [],
            "pos": -1,
            "expected": False
        },
        {
            "name": "Edge case: Single node, self-cycle",
            "arr": [1],
            "pos": 0,
            "expected": True
        },
        {
            "name": "Edge case: Long list, no cycle",
            "arr": [1, 2, 3, 4, 5, 6, 7],
            "pos": -1,
            "expected": False
        },
        {
            "name": "Edge case: Long list, cycle at start",
            "arr": [1, 2, 3, 4, 5, 6, 7],
            "pos": 0,
            "expected": True
        },
        {
            "name": "Edge case: Long list, cycle in middle",
            "arr": [1, 2, 3, 4, 5, 6, 7],
            "pos": 3,
            "expected": True
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: arr={test['arr']}, pos={test['pos']}")
        print(f"  Expected: {test['expected']}")

        try:
            head = list_to_ll_with_cycle(test['arr'], test['pos'])
            result = detect_cycle(head)

            if result is None:
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
    test_detect_cycle()
