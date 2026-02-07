"""
Problem: Search in Rotated Sorted Array (LeetCode #33)
Difficulty: Medium
Category: Arrays

Description:
Given the array nums after rotation and an integer target, return the index of target if it is in nums, or -1 if not. Must achieve O(log n) runtime.

Examples:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values are unique

Time Complexity Target: O(log n)
Space Complexity Target: O(1)
"""

from typing import List


def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Rotated sorted array of unique integers
        target: Integer to search for

    Returns:
        Index of target if found, otherwise -1
    """
    pass


# Test Cases
def test_search_in_rotated_sorted_array():
    """Test cases for search_in_rotated_sorted_array"""

    test_cases = [
        {
            "name": "Test case 1: Target found in rotated array",
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 0,
            "expected": 4
        },
        {
            "name": "Test case 2: Target not present",
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 3,
            "expected": -1
        },
        {
            "name": "Test case 3: Single element, found",
            "nums": [1],
            "target": 1,
            "expected": 0
        },
        {
            "name": "Test case 4: Single element, not found",
            "nums": [1],
            "target": 0,
            "expected": -1
        },
        {
            "name": "Edge case: Target is pivot element",
            "nums": [3, 1, 2],
            "target": 3,
            "expected": 0
        },
        {
            "name": "Edge case: Two elements, target is second",
            "nums": [3, 1],
            "target": 1,
            "expected": 1
        },
        {
            "name": "Edge case: Two elements, target is first",
            "nums": [3, 1],
            "target": 3,
            "expected": 0
        },
        {
            "name": "Edge case: Target at last position",
            "nums": [5, 1, 3],
            "target": 3,
            "expected": 2
        },
        {
            "name": "Edge case: No rotation, target found",
            "nums": [1, 2, 3, 4, 5],
            "target": 3,
            "expected": 2
        },
        {
            "name": "Edge case: No rotation, target not found",
            "nums": [1, 2, 3, 4, 5],
            "target": 6,
            "expected": -1
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums = {test['nums']}, target = {test['target']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = search_in_rotated_sorted_array(test['nums'], test['target'])

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
    test_search_in_rotated_sorted_array()
