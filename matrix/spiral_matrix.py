"""
Problem: Spiral Matrix (LeetCode #54)
Difficulty: Medium
Category: Matrix

Description:
Given an m x n matrix, return all elements of the matrix in spiral order (clockwise from outside to inside).

Examples:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

Time Complexity Target: O(m*n)
Space Complexity Target: O(1)
"""

from typing import List


def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        matrix: m x n integer matrix

    Returns:
        List of all elements in spiral (clockwise) order
    """
    pass


# Test Cases
def test_spiral_matrix():
    """Test cases for spiral_matrix"""

    test_cases = [
        {
            "name": "Test case 1: 3x3 matrix",
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5],
        },
        {
            "name": "Test case 2: 3x4 matrix",
            "input": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        },
        {
            "name": "Edge case: single element",
            "input": [[1]],
            "expected": [1],
        },
        {
            "name": "Edge case: single row",
            "input": [[1, 2, 3]],
            "expected": [1, 2, 3],
        },
        {
            "name": "Edge case: single column",
            "input": [[1], [2], [3]],
            "expected": [1, 2, 3],
        },
        {
            "name": "Edge case: 2x2 matrix",
            "input": [[1, 2], [3, 4]],
            "expected": [1, 2, 4, 3],
        },
        {
            "name": "Edge case: 2x3 matrix",
            "input": [[1, 2, 3], [4, 5, 6]],
            "expected": [1, 2, 3, 6, 5, 4],
        },
        {
            "name": "Edge case: negative values",
            "input": [[-1, -2], [-3, -4]],
            "expected": [-1, -2, -4, -3],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = spiral_matrix(test["input"])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
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
    test_spiral_matrix()
