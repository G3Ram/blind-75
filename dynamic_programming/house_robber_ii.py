"""
Problem: House Robber II (LeetCode #213)
Difficulty: Medium
Category: Dynamic Programming

Description:
All houses are arranged in a circle. Adjacent houses have security systems. Find maximum money you can rob without alerting police.

Examples:
Input: nums = [2,3,2]
Output: 3
Explanation: Cannot rob house 1 and 3
Input: nums = [1,2,3,1]
Output: 4

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List, Optional


def house_robber_ii(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: List of money in each house arranged in a circle

    Returns:
        Maximum money that can be robbed without robbing adjacent houses
    """
    pass


# Test Cases
def test_house_robber_ii():
    """Test cases for house_robber_ii"""

    test_cases = [
        {
            "name": "Test case 1: nums=[2,3,2]",
            "input": [2, 3, 2],
            "expected": 3,
        },
        {
            "name": "Test case 2: nums=[1,2,3,1]",
            "input": [1, 2, 3, 1],
            "expected": 4,
        },
        {
            "name": "Edge case: single house",
            "input": [5],
            "expected": 5,
        },
        {
            "name": "Edge case: two houses, take the larger",
            "input": [3, 10],
            "expected": 10,
        },
        {
            "name": "Edge case: all zeros",
            "input": [0, 0, 0, 0],
            "expected": 0,
        },
        {
            "name": "Edge case: all same value",
            "input": [3, 3, 3, 3],
            "expected": 6,
        },
        {
            "name": "Circular constraint matters: nums=[5,1,1,5]",
            "input": [5, 1, 1, 5],
            "expected": 10,
        },
        {
            "name": "Larger input: nums=[2,3,2,5,1]",
            "input": [2, 3, 2, 5, 1],
            "expected": 8,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = house_robber_ii(test["input"])

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
    test_house_robber_ii()
