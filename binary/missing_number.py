"""
Problem: Missing Number (LeetCode #268)
Difficulty: Easy
Category: Binary

Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Examples:
Input: nums = [3,0,1]
Output: 2
Explanation: Range is [0,3], missing number is 2
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All numbers are unique

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List


def missing_number(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of n distinct numbers in range [0, n]

    Returns:
        The missing number in the range [0, n]
    """
    pass


# Test Cases
def test_missing_number():
    """Test cases for missing_number"""

    test_cases = [
        {
            "name": "Test case 1: missing middle number",
            "input": [3, 0, 1],
            "expected": 2,
        },
        {
            "name": "Test case 2: missing near the end",
            "input": [9, 6, 4, 2, 3, 5, 7, 0, 1],
            "expected": 8,
        },
        {
            "name": "Edge case: single element missing 0",
            "input": [1],
            "expected": 0,
        },
        {
            "name": "Edge case: single element missing 1",
            "input": [0],
            "expected": 1,
        },
        {
            "name": "Edge case: missing last number (n)",
            "input": [0, 1, 2],
            "expected": 3,
        },
        {
            "name": "Edge case: missing first number (0)",
            "input": [1, 2, 3],
            "expected": 0,
        },
        {
            "name": "Edge case: two elements, missing middle",
            "input": [0, 2],
            "expected": 1,
        },
        {
            "name": "Edge case: sequential with missing at end",
            "input": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            "expected": 10,
        },
        {
            "name": "Edge case: reversed order missing first",
            "input": [4, 3, 2, 1],
            "expected": 0,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = missing_number(test['input'])

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
    test_missing_number()
