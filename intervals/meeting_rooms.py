"""
Problem: Meeting Rooms (LeetCode #252)
Difficulty: Easy
Category: Intervals

Description:
Given an array of meeting time intervals consisting of start and end times, determine if a person could attend all meetings.

Examples:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: Meetings overlap

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2

Time Complexity Target: O(n log n)
Space Complexity Target: O(1)
"""

from typing import List


def meeting_rooms(intervals: List[List[int]]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        intervals: List of meeting time intervals [start, end]

    Returns:
        True if a person can attend all meetings, False otherwise
    """
    pass


# Test Cases
def test_meeting_rooms():
    """Test cases for meeting_rooms"""

    test_cases = [
        {
            "name": "Test case 1: Overlapping meetings",
            "input": [[0, 30], [5, 10], [15, 20]],
            "expected": False,
        },
        {
            "name": "Test case 2: Non-overlapping meetings",
            "input": [[7, 10], [2, 4]],
            "expected": True,
        },
        {
            "name": "Edge case: Empty intervals",
            "input": [],
            "expected": True,
        },
        {
            "name": "Edge case: Single meeting",
            "input": [[5, 10]],
            "expected": True,
        },
        {
            "name": "Edge case: Back-to-back meetings (touching endpoints)",
            "input": [[0, 5], [5, 10]],
            "expected": True,
        },
        {
            "name": "Edge case: All same times",
            "input": [[1, 5], [1, 5], [1, 5]],
            "expected": False,
        },
        {
            "name": "Edge case: Two meetings exactly overlapping",
            "input": [[1, 10], [2, 9]],
            "expected": False,
        },
        {
            "name": "Edge case: Many non-overlapping meetings",
            "input": [[1, 2], [3, 4], [5, 6], [7, 8]],
            "expected": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = meeting_rooms(test["input"])

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
    test_meeting_rooms()
