"""
Problem: Valid Palindrome (LeetCode #125)
Difficulty: Easy
Category: Strings

Description:
Given a string s, return true if it is a palindrome, otherwise false. Consider only alphanumeric characters and ignore cases.

Examples:
Input: s = 'A man, a plan, a canal: Panama'
Output: true
Input: s = 'race a car'
Output: false

Constraints:
- 1 <= s.length <= 2*10^5
- s consists only of printable ASCII characters

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""


def valid_palindrome(s: str) -> bool:
    """
    TODO: Implement your solution here

    Args:
        s: Input string (may contain non-alphanumeric characters)

    Returns:
        True if s is a palindrome considering only alphanumeric characters, False otherwise
    """
    pass


# Test Cases
def test_valid_palindrome():
    """Test cases for valid_palindrome"""

    test_cases = [
        {
            "name": "Test case 1: Classic palindrome with punctuation",
            "input": "A man, a plan, a canal: Panama",
            "expected": True
        },
        {
            "name": "Test case 2: Not a palindrome",
            "input": "race a car",
            "expected": False
        },
        {
            "name": "Test case 3: Empty string (only spaces)",
            "input": " ",
            "expected": True
        },
        {
            "name": "Test case 4: Single character",
            "input": "a",
            "expected": True
        },
        {
            "name": "Test case 5: Simple palindrome",
            "input": "racecar",
            "expected": True
        },
        {
            "name": "Test case 6: Mixed case palindrome",
            "input": "Madam",
            "expected": True
        },
        {
            "name": "Edge case: Numbers as palindrome",
            "input": "12321",
            "expected": True
        },
        {
            "name": "Edge case: Alphanumeric mix",
            "input": "0P",
            "expected": False
        },
        {
            "name": "Edge case: All same characters",
            "input": "aaa",
            "expected": True
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: '{test['input']}'")
        print(f"  Expected: {test['expected']}")

        try:
            result = valid_palindrome(test['input'])

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
    test_valid_palindrome()
