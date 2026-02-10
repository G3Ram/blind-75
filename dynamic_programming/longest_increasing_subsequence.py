"""
Problem: Longest Increasing Subsequence (LeetCode #300)
Difficulty: Medium
Category: Dynamic Programming

Description:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Examples:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: LIS is [2,3,7,101]

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

Time Complexity Target: O(n log n)
Space Complexity Target: O(n)
"""

from typing import List, Optional


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Input array of integers

    Returns:
        Length of the longest strictly increasing subsequence
    """
    pass


# Test Cases
def test_longest_increasing_subsequence():
    """Test cases for longest_increasing_subsequence"""

    test_cases = [
        {
            "name": "Test case 1: nums=[10,9,2,5,3,7,101,18]",
            "input": [10, 9, 2, 5, 3, 7, 101, 18],
            "expected": 4,
        },
        {
            "name": "Test case 2: nums=[0,1,0,3,2,3]",
            "input": [0, 1, 0, 3, 2, 3],
            "expected": 4,
        },
        {
            "name": "Test case 3: all same values (no increase)",
            "input": [7, 7, 7, 7, 7],
            "expected": 1,
        },
        {
            "name": "Edge case: single element",
            "input": [5],
            "expected": 1,
        },
        {
            "name": "Edge case: already sorted ascending",
            "input": [1, 2, 3, 4, 5],
            "expected": 5,
        },
        {
            "name": "Edge case: sorted descending",
            "input": [5, 4, 3, 2, 1],
            "expected": 1,
        },
        {
            "name": "Edge case: negative numbers",
            "input": [-3, -2, -1, 0, 1],
            "expected": 5,
        },
        {
            "name": "Mixed positive/negative: nums=[1,-1,2,-2,3]",
            "input": [1, -1, 2, -2, 3],
            "expected": 3,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = longest_increasing_subsequence(test["input"])

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
    test_longest_increasing_subsequence()
