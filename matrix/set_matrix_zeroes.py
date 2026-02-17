"""
Problem: Set Matrix Zeroes (LeetCode #73)
Difficulty: Medium
Category: Matrix

Description:
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Must do it in-place.

Examples:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

Time Complexity Target: O(m*n)
Space Complexity Target: O(1)
"""

import copy
from typing import List


def set_matrix_zeroes(matrix: List[List[int]]) -> None:
    """
    TODO: Implement your solution here

    Modifies matrix in-place. Returns None.

    Args:
        matrix: m x n integer matrix

    Returns:
        None (modifies matrix in-place)
    """
    pass


# Test Cases
def test_set_matrix_zeroes():
    """Test cases for set_matrix_zeroes"""

    test_cases = [
        {
            "name": "Test case 1: single zero in middle",
            "input": [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            "expected": [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        },
        {
            "name": "Test case 2: zeros in first and last columns",
            "input": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        },
        {
            "name": "Edge case: single element zero",
            "input": [[0]],
            "expected": [[0]],
        },
        {
            "name": "Edge case: single element non-zero",
            "input": [[1]],
            "expected": [[1]],
        },
        {
            "name": "Edge case: no zeros present",
            "input": [[1, 2], [3, 4]],
            "expected": [[1, 2], [3, 4]],
        },
        {
            "name": "Edge case: all zeros",
            "input": [[0, 0], [0, 0]],
            "expected": [[0, 0], [0, 0]],
        },
        {
            "name": "Edge case: zero in corner",
            "input": [[0, 1, 1], [1, 1, 1], [1, 1, 1]],
            "expected": [[0, 0, 0], [0, 1, 1], [0, 1, 1]],
        },
        {
            "name": "Edge case: multiple zeros in same row",
            "input": [[1, 0, 1], [0, 1, 1], [1, 1, 1]],
            "expected": [[0, 0, 0], [0, 0, 0], [0, 0, 1]],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            matrix = copy.deepcopy(test["input"])
            set_matrix_zeroes(matrix)
            result = matrix

            if result == test["input"] and test["input"] != test["expected"]:
                print(f"  ✗ FAILED: Function not yet implemented (matrix unchanged)")
                failed += 1
            elif result == test["expected"]:
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
    test_set_matrix_zeroes()
