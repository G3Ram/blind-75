"""
Problem: Alien Dictionary (LeetCode #269)
Difficulty: Hard
Category: Graphs

Description:
Given a sorted dictionary of an alien language with unique letters, derive the order of letters in this language. If order is invalid, return empty string.

Examples:
Input: words = ['wrt','wrf','er','ett','rftt']
Output: 'wertf'

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters

Time Complexity Target: O(C)
Space Complexity Target: O(1)
"""

from typing import List


def alien_dictionary(words: List[str]) -> str:
    """
    TODO: Implement your solution here

    Args:
        words: List of words sorted lexicographically in the alien language

    Returns:
        String of characters in the alien language order, or '' if invalid
    """
    pass


def is_valid_alien_order(words: List[str], order: str) -> bool:
    """Helper to validate that a given order is consistent with the word list."""
    chars_in_words = set(''.join(words))
    if set(order) != chars_in_words or len(order) != len(chars_in_words):
        return False
    rank = {c: i for i, c in enumerate(order)}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        found_diff = False
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                if rank[w1[j]] >= rank[w2[j]]:
                    return False
                found_diff = True
                break
        if not found_diff and len(w1) > len(w2):
            return False
    return True


# Test Cases
def test_alien_dictionary():
    """Test cases for alien_dictionary"""

    test_cases = [
        {
            "name": "Test case 1: five words derive unique order",
            "input": ['wrt', 'wrf', 'er', 'ett', 'rftt'],
            "expected_valid": True,
            "invalid_expected": None
        },
        {
            "name": "Test case 2: two words simple order",
            "input": ['z', 'x'],
            "expected_valid": True,
            "invalid_expected": None
        },
        {
            "name": "Test case 3: cycle makes order invalid",
            "input": ['z', 'x', 'z'],
            "expected_valid": False,
            "invalid_expected": ""
        },
        {
            "name": "Test case 4: longer word before prefix (invalid)",
            "input": ['abc', 'ab'],
            "expected_valid": False,
            "invalid_expected": ""
        },
        {
            "name": "Edge case: single word",
            "input": ['z'],
            "expected_valid": True,
            "invalid_expected": None
        },
        {
            "name": "Edge case: all same word",
            "input": ['abc', 'abc'],
            "expected_valid": True,
            "invalid_expected": None
        },
        {
            "name": "Edge case: single letter words forming chain",
            "input": ['a', 'b', 'c'],
            "expected_valid": True,
            "invalid_expected": None
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: {test['input']}")
        print(f"  Expected valid order: {test['expected_valid']}")

        try:
            result = alien_dictionary(test['input'])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            elif not test['expected_valid']:
                # Expect invalid (empty string)
                if result == "":
                    print(f"  ✓ PASSED: '' (correctly identified as invalid)")
                    passed += 1
                else:
                    print(f"  ✗ FAILED: Expected '' for invalid input, got '{result}'")
                    failed += 1
            else:
                # Expect a valid ordering
                if result == "":
                    print(f"  ✗ FAILED: Got empty string but expected a valid order")
                    failed += 1
                elif is_valid_alien_order(test['input'], result):
                    print(f"  ✓ PASSED: '{result}' (valid alien order)")
                    passed += 1
                else:
                    print(f"  ✗ FAILED: Got '{result}' which is not a valid alien order")
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
    test_alien_dictionary()
