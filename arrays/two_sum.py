"""
Problem: Two Sum (LeetCode #1)
Difficulty: Easy
Category: Arrays

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- Only one valid answer exists

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List, Optional


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        nums: Input array of integers
        target: Target sum to find

    Returns:
        List of two indices whose values add up to target
    """
    pass


# Test Cases
def test_two_sum():
    """Test cases for two_sum"""

    # Test case 1: Basic example
    print("Test case 1: nums = [2,7,11,15], target = 9")
    result = two_sum([2, 7, 11, 15], 9)
    assert result == [0, 1], f"Expected [0, 1], got {result}"
    print(f"✓ Passed: {result}")

    # Test case 2: Target at end
    print("\nTest case 2: nums = [3,2,4], target = 6")
    result = two_sum([3, 2, 4], 6)
    assert result == [1, 2], f"Expected [1, 2], got {result}"
    print(f"✓ Passed: {result}")

    # Test case 3: Same number used
    print("\nTest case 3: nums = [3,3], target = 6")
    result = two_sum([3, 3], 6)
    assert result == [0, 1], f"Expected [0, 1], got {result}"
    print(f"✓ Passed: {result}")

    # Edge case: Negative numbers
    print("\nEdge case: nums = [-1,-2,-3,-4,-5], target = -8")
    result = two_sum([-1, -2, -3, -4, -5], -8)
    assert result == [2, 4], f"Expected [2, 4], got {result}"
    print(f"✓ Passed: {result}")

    print("\n✓ All test cases passed!")


if __name__ == "__main__":
    test_two_sum()
