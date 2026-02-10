"""
Problem: Coin Change II (LeetCode #518)
Difficulty: Medium
Category: Dynamic Programming

Description:
Given coins of different denominations and a total amount, return the number of combinations that make up that amount.

Examples:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1

Constraints:
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- 0 <= amount <= 5000

Time Complexity Target: O(n*amount)
Space Complexity Target: O(amount)
"""

from typing import List, Optional


def coin_change_ii(amount: int, coins: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        amount: Target amount to make
        coins: List of coin denominations

    Returns:
        Number of combinations that make up the amount
    """
    pass


# Test Cases
def test_coin_change_ii():
    """Test cases for coin_change_ii"""

    test_cases = [
        {
            "name": "Test case 1: amount=5, coins=[1,2,5]",
            "amount": 5,
            "coins": [1, 2, 5],
            "expected": 4,
        },
        {
            "name": "Test case 2: amount=3, coins=[2] (impossible)",
            "amount": 3,
            "coins": [2],
            "expected": 0,
        },
        {
            "name": "Edge case: amount=0 (one way - use no coins)",
            "amount": 0,
            "coins": [1, 2, 5],
            "expected": 1,
        },
        {
            "name": "Edge case: single coin equals amount",
            "amount": 10,
            "coins": [10],
            "expected": 1,
        },
        {
            "name": "Edge case: coins larger than amount",
            "amount": 3,
            "coins": [5, 10],
            "expected": 0,
        },
        {
            "name": "Multiple combos: amount=10, coins=[1,5,10]",
            "amount": 10,
            "coins": [1, 5, 10],
            "expected": 4,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: amount={test['amount']}, coins={test['coins']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = coin_change_ii(test["amount"], test["coins"])

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
    test_coin_change_ii()
