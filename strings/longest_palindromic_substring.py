"""
Problem: Longest Palindromic Substring (LeetCode #5)
Difficulty: Medium
Category: Strings

Description:
Given a string s, return the longest palindromic substring in s.

Examples:
Input: s = 'babad'
Output: 'bab' or 'aba'
Explanation: Both are valid
Input: s = 'cbbd'
Output: 'bb'

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters

Time Complexity Target: O(n²)
Space Complexity Target: O(1)
"""


def longest_palindromic_substring(s: str) -> str:
    """
    TODO: Implement your solution here

    Args:
        s: Input string

    Returns:
        The longest palindromic substring in s
    """
    pass


# Test Cases
def test_longest_palindromic_substring():
    """Test cases for longest_palindromic_substring"""

    test_cases = [
        {
            "name": "Test case 1: Multiple valid answers",
            "input": "babad",
            "valid_answers": ["bab", "aba"]
        },
        {
            "name": "Test case 2: Even-length palindrome",
            "input": "cbbd",
            "valid_answers": ["bb"]
        },
        {
            "name": "Test case 3: Single character",
            "input": "a",
            "valid_answers": ["a"]
        },
        {
            "name": "Test case 4: All same characters",
            "input": "aaaa",
            "valid_answers": ["aaaa"]
        },
        {
            "name": "Test case 5: Entire string is palindrome",
            "input": "racecar",
            "valid_answers": ["racecar"]
        },
        {
            "name": "Test case 6: Two characters same",
            "input": "bb",
            "valid_answers": ["bb"]
        },
        {
            "name": "Edge case: Palindrome at end",
            "input": "xyzabba",
            "valid_answers": ["abba"]
        },
        {
            "name": "Edge case: Palindrome at start",
            "input": "abbaxyz",
            "valid_answers": ["abba"]
        },
        {
            "name": "Edge case: All different characters",
            "input": "abcd",
            "valid_answers": ["a", "b", "c", "d"]
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: '{test['input']}'")
        print(f"  Expected (any of): {test['valid_answers']}")

        try:
            result = longest_palindromic_substring(test['input'])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                if result in test['valid_answers']:
                    print(f"  ✓ PASSED: '{result}'")
                    passed += 1
                else:
                    # Also check if result is a valid palindrome of max length
                    max_len = max(len(a) for a in test['valid_answers'])
                    is_palindrome = result == result[::-1]
                    if is_palindrome and len(result) == max_len:
                        print(f"  ✓ PASSED: '{result}' (valid palindrome of correct length)")
                        passed += 1
                    else:
                        print(f"  ✗ FAILED: Got '{result}'")
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
    test_longest_palindromic_substring()
