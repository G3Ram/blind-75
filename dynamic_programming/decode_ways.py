"""
Problem: Decode Ways (LeetCode #91)
Difficulty: Medium
Category: Dynamic Programming

Description:
A message containing letters A-Z can be encoded as numbers where 'A'=1, 'B'=2, ..., 'Z'=26. Given encoded message containing digits, return the number of ways to decode it.

Examples:
Input: s = '12'
Output: 2
Explanation: Can be decoded as 'AB' (1 2) or 'L' (12)
Input: s = '226'
Output: 3
Explanation: 'BZ', 'VF', or 'BBF'

Constraints:
- 1 <= s.length <= 100
- s contains only digits
- s may contain leading zeros

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List, Optional


def decode_ways(s: str) -> int:
    """
    TODO: Implement your solution here

    Args:
        s: String of digits to decode

    Returns:
        Number of ways to decode the string
    """
    pass


# Test Cases
def test_decode_ways():
    """Test cases for decode_ways"""

    test_cases = [
        {
            "name": "Test case 1: s='12'",
            "input": "12",
            "expected": 2,
        },
        {
            "name": "Test case 2: s='226'",
            "input": "226",
            "expected": 3,
        },
        {
            "name": "Edge case: leading zero s='06' (invalid)",
            "input": "06",
            "expected": 0,
        },
        {
            "name": "Edge case: single digit s='1'",
            "input": "1",
            "expected": 1,
        },
        {
            "name": "Edge case: zero only s='0' (invalid)",
            "input": "0",
            "expected": 0,
        },
        {
            "name": "Edge case: all same digits s='111'",
            "input": "111",
            "expected": 3,
        },
        {
            "name": "Edge case: contains zero s='10'",
            "input": "10",
            "expected": 1,
        },
        {
            "name": "Edge case: zero blocks decoding s='100'",
            "input": "100",
            "expected": 0,
        },
        {
            "name": "Larger input: s='1226'",
            "input": "1226",
            "expected": 5,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = decode_ways(test["input"])

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
    test_decode_ways()
