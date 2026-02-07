"""
Problem: Find Minimum in Rotated Sorted Array (LeetCode #153)
Difficulty: Medium
Category: Arrays

Description:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the rotated array, return the minimum element. Must run in O(log n) time.

Examples:
Input: nums = [3,4,5,1,2]
Output: 1
Input: nums = [4,5,6,7,0,1,2]
Output: 0

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All integers are unique

Time Complexity Target: O(log n)
Space Complexity Target: O(1)
"""

from typing import List


def find_minimum_in_rotated_sorted_array(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Rotated sorted array of unique integers

    Returns:
        The minimum element in the array
    """
    pass


# Test Cases
def test_find_minimum_in_rotated_sorted_array():
    """Test cases for find_minimum_in_rotated_sorted_array"""

    test_cases = [
        {
            "name": "Test case 1: Rotated mid-way",
            "input": [3, 4, 5, 1, 2],
            "expected": 1
        },
        {
            "name": "Test case 2: Rotated more",
            "input": [4, 5, 6, 7, 0, 1, 2],
            "expected": 0
        },
        {
            "name": "Test case 3: No rotation (sorted)",
            "input": [11, 13, 15, 17],
            "expected": 11
        },
        {
            "name": "Edge case: Single element",
            "input": [1],
            "expected": 1
        },
        {
            "name": "Edge case: Two elements, rotated",
            "input": [2, 1],
            "expected": 1
        },
        {
            "name": "Edge case: Two elements, not rotated",
            "input": [1, 2],
            "expected": 1
        },
        {
            "name": "Edge case: Minimum at second position",
            "input": [3, 1, 2],
            "expected": 1
        },
        {
            "name": "Edge case: Negative numbers",
            "input": [0, 1, 2, -5, -3],
            "expected": -5
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = find_minimum_in_rotated_sorted_array(test['input'])

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
    test_find_minimum_in_rotated_sorted_array()
