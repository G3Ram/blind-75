"""
Problem: Longest Consecutive Sequence (LeetCode #128)
Difficulty: Medium
Category: Graphs

Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. Must run in O(n) time.

Examples:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The sequence is [1,2,3,4]

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List


def longest_consecutive_sequence(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Unsorted array of integers

    Returns:
        Length of the longest consecutive elements sequence
    """
    pass


# Test Cases
def test_longest_consecutive_sequence():
    """Test cases for longest_consecutive_sequence"""

    test_cases = [
        {
            "name": "Test case 1: scattered sequence of length 4",
            "input": [100, 4, 200, 1, 3, 2],
            "expected": 4
        },
        {
            "name": "Test case 2: longer sequence with duplicates",
            "input": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
            "expected": 9
        },
        {
            "name": "Test case 3: already sorted consecutive",
            "input": [1, 2, 3, 4, 5],
            "expected": 5
        },
        {
            "name": "Test case 4: reverse consecutive",
            "input": [5, 4, 3, 2, 1],
            "expected": 5
        },
        {
            "name": "Edge case: empty array",
            "input": [],
            "expected": 0
        },
        {
            "name": "Edge case: single element",
            "input": [7],
            "expected": 1
        },
        {
            "name": "Edge case: no consecutive pairs",
            "input": [1, 3, 5, 7],
            "expected": 1
        },
        {
            "name": "Edge case: all duplicates",
            "input": [1, 1, 1, 1],
            "expected": 1
        },
        {
            "name": "Edge case: includes negative numbers",
            "input": [-1, -2, -3, 0, 1],
            "expected": 5
        },
        {
            "name": "Edge case: two separate sequences, pick longer",
            "input": [1, 2, 3, 10, 11, 12, 13],
            "expected": 4
        },
        {
            "name": "Edge case: duplicate elements in sequence",
            "input": [1, 2, 2, 3],
            "expected": 3
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = longest_consecutive_sequence(test['input'])

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
    test_longest_consecutive_sequence()
