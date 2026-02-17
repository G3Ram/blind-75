"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Difficulty: Medium
Category: Strings

Description:
Given a string s, find the length of the longest substring without repeating characters.

Examples:
Input: s = 'abcabcbb'
Output: 3
Explanation: Answer is 'abc' with length 3
Input: s = 'bbbbb'
Output: 1
Explanation: Answer is 'b'

Constraints:
- 0 <= s.length <= 5*10^4
- s consists of English letters, digits, symbols and spaces

Time Complexity Target: O(n)
Space Complexity Target: O(min(m,n))
"""


def longest_substring_without_repeating_characters(s: str) -> int:
    """
    TODO: Implement your solution here

    Args:
        s: Input string

    Returns:
        Length of the longest substring without repeating characters
    """
    pass


# Test Cases
def test_longest_substring_without_repeating_characters():
    """Test cases for longest_substring_without_repeating_characters"""

    test_cases = [
        {
            "name": "Test case 1: Repeating pattern",
            "input": "abcabcbb",
            "expected": 3
        },
        {
            "name": "Test case 2: All same characters",
            "input": "bbbbb",
            "expected": 1
        },
        {
            "name": "Test case 3: Partial repeat",
            "input": "pwwkew",
            "expected": 3
        },
        {
            "name": "Test case 4: Empty string",
            "input": "",
            "expected": 0
        },
        {
            "name": "Test case 5: Single character",
            "input": "a",
            "expected": 1
        },
        {
            "name": "Test case 6: All unique characters",
            "input": "abcdef",
            "expected": 6
        },
        {
            "name": "Edge case: Two characters same",
            "input": "aa",
            "expected": 1
        },
        {
            "name": "Edge case: Space character",
            "input": "a b",
            "expected": 3
        },
        {
            "name": "Edge case: Digits and letters",
            "input": "a1b2c3",
            "expected": 6
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: '{test['input']}'")
        print(f"  Expected: {test['expected']}")

        try:
            result = longest_substring_without_repeating_characters(test['input'])

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
    test_longest_substring_without_repeating_characters()
