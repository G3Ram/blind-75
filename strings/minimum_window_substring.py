"""
Problem: Minimum Window Substring (LeetCode #76)
Difficulty: Hard
Category: Strings

Description:
Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If no such substring exists, return empty string.

Examples:
Input: s = 'ADOBECODEBANC', t = 'ABC'
Output: 'BANC'

Constraints:
- m == s.length, n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters

Time Complexity Target: O(m+n)
Space Complexity Target: O(m+n)
"""


def minimum_window_substring(s: str, t: str) -> str:
    """
    TODO: Implement your solution here

    Args:
        s: The source string to search within
        t: The target string whose characters must all be in the window

    Returns:
        The minimum window substring of s containing all characters of t,
        or empty string if no such window exists
    """
    pass


# Test Cases
def test_minimum_window_substring():
    """Test cases for minimum_window_substring"""

    test_cases = [
        {
            "name": "Test case 1: Standard case",
            "input": ("ADOBECODEBANC", "ABC"),
            "expected": "BANC"
        },
        {
            "name": "Test case 2: s equals t",
            "input": ("A", "A"),
            "expected": "A"
        },
        {
            "name": "Test case 3: t longer than s - impossible",
            "input": ("A", "AA"),
            "expected": ""
        },
        {
            "name": "Test case 4: No valid window",
            "input": ("ADOBECODEBANC", "XYZ"),
            "expected": ""
        },
        {
            "name": "Test case 5: t has duplicates",
            "input": ("AAAB", "AAB"),
            "expected": "AAAB"
        },
        {
            "name": "Test case 6: Minimum window at end",
            "input": ("ADOBEC", "CE"),
            "expected": "OBEC"
        },
        {
            "name": "Edge case: Single character match",
            "input": ("ABC", "B"),
            "expected": "B"
        },
        {
            "name": "Edge case: Repeated characters in s",
            "input": ("AABBC", "ABC"),
            "expected": "ABBC"
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        s, t = test['input']
        print(f"\n{test['name']}")
        print(f"  Input: s = '{s}', t = '{t}'")
        print(f"  Expected: '{test['expected']}'")

        try:
            result = minimum_window_substring(s, t)

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                if result == test['expected']:
                    print(f"  ✓ PASSED: '{result}'")
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
    test_minimum_window_substring()
