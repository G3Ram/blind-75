"""
Problem: Number of Islands (LeetCode #200)
Difficulty: Medium
Category: Graphs

Description:
Given an m x n 2D grid of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

Examples:
Input: grid = [['1','1','0'],['1','1','0'],['0','0','1']]
Output: 2

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

Time Complexity Target: O(m*n)
Space Complexity Target: O(m*n)
"""

from typing import List


def number_of_islands(grid: List[List[str]]) -> int:
    """
    TODO: Implement your solution here

    Args:
        grid: m x n grid of '1's (land) and '0's (water)

    Returns:
        Number of islands
    """
    pass


# Test Cases
def test_number_of_islands():
    """Test cases for number_of_islands"""

    test_cases = [
        {
            "name": "Test case 1: two islands",
            "input": [['1','1','0'],['1','1','0'],['0','0','1']],
            "expected": 2
        },
        {
            "name": "Test case 2: one large island",
            "input": [['1','1','1'],['0','1','0'],['1','1','1']],
            "expected": 1
        },
        {
            "name": "Test case 3: four separate islands",
            "input": [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']],
            "expected": 3
        },
        {
            "name": "Edge case: single land cell",
            "input": [['1']],
            "expected": 1
        },
        {
            "name": "Edge case: single water cell",
            "input": [['0']],
            "expected": 0
        },
        {
            "name": "Edge case: all water",
            "input": [['0','0'],['0','0']],
            "expected": 0
        },
        {
            "name": "Edge case: all land",
            "input": [['1','1'],['1','1']],
            "expected": 1
        },
        {
            "name": "Edge case: diagonal land not connected",
            "input": [['1','0'],['0','1']],
            "expected": 2
        },
        {
            "name": "Edge case: checkerboard pattern",
            "input": [['1','0','1'],['0','1','0'],['1','0','1']],
            "expected": 5
        },
        {
            "name": "Edge case: single row all land",
            "input": [['1','1','1','1']],
            "expected": 1
        },
        {
            "name": "Edge case: single column alternating",
            "input": [['1'],['0'],['1'],['0'],['1']],
            "expected": 3
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = number_of_islands(test['input'])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                if result == test['expected']:
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
    test_number_of_islands()
