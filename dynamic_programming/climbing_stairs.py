"""
Problem: Climbing Stairs (LeetCode #70)
Difficulty: Easy
Category: Dynamic Programming

Description:
You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Examples:
Input: n = 2
Output: 2
Explanation: 1+1, or 2
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, or 2+1

Constraints:
- 1 <= n <= 45

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List, Optional


def climbing_stairs(n: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        n: Number of stairs to climb

    Returns:
        Number of distinct ways to climb to the top
    """
    pass


# Test Cases
def test_climbing_stairs():
    """Test cases for climbing_stairs"""

    test_cases = [
        {
            "name": "Test case 1: n=2",
            "input": 2,
            "expected": 2,
        },
        {
            "name": "Test case 2: n=3",
            "input": 3,
            "expected": 3,
        },
        {
            "name": "Edge case: n=1 (single step)",
            "input": 1,
            "expected": 1,
        },
        {
            "name": "Base case: n=4",
            "input": 4,
            "expected": 5,
        },
        {
            "name": "Larger input: n=10",
            "input": 10,
            "expected": 89,
        },
        {
            "name": "Max constraint: n=45",
            "input": 45,
            "expected": 1836311903,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = climbing_stairs(test["input"])

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
    test_climbing_stairs()
