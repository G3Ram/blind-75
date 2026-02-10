"""
Problem: Combination Sum IV (LeetCode #377)
Difficulty: Medium
Category: Dynamic Programming

Description:
Given an array of distinct integers and a target, return the number of possible combinations that add up to target. Different sequences count as different combinations.

Examples:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation: [1,1,1,1], [1,1,2], [1,2,1], [1,3], [2,1,1], [2,2], [3,1]

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All elements are unique
- 1 <= target <= 1000

Time Complexity Target: O(target*n)
Space Complexity Target: O(target)
"""

from typing import List, Optional


def combination_sum_iv(nums: List[int], target: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Array of distinct integers
        target: Target sum to reach

    Returns:
        Number of possible combinations (sequences) that sum to target
    """
    pass


# Test Cases
def test_combination_sum_iv():
    """Test cases for combination_sum_iv"""

    test_cases = [
        {
            "name": "Test case 1: nums=[1,2,3], target=4",
            "nums": [1, 2, 3],
            "target": 4,
            "expected": 7,
        },
        {
            "name": "Test case 2: nums=[9], target=3 (impossible)",
            "nums": [9],
            "target": 3,
            "expected": 0,
        },
        {
            "name": "Edge case: target=1, nums=[1,2,3]",
            "nums": [1, 2, 3],
            "target": 1,
            "expected": 1,
        },
        {
            "name": "Edge case: single element equals target",
            "nums": [5],
            "target": 5,
            "expected": 1,
        },
        {
            "name": "Edge case: target smaller than all nums",
            "nums": [3, 5, 7],
            "target": 2,
            "expected": 0,
        },
        {
            "name": "Multiple sequences: nums=[1,2], target=3",
            "nums": [1, 2],
            "target": 3,
            "expected": 3,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums={test['nums']}, target={test['target']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = combination_sum_iv(test["nums"], test["target"])

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
    test_combination_sum_iv()
