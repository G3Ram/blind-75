"""
Problem: Maximum Product Subarray (LeetCode #152)
Difficulty: Medium
Category: Arrays

Description:
Given an integer array nums, find a subarray that has the largest product, and return the product.

Examples:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: Subarray [2,3] has product 6

Constraints:
- 1 <= nums.length <= 2*10^4
- -10 <= nums[i] <= 10

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List


def maximum_product_subarray(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Input array of integers

    Returns:
        The largest product of any contiguous subarray
    """
    pass


# Test Cases
def test_maximum_product_subarray():
    """Test cases for maximum_product_subarray"""

    test_cases = [
        {
            "name": "Test case 1: Basic example",
            "input": [2, 3, -2, 4],
            "expected": 6
        },
        {
            "name": "Test case 2: Contains zero",
            "input": [-2, 0, -1],
            "expected": 0
        },
        {
            "name": "Test case 3: Two negatives make positive",
            "input": [-2, 3, -4],
            "expected": 24
        },
        {
            "name": "Edge case: Single positive element",
            "input": [1],
            "expected": 1
        },
        {
            "name": "Edge case: Single negative element",
            "input": [-1],
            "expected": -1
        },
        {
            "name": "Edge case: Zero separates subarrays",
            "input": [0, 2],
            "expected": 2
        },
        {
            "name": "Edge case: All negative, odd count",
            "input": [-3, -1, -1],
            "expected": 3
        },
        {
            "name": "Edge case: All negative, even count",
            "input": [-2, -3],
            "expected": 6
        },
        {
            "name": "Edge case: All positive",
            "input": [1, 2, 3, 4],
            "expected": 24
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = maximum_product_subarray(test['input'])

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
    test_maximum_product_subarray()
