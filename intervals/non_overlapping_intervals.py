"""
Problem: Non-overlapping Intervals (LeetCode #435)
Difficulty: Medium
Category: Intervals

Description:
Given an array of intervals, return the minimum number of intervals you need to remove to make the rest non-overlapping.

Examples:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: Remove [1,3] to make rest non-overlapping

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5*10^4 <= starti < endi <= 5*10^4

Time Complexity Target: O(n log n)
Space Complexity Target: O(1)
"""

from typing import List


def non_overlapping_intervals(intervals: List[List[int]]) -> int:
    """
    TODO: Implement your solution here

    Args:
        intervals: List of intervals [start, end]

    Returns:
        Minimum number of intervals to remove to make rest non-overlapping
    """
    pass


# Test Cases
def test_non_overlapping_intervals():
    """Test cases for non_overlapping_intervals"""

    test_cases = [
        {
            "name": "Test case 1: Remove one interval",
            "input": [[1, 2], [2, 3], [3, 4], [1, 3]],
            "expected": 1,
        },
        {
            "name": "Test case 2: Already non-overlapping",
            "input": [[1, 2], [2, 3]],
            "expected": 0,
        },
        {
            "name": "Test case 3: Remove all but one",
            "input": [[1, 2], [1, 2], [1, 2]],
            "expected": 2,
        },
        {
            "name": "Edge case: Single interval",
            "input": [[1, 5]],
            "expected": 0,
        },
        {
            "name": "Edge case: Two overlapping intervals",
            "input": [[1, 5], [2, 6]],
            "expected": 1,
        },
        {
            "name": "Edge case: No overlaps",
            "input": [[1, 2], [3, 4], [5, 6]],
            "expected": 0,
        },
        {
            "name": "Edge case: All overlapping, many to remove",
            "input": [[1, 100], [11, 22], [1, 11], [2, 12]],
            "expected": 2,
        },
        {
            "name": "Edge case: Negative values",
            "input": [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95]],
            "expected": 1,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = non_overlapping_intervals(test["input"])

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
    test_non_overlapping_intervals()
