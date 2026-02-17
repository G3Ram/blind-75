"""
Problem: Encode and Decode Strings (LeetCode #271)
Difficulty: Medium
Category: Strings

Description:
Design an algorithm to encode a list of strings to a string and decode it back. The encoded string is then sent over the network and decoded back to the original list of strings.

Examples:
Input: strs = ['Hello','World']
Output: 'Hello', 'World'
Explanation: Encode to a single string, then decode back

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""

from typing import List


def encode(strs: List[str]) -> str:
    """
    TODO: Implement your solution here

    Args:
        strs: List of strings to encode

    Returns:
        A single encoded string representing the list
    """
    pass


def decode(s: str) -> List[str]:
    """
    TODO: Implement your solution here

    Args:
        s: Encoded string

    Returns:
        The original list of strings
    """
    pass


# Test Cases
def test_encode_and_decode_strings():
    """Test cases for encode and decode strings"""

    test_cases = [
        {
            "name": "Test case 1: Simple words",
            "input": ["Hello", "World"]
        },
        {
            "name": "Test case 2: Single string",
            "input": ["hello"]
        },
        {
            "name": "Test case 3: Strings with special characters",
            "input": ["Hello", "World", "!@#$%"]
        },
        {
            "name": "Test case 4: Empty string in list",
            "input": ["", "hello", ""]
        },
        {
            "name": "Test case 5: Single empty string",
            "input": [""]
        },
        {
            "name": "Test case 6: Strings with spaces",
            "input": ["hello world", "foo bar"]
        },
        {
            "name": "Edge case: All empty strings",
            "input": ["", "", ""]
        },
        {
            "name": "Edge case: String containing delimiter-like chars",
            "input": ["1#2", "3#4", "5"]
        },
        {
            "name": "Edge case: Multiple single chars",
            "input": ["a", "b", "c"]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")

        try:
            encoded = encode(test['input'])
            result = decode(encoded)

            if encoded is None or result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                if result == test['input']:
                    print(f"  ✓ PASSED: {result}")
                    passed += 1
                else:
                    print(f"  ✗ FAILED: Got {result} (encoded as '{encoded}')")
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
    test_encode_and_decode_strings()
