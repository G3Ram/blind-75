"""
Problem: Coin Change (LeetCode #322)
Difficulty: Medium
Category: Dynamic Programming

Description:
Given coins of different denominations and a total amount, return the fewest number of coins needed to make up that amount. Return -1 if impossible.

Examples:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

Time Complexity Target: O(n*amount)
Space Complexity Target: O(amount)
"""

from typing import List, Optional


def coin_change(nums: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        nums: Input array or parameters

    Returns:
        Result based on problem requirements
    """
    pass


# Test Cases
def test_coin_change():
    """Test cases for coin_change"""

    # Test case 1
    print("Test case 1...")
    # TODO: Add test case implementation

    # Test case 2
    print("Test case 2...")
    # TODO: Add test case implementation

    # Edge cases
    print("Edge case tests...")
    # TODO: Add edge case tests

    print("✓ All test cases passed!")


if __name__ == "__main__":
    test_coin_change()
