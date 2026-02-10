"""
Problem: Jump Game (LeetCode #55)
Difficulty: Medium
Category: Dynamic Programming

Description:
Given an array nums where each element represents your maximum jump length at that position, determine if you can reach the last index.

Examples:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step to index 1, then 3 steps to last index
Input: nums = [3,2,1,0,4]
Output: false

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List, Optional


def jump_game(nums: List[int]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        nums: Array where nums[i] is the max jump length from index i

    Returns:
        True if you can reach the last index, False otherwise
    """
    pass


# Test Cases
def test_jump_game():
    """Test cases for jump_game"""

    test_cases = [
        {
            "name": "Test case 1: nums=[2,3,1,1,4] (can reach)",
            "input": [2, 3, 1, 1, 4],
            "expected": True,
        },
        {
            "name": "Test case 2: nums=[3,2,1,0,4] (cannot reach)",
            "input": [3, 2, 1, 0, 4],
            "expected": False,
        },
        {
            "name": "Edge case: single element",
            "input": [0],
            "expected": True,
        },
        {
            "name": "Edge case: two elements, can jump",
            "input": [1, 0],
            "expected": True,
        },
        {
            "name": "Edge case: two elements, cannot jump",
            "input": [0, 1],
            "expected": False,
        },
        {
            "name": "Edge case: all zeros except first",
            "input": [5, 0, 0, 0, 0],
            "expected": True,
        },
        {
            "name": "Edge case: all zeros (blocked at start)",
            "input": [0, 0, 0, 0],
            "expected": False,
        },
        {
            "name": "Edge case: large jumps",
            "input": [10, 0, 0, 0, 0],
            "expected": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = jump_game(test["input"])

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
    test_jump_game()
