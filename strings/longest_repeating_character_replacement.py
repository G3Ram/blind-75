"""
Problem: Longest Repeating Character Replacement (LeetCode #424)
Difficulty: Medium
Category: Strings

Description:
Given a string s and an integer k, you can choose any character and change it to any other uppercase English character at most k times. Return the length of the longest substring containing the same letter you can get after performing the operations.

Examples:
Input: s = 'ABAB', k = 2
Output: 4
Explanation: Replace the two 'A's with 'B's or vice versa

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length

Time Complexity Target: O(n)
Space Complexity Target: O(1)
"""


def longest_repeating_character_replacement(s: str, k: int) -> int:
    """
    TODO: Implement your solution here

    Args:
        s: String of uppercase English letters
        k: Maximum number of character replacements allowed

    Returns:
        Length of the longest substring with same letters after at most k replacements
    """
    pass


# Test Cases
def test_longest_repeating_character_replacement():
    """Test cases for longest_repeating_character_replacement"""

    test_cases = [
        {
            "name": "Test case 1: Alternating with k=2",
            "input": ("ABAB", 2),
            "expected": 4
        },
        {
            "name": "Test case 2: Mixed with k=2",
            "input": ("AABABBA", 1),
            "expected": 4
        },
        {
            "name": "Test case 3: All same characters",
            "input": ("AAAA", 2),
            "expected": 4
        },
        {
            "name": "Test case 4: k=0 no replacements",
            "input": ("AABABBA", 0),
            "expected": 2
        },
        {
            "name": "Test case 5: Single character string",
            "input": ("A", 0),
            "expected": 1
        },
        {
            "name": "Test case 6: k equals string length",
            "input": ("ABCD", 4),
            "expected": 4
        },
        {
            "name": "Edge case: Two characters k=1",
            "input": ("AB", 1),
            "expected": 2
        },
        {
            "name": "Edge case: All different with k=0",
            "input": ("ABCD", 0),
            "expected": 1
        },
        {
            "name": "Edge case: Large k",
            "input": ("ABCDE", 3),
            "expected": 4
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        s, k = test['input']
        print(f"\n{test['name']}")
        print(f"  Input: s = '{s}', k = {k}")
        print(f"  Expected: {test['expected']}")

        try:
            result = longest_repeating_character_replacement(s, k)

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
    test_longest_repeating_character_replacement()
