"""
Problem: Two Sum (LeetCode #1)
Difficulty: Easy
Category: Arrays

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- Only one valid answer exists

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        nums: Input array of integers
        target: Target sum to find

    Returns:
        List of two indices whose values add up to target
    """
    pass


# Test Cases
def test_two_sum():
    """Test cases for two_sum"""

    test_cases = [
        {
            "name": "Test case 1: Basic example",
            "input": ([2, 7, 11, 15], 9),
            "expected": [0, 1]
        },
        {
            "name": "Test case 2: Target at end",
            "input": ([3, 2, 4], 6),
            "expected": [1, 2]
        },
        {
            "name": "Test case 3: Same number used",
            "input": ([3, 3], 6),
            "expected": [0, 1]
        },
        {
            "name": "Edge case: Negative numbers",
            "input": ([-1, -2, -3, -4, -5], -8),
            "expected": [2, 4]
        }
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums = {test['input'][0]}, target = {test['input'][1]}")
        print(f"  Expected: {test['expected']}")

        try:
            result = two_sum(test['input'][0], test['input'][1])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            elif result == test['expected']:
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
    test_two_sum()
