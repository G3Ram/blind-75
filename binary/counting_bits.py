"""
Problem: Counting Bits (LeetCode #338)
Difficulty: Easy
Category: Binary

Description:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Examples:
Input: n = 2
Output: [0,1,1]
Explanation: 0 has 0 ones, 1 has 1 one, 2 (10) has 1 one
Input: n = 5
Output: [0,1,1,2,1,2]

Constraints:
- 0 <= n <= 10^5

Time Complexity Target: O(n)
Space Complexity Target: O(n)
"""

from typing import List


def counting_bits(n: int) -> List[int]:
    """
    TODO: Implement your solution here

    Args:
        n: Non-negative integer upper bound

    Returns:
        Array of length n+1 where ans[i] = number of 1-bits in i
    """
    pass


# Test Cases
def test_counting_bits():
    """Test cases for counting_bits"""

    test_cases = [
        {
            "name": "Test case 1: n=2",
            "input": 2,
            "expected": [0, 1, 1],
        },
        {
            "name": "Test case 2: n=5",
            "input": 5,
            "expected": [0, 1, 1, 2, 1, 2],
        },
        {
            "name": "Edge case: n=0 (only 0 itself)",
            "input": 0,
            "expected": [0],
        },
        {
            "name": "Edge case: n=1",
            "input": 1,
            "expected": [0, 1],
        },
        {
            "name": "Edge case: n=4 (power of 2 boundary)",
            "input": 4,
            "expected": [0, 1, 1, 2, 1],
        },
        {
            "name": "Edge case: n=8",
            "input": 8,
            "expected": [0, 1, 1, 2, 1, 2, 2, 3, 1],
        },
        {
            "name": "Edge case: n=7 (all values 0-7)",
            "input": 7,
            "expected": [0, 1, 1, 2, 1, 2, 2, 3],
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = counting_bits(test['input'])

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
    test_counting_bits()
