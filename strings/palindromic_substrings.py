"""
Problem: Palindromic Substrings (LeetCode #647)
Difficulty: Medium
Category: Strings

Description:
Given a string s, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward.

Examples:
Input: s = 'abc'
Output: 3
Explanation: Three palindromic substrings: 'a', 'b', 'c'
Input: s = 'aaa'
Output: 6
Explanation: 'a', 'a', 'a', 'aa', 'aa', 'aaa'

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters

Time Complexity Target: O(n²)
Space Complexity Target: O(1)
"""


def palindromic_substrings(s: str) -> int:
    """
    TODO: Implement your solution here

    Args:
        s: Input string of lowercase English letters

    Returns:
        Number of palindromic substrings in s
    """
    pass


# Test Cases
def test_palindromic_substrings():
    """Test cases for palindromic_substrings"""

    test_cases = [
        {
            "name": "Test case 1: All distinct characters",
            "input": "abc",
            "expected": 3
        },
        {
            "name": "Test case 2: All same characters",
            "input": "aaa",
            "expected": 6
        },
        {
            "name": "Test case 3: Single character",
            "input": "a",
            "expected": 1
        },
        {
            "name": "Test case 4: Two same characters",
            "input": "aa",
            "expected": 3
        },
        {
            "name": "Test case 5: Two different characters",
            "input": "ab",
            "expected": 2
        },
        {
            "name": "Test case 6: Palindrome string",
            "input": "racecar",
            "expected": 10
        },
        {
            "name": "Edge case: Longer mixed string",
            "input": "abba",
            "expected": 6
        },
        {
            "name": "Edge case: Repeated pattern",
            "input": "aaaa",
            "expected": 10
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: '{test['input']}'")
        print(f"  Expected: {test['expected']}")

        try:
            result = palindromic_substrings(test['input'])

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
    test_palindromic_substrings()
