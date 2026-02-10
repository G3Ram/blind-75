"""
Problem: Word Break (LeetCode #139)
Difficulty: Medium
Category: Dynamic Programming

Description:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

Examples:
Input: s = 'leetcode', wordDict = ['leet','code']
Output: true
Explanation: Can be segmented as 'leet code'

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- All strings consist of lowercase English letters

Time Complexity Target: O(n²)
Space Complexity Target: O(n)
"""

from typing import List, Optional


def word_break(s: str, wordDict: List[str]) -> bool:
    """
    TODO: Implement your solution here

    Args:
        s: String to segment
        wordDict: List of valid words

    Returns:
        True if s can be segmented using words in wordDict, False otherwise
    """
    pass


# Test Cases
def test_word_break():
    """Test cases for word_break"""

    test_cases = [
        {
            "name": "Test case 1: s='leetcode', wordDict=['leet','code']",
            "s": "leetcode",
            "wordDict": ["leet", "code"],
            "expected": True,
        },
        {
            "name": "Test case 2: s='applepenapple', wordDict=['apple','pen']",
            "s": "applepenapple",
            "wordDict": ["apple", "pen"],
            "expected": True,
        },
        {
            "name": "Test case 3: s='catsandog', wordDict=['cats','dog','sand','and','cat'] (impossible)",
            "s": "catsandog",
            "wordDict": ["cats", "dog", "sand", "and", "cat"],
            "expected": False,
        },
        {
            "name": "Edge case: single character word in dict",
            "s": "a",
            "wordDict": ["a"],
            "expected": True,
        },
        {
            "name": "Edge case: word not in dict",
            "s": "hello",
            "wordDict": ["world"],
            "expected": False,
        },
        {
            "name": "Edge case: repeated word usage",
            "s": "aaaa",
            "wordDict": ["aa"],
            "expected": True,
        },
        {
            "name": "Edge case: word equals full string",
            "s": "hello",
            "wordDict": ["hello"],
            "expected": True,
        },
        {
            "name": "Multiple valid segmentations exist",
            "s": "catsanddog",
            "wordDict": ["cat", "cats", "and", "sand", "dog"],
            "expected": True,
        },
    ]

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{test['name']}")
        print(f"  Input: s={test['s']!r}, wordDict={test['wordDict']}")
        print(f"  Expected: {test['expected']}")

        try:
            result = word_break(test["s"], test["wordDict"])

            if result is None:
                print(f"  ✗ FAILED: Function not yet implemented (returned None)")
                failed += 1
            else:
                if result == test["expected"]:
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
    test_word_break()
