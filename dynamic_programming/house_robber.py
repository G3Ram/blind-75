"""
Problem: House Robber (LeetCode #198)
Difficulty: Medium
Category: Dynamic Programming

Description:
You are a robber planning to rob houses along a street. Each house has money, but adjacent houses have security systems connected. Find maximum money you can rob without robbing adjacent houses.

Examples:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) then house 3 (money = 3)
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob houses 1, 3, and 5

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List, Optional


def house_robber(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: List of money in each house

    Returns:
        Maximum money that can be robbed without robbing adjacent houses
    """
    pass


# Test Cases
def test_house_robber():
    """Test cases for house_robber"""

    test_cases = [
        {
            "name": "Test case 1: nums=[1,2,3,1]",
            "input": [1, 2, 3, 1],
            "expected": 4,
        },
        {
            "name": "Test case 2: nums=[2,7,9,3,1]",
            "input": [2, 7, 9, 3, 1],
            "expected": 12,
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
            "name": "Increasing values",
            "input": [1, 2, 3, 4, 5],
            "expected": 9,
        },
        {
            "name": "Max values: all 400",
            "input": [400, 400, 400, 400, 400],
            "expected": 1200,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = house_robber(test["input"])

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
    test_house_robber()
