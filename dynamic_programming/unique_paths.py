"""
Problem: Unique Paths (LeetCode #62)
Difficulty: Medium
Category: Dynamic Programming

Description:
A robot on an m x n grid starts at top-left and wants to reach bottom-right. The robot can only move down or right. How many unique paths are there?

Examples:
Input: m = 3, n = 7
Output: 28
Input: m = 3, n = 2
Output: 3

Constraints:
- 1 <= m, n <= 100

Time Complexity Target: O(m*n)
Space Complexity Target: O(n)
"""

from typing import List, Optional


def unique_paths(m: int, n: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        m: Number of rows in the grid
        n: Number of columns in the grid

    Returns:
        Number of unique paths from top-left to bottom-right
    """
    pass


# Test Cases
def test_unique_paths():
    """Test cases for unique_paths"""

    test_cases = [
        {
            "name": "Test case 1: m=3, n=7",
            "m": 3,
            "n": 7,
            "expected": 28,
        },
        {
            "name": "Test case 2: m=3, n=2",
            "m": 3,
            "n": 2,
            "expected": 3,
        },
        {
            "name": "Edge case: 1x1 grid",
            "m": 1,
            "n": 1,
            "expected": 1,
        },
        {
            "name": "Edge case: single row",
            "m": 1,
            "n": 10,
            "expected": 1,
        },
        {
            "name": "Edge case: single column",
            "m": 10,
            "n": 1,
            "expected": 1,
        },
        {
            "name": "Edge case: 2x2 grid",
            "m": 2,
            "n": 2,
            "expected": 2,
        },
        {
            "name": "Symmetric grid: m=5, n=5",
            "m": 5,
            "n": 5,
            "expected": 70,
        },
        {
            "name": "Larger grid: m=10, n=10",
            "m": 10,
            "n": 10,
            "expected": 48620,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: m={test['m']}, n={test['n']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = unique_paths(test["m"], test["n"])

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
    test_unique_paths()
