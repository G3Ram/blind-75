"""
Problem: Insert Interval (LeetCode #57)
Difficulty: Medium
Category: Intervals

Description:
Given a set of non-overlapping intervals sorted by start time, insert a new interval and merge if necessary.

Examples:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- newInterval.length == 2
- Intervals are sorted by start time

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List


def insert_interval(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        intervals: List of non-overlapping intervals sorted by start time
        newInterval: New interval to insert

    Returns:
        List of merged intervals after inserting newInterval
    """
    pass


# Test Cases
def test_insert_interval():
    """Test cases for insert_interval"""

    test_cases = [
        {
            "name": "Test case 1: Insert overlapping interval",
            "intervals": [[1, 3], [6, 9]],
            "newInterval": [2, 5],
            "expected": [[1, 5], [6, 9]],
        },
        {
            "name": "Test case 2: Insert interval merging multiple",
            "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            "newInterval": [4, 8],
            "expected": [[1, 2], [3, 10], [12, 16]],
        },
        {
            "name": "Edge case: Empty intervals list",
            "intervals": [],
            "newInterval": [5, 7],
            "expected": [[5, 7]],
        },
        {
            "name": "Edge case: Insert before all intervals",
            "intervals": [[3, 5], [6, 9]],
            "newInterval": [1, 2],
            "expected": [[1, 2], [3, 5], [6, 9]],
        },
        {
            "name": "Edge case: Insert after all intervals",
            "intervals": [[1, 3], [6, 9]],
            "newInterval": [10, 15],
            "expected": [[1, 3], [6, 9], [10, 15]],
        },
        {
            "name": "Edge case: New interval covers all existing",
            "intervals": [[1, 2], [3, 4], [5, 6]],
            "newInterval": [0, 10],
            "expected": [[0, 10]],
        },
        {
            "name": "Edge case: No overlap, insert in middle",
            "intervals": [[1, 2], [7, 9]],
            "newInterval": [4, 5],
            "expected": [[1, 2], [4, 5], [7, 9]],
        },
        {
            "name": "Edge case: Single interval, overlapping",
            "intervals": [[1, 5]],
            "newInterval": [2, 3],
            "expected": [[1, 5]],
        },
        {
            "name": "Edge case: Adjacent intervals merge",
            "intervals": [[1, 3], [6, 9]],
            "newInterval": [3, 6],
            "expected": [[1, 9]],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: intervals={test['intervals']}, newInterval={test['newInterval']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = insert_interval(test["intervals"], test["newInterval"])

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
    test_insert_interval()
