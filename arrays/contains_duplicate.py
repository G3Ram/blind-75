"""
Problem: Contains Duplicate (LeetCode #217)
Difficulty: Easy
Category: Arrays

Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Examples:
Input: nums = [1,2,3,1]
Output: true
Input: nums = [1,2,3,4]
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        nums: Input array of integers

    Returns:
        True if any value appears at least twice, False if all elements are distinct
    """
    pass


# Test Cases
def test_contains_duplicate():
    """Test cases for contains_duplicate"""

    test_cases = [
        {
            "name": "Test case 1: Has duplicate",
            "input": [1, 2, 3, 1],
            "expected": True
        },
        {
            "name": "Test case 2: No duplicates",
            "input": [1, 2, 3, 4],
            "expected": False
        },
        {
            "name": "Test case 3: Multiple duplicates",
            "input": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            "expected": True
        },
        {
            "name": "Edge case: Single element",
            "input": [1],
            "expected": False
        },
        {
            "name": "Edge case: Two same elements",
            "input": [5, 5],
            "expected": True
        },
        {
            "name": "Edge case: Two different elements",
            "input": [1, 2],
            "expected": False
        },
        {
            "name": "Edge case: Negative numbers with duplicate",
            "input": [-1, -2, -3, -1],
            "expected": True
        },
        {
            "name": "Edge case: Negative numbers, no duplicate",
            "input": [-3, -2, -1, 0],
            "expected": False
        },
        {
            "name": "Edge case: All same elements",
            "input": [7, 7, 7, 7],
            "expected": True
        },
        {
            "name": "Edge case: Duplicate at end only",
            "input": [1, 2, 3, 4, 5, 1],
            "expected": True
        },
        {
            "name": "Edge case: Large values",
            "input": [10**9, -(10**9), 10**9],
            "expected": True
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = contains_duplicate(test['input'])

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
    test_contains_duplicate()
