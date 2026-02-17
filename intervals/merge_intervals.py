"""
Problem: Merge Intervals (LeetCode #56)
Difficulty: Medium
Category: Intervals

Description:
Given an array of intervals, merge all overlapping intervals and return an array of non-overlapping intervals.

Examples:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: [1,3] and [2,6] overlap

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

Time Complexity Target: O(n log n)
Space Complexity Target: O(n)
"""

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        intervals: List of intervals [start, end]

    Returns:
        List of merged non-overlapping intervals
    """
    pass


# Test Cases
def test_merge_intervals():
    """Test cases for merge_intervals"""

    test_cases = [
        {
            "name": "Test case 1: Multiple overlapping intervals",
            "input": [[1, 3], [2, 6], [8, 10], [15, 18]],
            "expected": [[1, 6], [8, 10], [15, 18]],
        },
        {
            "name": "Test case 2: All intervals overlap into one",
            "input": [[1, 4], [4, 5]],
            "expected": [[1, 5]],
        },
        {
            "name": "Edge case: Single interval",
            "input": [[1, 3]],
            "expected": [[1, 3]],
        },
        {
            "name": "Edge case: No overlapping intervals",
            "input": [[1, 2], [3, 4], [5, 6]],
            "expected": [[1, 2], [3, 4], [5, 6]],
        },
        {
            "name": "Edge case: All same intervals",
            "input": [[2, 4], [2, 4], [2, 4]],
            "expected": [[2, 4]],
        },
        {
            "name": "Edge case: Unsorted input",
            "input": [[15, 18], [1, 3], [2, 6], [8, 10]],
            "expected": [[1, 6], [8, 10], [15, 18]],
        },
        {
            "name": "Edge case: One interval contains another",
            "input": [[1, 10], [2, 5]],
            "expected": [[1, 10]],
        },
        {
            "name": "Edge case: All intervals merge into one",
            "input": [[1, 4], [2, 6], [5, 9]],
            "expected": [[1, 9]],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = merge_intervals(test["input"])

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
    test_merge_intervals()
