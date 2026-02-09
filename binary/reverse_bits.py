"""
Problem: Reverse Bits (LeetCode #190)
Difficulty: Easy
Category: Binary

Description:
Reverse bits of a given 32-bit unsigned integer.

Examples:
Input: n = 43261596 (00000010100101000001111010011100)
Output: 964176192 (00111001011110000010100101000000)
Input: n = 4294967293 (11111111111111111111111111111101)
Output: 3221225471 (10111111111111111111111111111111)

Constraints:
- The input must be a binary string of length 32
- 0 <= n <= 2^32 - 1

Time Complexity Target: O(1)
Space Complexity Target: O(1)
"""


def reverse_bits(n: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        n: A 32-bit unsigned integer

    Returns:
        The integer whose bits are the reverse of n's 32-bit binary representation
    """
    pass


# Test Cases
def test_reverse_bits():
    """Test cases for reverse_bits"""

    test_cases = [
        {
            "name": "Test case 1: n=43261596 (00000010100101000001111010011100)",
            "input": 43261596,
            "expected": 964176192,
        },
        {
            "name": "Test case 2: n=4294967293 (11111111111111111111111111111101)",
            "input": 4294967293,
            "expected": 3221225471,
        },
        {
            "name": "Edge case: n=0 (all zeros)",
            "input": 0,
            "expected": 0,
        },
        {
            "name": "Edge case: n=1 (LSB set, becomes MSB after reverse)",
            "input": 1,
            "expected": 2147483648,
        },
        {
            "name": "Edge case: n=2147483648 (only MSB set, becomes LSB after reverse)",
            "input": 2147483648,
            "expected": 1,
        },
        {
            "name": "Edge case: n=4294967295 (all 32 bits set)",
            "input": 4294967295,
            "expected": 4294967295,
        },
        {
            "name": "Edge case: n=2 (00000000000000000000000000000010)",
            "input": 2,
            "expected": 1073741824,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = reverse_bits(test['input'])

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
    test_reverse_bits()
