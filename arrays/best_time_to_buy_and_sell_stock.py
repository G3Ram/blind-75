"""
Problem: Best Time to Buy and Sell Stock (LeetCode #121)
Difficulty: Easy
Category: Arrays

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize profit by choosing a single day to buy and one day in the future to sell. Return the maximum profit, or 0 if no profit.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List


def best_time_to_buy_and_sell_stock(prices: List[int]) -> int:
    """
    TODO: Implement your solution here

    Args:
        prices: Array where prices[i] is the stock price on day i

    Returns:
        Maximum profit achievable, or 0 if no profit is possible
    """
    pass


# Test Cases
def test_best_time_to_buy_and_sell_stock():
    """Test cases for best_time_to_buy_and_sell_stock"""

    test_cases = [
        {
            "name": "Test case 1: Basic example",
            "input": [7, 1, 5, 3, 6, 4],
            "expected": 5
        },
        {
            "name": "Test case 2: Decreasing prices, no profit",
            "input": [7, 6, 4, 3, 1],
            "expected": 0
        },
        {
            "name": "Test case 3: Buy low sell high in middle",
            "input": [3, 2, 6, 5, 0, 3],
            "expected": 4
        },
        {
            "name": "Edge case: Single element",
            "input": [1],
            "expected": 0
        },
        {
            "name": "Edge case: Two elements, profit",
            "input": [1, 2],
            "expected": 1
        },
        {
            "name": "Edge case: Two elements, no profit",
            "input": [2, 1],
            "expected": 0
        },
        {
            "name": "Edge case: All same prices",
            "input": [3, 3, 3, 3],
            "expected": 0
        },
        {
            "name": "Edge case: Max profit at very end",
            "input": [1, 2, 3, 4, 5],
            "expected": 4
        },
        {
            "name": "Edge case: Best buy is not first element",
            "input": [2, 4, 1],
            "expected": 2
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: prices = {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = best_time_to_buy_and_sell_stock(test['input'])

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
    test_best_time_to_buy_and_sell_stock()
