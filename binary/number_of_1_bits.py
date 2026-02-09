"""
Problem: Number of 1 Bits (LeetCode #191)
Difficulty: Easy
Category: Binary

Description:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Examples:
Input: n = 11
Output: 3
Explanation: Binary: 00000000000000000000000000001011
Input: n = 128
Output: 1
Explanation: Binary: 00000000000000000000000010000000

Constraints:
- 1 <= n <= 2^31 - 1

Time Complexity Target: O(1)
Space Complexity Target: O(1)
"""


def number_of_1_bits(n: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        n: An unsigned 32-bit integer

    Returns:
        Number of '1' bits in the binary representation of n
    """
    pass


# Test Cases
def test_number_of_1_bits():
    """Test cases for number_of_1_bits"""

    test_cases = [
        {
            "name": "Test case 1: n=11 (binary 1011)",
            "input": 11,
            "expected": 3,
        },
        {
            "name": "Test case 2: n=128 (binary 10000000)",
            "input": 128,
            "expected": 1,
        },
        {
            "name": "Edge case: minimum value n=1 (binary 1)",
            "input": 1,
            "expected": 1,
        },
        {
            "name": "Edge case: power of 2 (single bit set)",
            "input": 1024,
            "expected": 1,
        },
        {
            "name": "Edge case: n=7 (binary 111, three consecutive 1s)",
            "input": 7,
            "expected": 3,
        },
        {
            "name": "Edge case: n=2147483647 (2^31-1, all 31 bits set)",
            "input": 2147483647,
            "expected": 31,
        },
        {
            "name": "Edge case: n=2147483648 (2^31, only highest bit set)",
            "input": 2147483648,
            "expected": 1,
        },
        {
            "name": "Edge case: alternating bits n=1431655765 (01010101...)",
            "input": 1431655765,
            "expected": 16,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = number_of_1_bits(test['input'])

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
    test_number_of_1_bits()
