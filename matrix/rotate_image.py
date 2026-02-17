"""
Problem: Rotate Image (LeetCode #48)
Difficulty: Medium
Category: Matrix

Description:
Given an n x n 2D matrix representing an image, rotate the image by 90 degrees clockwise. Must rotate the matrix in-place.

Examples:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

Time Complexity Target: O(n²)
Space Complexity Target: O(1)
"""

import copy
from typing import List


def rotate_image(matrix: List[List[int]]) -> None:
    """
    TODO: Implement your solution here

    Rotates matrix 90 degrees clockwise in-place. Returns None.

    Args:
        matrix: n x n integer matrix

    Returns:
        None (modifies matrix in-place)
    """
    pass


# Test Cases
def test_rotate_image():
    """Test cases for rotate_image"""

    test_cases = [
        {
            "name": "Test case 1: 3x3 matrix",
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        },
        {
            "name": "Test case 2: 4x4 matrix",
            "input": [
                [5, 1, 9, 11],
                [2, 4, 8, 10],
                [13, 3, 6, 7],
                [15, 14, 12, 16],
            ],
            "expected": [
                [15, 13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7, 10, 11],
            ],
        },
        {
            "name": "Edge case: single element",
            "input": [[1]],
            "expected": [[1]],
        },
        {
            "name": "Edge case: 2x2 matrix",
            "input": [[1, 2], [3, 4]],
            "expected": [[3, 1], [4, 2]],
        },
        {
            "name": "Edge case: all same values",
            "input": [[5, 5], [5, 5]],
            "expected": [[5, 5], [5, 5]],
        },
        {
            "name": "Edge case: negative values",
            "input": [[-1, -2], [-3, -4]],
            "expected": [[-3, -1], [-4, -2]],
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
            rotate_image(matrix)
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
    test_rotate_image()
