"""
Problem: Minimum Interval to Include Each Query (LeetCode #1851)
Difficulty: Hard
Category: Intervals

Description:
Given intervals and queries arrays, for each query find the size of the smallest interval containing it. Return -1 if no interval contains the query.

Examples:
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]

Constraints:
- 1 <= intervals.length <= 10^5
- 1 <= queries.length <= 10^5
- intervals[i].length == 2
- 1 <= lefti <= righti <= 10^7

Time Complexity Target: O(n log n + q log q)
Space Complexity Target: O(n + q)
"""

from typing import List


def minimum_interval_to_include_each_query(intervals: List[List[int]], queries: List[int]) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        intervals: List of intervals [left, right]
        queries: List of query points

    Returns:
        List of sizes of the smallest interval containing each query, or -1 if none
    """
    pass


# Test Cases
def test_minimum_interval_to_include_each_query():
    """Test cases for minimum_interval_to_include_each_query"""

    test_cases = [
        {
            "name": "Test case 1: Multiple intervals per query",
            "intervals": [[1, 4], [2, 4], [3, 6], [4, 4]],
            "queries": [2, 3, 4, 5],
            "expected": [3, 3, 1, 4],
        },
        {
            "name": "Test case 2: Some queries not covered",
            "intervals": [[2, 3], [2, 5], [1, 8], [20, 25]],
            "queries": [2, 19, 5, 22],
            "expected": [2, -1, 4, 6],
        },
        {
            "name": "Edge case: Single interval, single query inside",
            "intervals": [[1, 10]],
            "queries": [5],
            "expected": [10],
        },
        {
            "name": "Edge case: Single interval, query outside",
            "intervals": [[1, 5]],
            "queries": [6],
            "expected": [-1],
        },
        {
            "name": "Edge case: Query at interval boundary (left)",
            "intervals": [[1, 5]],
            "queries": [1],
            "expected": [5],
        },
        {
            "name": "Edge case: Query at interval boundary (right)",
            "intervals": [[1, 5]],
            "queries": [5],
            "expected": [5],
        },
        {
            "name": "Edge case: All queries not covered",
            "intervals": [[1, 2], [3, 4]],
            "queries": [5, 6, 7],
            "expected": [-1, -1, -1],
        },
        {
            "name": "Edge case: Nested intervals, pick smallest",
            "intervals": [[1, 10], [2, 8], [3, 6]],
            "queries": [4],
            "expected": [4],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: intervals={test['intervals']}, queries={test['queries']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = minimum_interval_to_include_each_query(test["intervals"], test["queries"])

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
    test_minimum_interval_to_include_each_query()
