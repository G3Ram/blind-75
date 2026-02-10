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


def coin_change(coins: List[int], amount: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        coins: List of coin denominations
        amount: Target amount to make

    Returns:
        Fewest number of coins to make up amount, or -1 if impossible
    """
    pass


# Test Cases
def test_coin_change():
    """Test cases for coin_change"""

    test_cases = [
        {
            "name": "Test case 1: coins=[1,2,5], amount=11",
            "coins": [1, 2, 5],
            "amount": 11,
            "expected": 3,
        },
        {
            "name": "Test case 2: coins=[2], amount=3 (impossible)",
            "coins": [2],
            "amount": 3,
            "expected": -1,
        },
        {
            "name": "Edge case: amount=0",
            "coins": [1, 2, 5],
            "amount": 0,
            "expected": 0,
        },
        {
            "name": "Edge case: single coin equals amount",
            "coins": [5],
            "amount": 5,
            "expected": 1,
        },
        {
            "name": "Edge case: amount=1, coin=[1]",
            "coins": [1],
            "amount": 1,
            "expected": 1,
        },
        {
            "name": "Multiple coins, greedy fails: coins=[1,3,4], amount=6",
            "coins": [1, 3, 4],
            "amount": 6,
            "expected": 2,
        },
        {
            "name": "Large amount: coins=[1,2,5], amount=100",
            "coins": [1, 2, 5],
            "amount": 100,
            "expected": 20,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: coins={test['coins']}, amount={test['amount']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = coin_change(test["coins"], test["amount"])

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
    test_coin_change()
