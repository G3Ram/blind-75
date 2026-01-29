"""
Problem: 3Sum (LeetCode #15)
Difficulty: Medium
Category: Arrays

Description:
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that i != j != k and nums[i] + nums[j] + nums[k] == 0.

Examples:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Time Complexity Target: O(n²)
Space Complexity Target: O(n)
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    TODO: Implement your solution here

    Args:
        nums: Input array of integers

    Returns:
        List of all unique triplets that sum to zero
    """
    pass


# Test Cases
def test_three_sum():
    """Test cases for three_sum"""

    test_cases = [
        {
            "name": "Test case 1: Multiple triplets",
            "input": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, -1, 2], [-1, 0, 1]]
        },
        {
            "name": "Test case 2: No valid triplets",
            "input": [0, 1, 1],
            "expected": []
        },
        {
            "name": "Test case 3: All zeros",
            "input": [0, 0, 0],
            "expected": [[0, 0, 0]]
        },
        {
            "name": "Test case 4: Single triplet",
            "input": [-2, 0, 2],
            "expected": [[-2, 0, 2]]
        },
        {
            "name": "Edge case: Exactly 3 elements, valid",
            "input": [-1, 0, 1],
            "expected": [[-1, 0, 1]]
        },
        {
            "name": "Edge case: Exactly 3 elements, invalid",
            "input": [1, 2, 3],
            "expected": []
        },
        {
            "name": "Edge case: All same positive numbers",
            "input": [1, 1, 1],
            "expected": []
        },
        {
            "name": "Edge case: All same negative numbers",
            "input": [-1, -1, -1],
            "expected": []
        },
        {
            "name": "Edge case: Duplicates in input",
            "input": [-2, 0, 0, 2, 2],
            "expected": [[-2, 0, 2]]
        },
        {
            "name": "Edge case: All positive numbers",
            "input": [1, 2, 3, 4, 5],
            "expected": []
        },
        {
            "name": "Edge case: All negative numbers",
            "input": [-5, -4, -3, -2, -1],
            "expected": []
        }
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: nums = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = three_sum(test['input'])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                # Sort both result and expected for order-independent comparison
                result_sorted = sorted([sorted(t) for t in result])
                expected_sorted = sorted([sorted(t) for t in test['expected']])

                if result_sorted == expected_sorted:
                    print(f"  ✓ PASSED: {result_sorted}")
                    passed += 1
                else:
                    print(f"  ✗ FAILED: Got {result_sorted}")
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
    test_three_sum()
