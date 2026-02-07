"""
Problem: Product of Array Except Self (LeetCode #238)
Difficulty: Medium
Category: Arrays

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements of nums except nums[i]. Must run in O(n) time without using division.

Examples:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- Product fits in 32-bit integer
- Must be O(n) without division

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List


def product_of_array_except_self(nums: List[int]) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        nums: Input array of integers

    Returns:
        Array where answer[i] is the product of all elements except nums[i]
    """
    pass


# Test Cases
def test_product_of_array_except_self():
    """Test cases for product_of_array_except_self"""

    test_cases = [
        {
            "name": "Test case 1: Basic example",
            "input": [1, 2, 3, 4],
            "expected": [24, 12, 8, 6]
        },
        {
            "name": "Test case 2: Contains zero",
            "input": [1, 0],
            "expected": [0, 1]
        },
        {
            "name": "Test case 3: Two zeros",
            "input": [0, 0],
            "expected": [0, 0]
        },
        {
            "name": "Test case 4: Contains negative numbers",
            "input": [-1, 1, 0, -3, 3],
            "expected": [0, 0, 9, 0, 0]
        },
        {
            "name": "Edge case: Two elements",
            "input": [2, 3],
            "expected": [3, 2]
        },
        {
            "name": "Edge case: All ones",
            "input": [1, 1, 1, 1],
            "expected": [1, 1, 1, 1]
        },
        {
            "name": "Edge case: Contains zero in middle",
            "input": [1, 2, 0],
            "expected": [0, 0, 2]
        },
        {
            "name": "Edge case: All negative",
            "input": [-2, -3, -4],
            "expected": [12, 8, 6]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = product_of_array_except_self(test['input'])

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
    test_product_of_array_except_self()
