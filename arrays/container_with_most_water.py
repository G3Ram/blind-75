"""
Problem: Container With Most Water (LeetCode #11)
Difficulty: Medium
Category: Arrays

Description:
Given n non-negative integers representing vertical lines on a chart, find two lines that together with the x-axis form a container with the most water.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List


def container_with_most_water(height: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        height: Array of non-negative integers representing line heights

    Returns:
        Maximum amount of water the container can store
    """
    pass


# Test Cases
def test_container_with_most_water():
    """Test cases for container_with_most_water"""

    test_cases = [
        {
            "name": "Test case 1: Basic example",
            "input": [1, 8, 6, 2, 5, 4, 8, 3, 7],
            "expected": 49
        },
        {
            "name": "Test case 2: Two elements equal",
            "input": [1, 1],
            "expected": 1
        },
        {
            "name": "Test case 3: Symmetric with best at edges",
            "input": [4, 3, 2, 1, 4],
            "expected": 16
        },
        {
            "name": "Test case 4: All zeros",
            "input": [0, 0],
            "expected": 0
        },
        {
            "name": "Edge case: Increasing heights",
            "input": [1, 2, 3, 4, 5],
            "expected": 6
        },
        {
            "name": "Edge case: Decreasing heights",
            "input": [5, 4, 3, 2, 1],
            "expected": 6
        },
        {
            "name": "Edge case: One zero",
            "input": [0, 5],
            "expected": 0
        },
        {
            "name": "Edge case: Three elements",
            "input": [1, 2, 1],
            "expected": 2
        },
        {
            "name": "Edge case: Large heights at edges",
            "input": [10, 1, 1, 1, 10],
            "expected": 40
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: height = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = container_with_most_water(test['input'])

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
    test_container_with_most_water()
