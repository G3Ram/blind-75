"""
Problem: Pacific Atlantic Water Flow (LeetCode #417)
Difficulty: Medium
Category: Graphs

Description:
Given an m x n matrix of heights representing an island, return coordinates of cells where water can flow to both Pacific (top/left edges) and Atlantic (bottom/right edges) oceans.

Examples:
Input: heights = [[1,2,3],[8,9,4],[7,6,5]]
Output: [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

Constraints:
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

Time Complexity Target: O(m*n)
Space Complexity Target: O(m*n)
"""

from typing import List


def pacific_atlantic_water_flow(heights: List[List[int]]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        heights: m x n matrix of non-negative integers representing heights

    Returns:
        List of [row, col] coordinates where water can flow to both oceans
    """
    pass


# Test Cases
def test_pacific_atlantic_water_flow():
    """Test cases for pacific_atlantic_water_flow"""

    test_cases = [
        {
            "name": "Test case 1: 3x3 grid",
            "input": [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
            "expected": [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        },
        {
            "name": "Test case 2: LeetCode example 5x5",
            "input": [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4]
            ],
            "expected": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        },
        {
            "name": "Edge case: single cell",
            "input": [[5]],
            "expected": [[0, 0]]
        },
        {
            "name": "Edge case: single row",
            "input": [[1, 2, 3]],
            "expected": [[0, 0], [0, 1], [0, 2]]
        },
        {
            "name": "Edge case: single column",
            "input": [[1], [2], [3]],
            "expected": [[0, 0], [1, 0], [2, 0]]
        },
        {
            "name": "Edge case: all same height",
            "input": [[3, 3], [3, 3]],
            "expected": [[0, 0], [0, 1], [1, 0], [1, 1]]
        },
        {
            "name": "Edge case: increasing heights (all cells flow to both)",
            "input": [[1, 2], [3, 4]],
            "expected": [[0, 1], [1, 0], [1, 1]]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = pacific_atlantic_water_flow(test['input'])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                result_sorted = sorted(result)
                expected_sorted = sorted(test['expected'])
                if result_sorted == expected_sorted:
                    print(f"  ✓ PASSED: {result_sorted}")
                    passed += 1
                else:
                    print(f"  ✗ FAILED: Got {result_sorted}")
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
    test_pacific_atlantic_water_flow()
