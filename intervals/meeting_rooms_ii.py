"""
Problem: Meeting Rooms II (LeetCode #253)
Difficulty: Medium
Category: Intervals

Description:
Given an array of meeting time intervals, return the minimum number of conference rooms required.

Examples:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation: Need 2 rooms at time 5-10

Constraints:
- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6

Time Complexity Target: O(n log n)
Space Complexity Target: O(n)
"""

from typing import List


def meeting_rooms_ii(intervals: List[List[int]]) -> int:
    """
    TODO: Implement your solution here

    Args:
        intervals: List of meeting time intervals [start, end]

    Returns:
        Minimum number of conference rooms required
    """
    pass


# Test Cases
def test_meeting_rooms_ii():
    """Test cases for meeting_rooms_ii"""

    test_cases = [
        {
            "name": "Test case 1: Need 2 rooms",
            "input": [[0, 30], [5, 10], [15, 20]],
            "expected": 2,
        },
        {
            "name": "Test case 2: Need 1 room",
            "input": [[7, 10], [2, 4]],
            "expected": 1,
        },
        {
            "name": "Edge case: Single meeting",
            "input": [[1, 5]],
            "expected": 1,
        },
        {
            "name": "Edge case: All meetings overlap",
            "input": [[1, 10], [1, 10], [1, 10]],
            "expected": 3,
        },
        {
            "name": "Edge case: Back-to-back meetings",
            "input": [[0, 5], [5, 10], [10, 15]],
            "expected": 1,
        },
        {
            "name": "Edge case: No overlaps",
            "input": [[1, 2], [3, 4], [5, 6]],
            "expected": 1,
        },
        {
            "name": "Edge case: Need 3 rooms at peak",
            "input": [[0, 10], [1, 9], [2, 8]],
            "expected": 3,
        },
        {
            "name": "Edge case: Rooms freed and reused",
            "input": [[0, 5], [1, 6], [5, 10], [6, 11]],
            "expected": 2,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = meeting_rooms_ii(test["input"])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                if result == test["expected"]:
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
    test_meeting_rooms_ii()
